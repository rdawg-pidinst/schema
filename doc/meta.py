#! /usr/bin/python3

import gitprops

def main():
    version = gitprops.get_version()
    date = gitprops.get_date()
    print("\\newcommand{\\schemaversion}{%s}" % version)
    print("\\newcommand{\\schemarelease}{%s}" % version.base_version)
    print("\\newcommand{\\schemadate}{%s}" % date)

if __name__ == "__main__":
    main()
