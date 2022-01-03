#! /usr/bin/python3

import datetime
import os
from pathlib import Path
import subprocess

class GitProps:
    """Determine properties of the git repository.
    """

    def __init__(self, root="."):
        self.root = Path(root).resolve()

    def _exec(self, cmd):
        proc = subprocess.run(cmd.split(),
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              cwd=self.root,
                              check=True,
                              env=dict(os.environ, LC_ALL='C'),
                              universal_newlines=True)
        return proc.stdout.strip()

    @property
    def commit(self):
        return self._exec("git log -1 --format=%H")

    @property
    def tag(self):
        try:
            return self._exec("git describe --exact-match %s" % self.commit)
        except subprocess.CalledProcessError:
            return None

    @property
    def is_dirty(self):
        return bool(self._exec("git status --porcelain --untracked-files=no"))

    @property
    def date(self):
        if self.is_dirty:
            d = datetime.date.today()
        else:
            tag = self.tag
            if tag:
                cmd = "git tag -l --format=%%(taggerdate:unix) %s" % tag
                ts = int(self._exec(cmd))
            else:
                ts = int(self._exec("git log -1 --format=%ad --date=unix"))
            d = datetime.date.fromtimestamp(ts)
        return d.strftime("%e %B %Y").strip()

    @property
    def version(self):
        return self._exec("git describe --always --dirty").strip()

def main():
    git = GitProps()
    print("\\newcommand{\\schemaversion}{%s}" % git.version)
    print("\\newcommand{\\schemadate}{%s}" % git.date)

if __name__ == "__main__":
    main()
