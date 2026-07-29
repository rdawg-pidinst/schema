#! /usr/bin/python3

import gitprops

def main():
    print("\\newcommand{\\schemaversion}{%s}" % gitprops.get_version())
    print("\\newcommand{\\schemadate}{%s}" % gitprops.get_date())

if __name__ == "__main__":
    main()
