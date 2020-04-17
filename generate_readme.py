#!/usr/bin/env python

import os

def lookup_desc(path):
    desc = ""
    with open(path, "r") as entry:
        data = entry.readline(1024)
        if data.startswith("<!-- desc: "):
            desc = " - %s" % data[11:-6]
    return desc

def list_items(prefix):
    arr = []
    for item in os.listdir(prefix):
        cur_path = os.path.join(prefix, item)
        if os.path.isdir(cur_path):
            deeper_path = os.path.join(cur_path, "%s.md" % item)
            arr.append("[%s](%s)%s\n" % (os.path.splitext(item)[0], deeper_path, lookup_desc(deeper_path)))
        elif os.path.isfile(cur_path):
            arr.append("[%s](%s)%s\n" % (os.path.splitext(item)[0], cur_path, lookup_desc(cur_path)))
    return arr

def main():

    data = []

    data.append("# crazychenz/notebooks\n")
    data.append("A repository for general engineering notes, journalism, and other forms of expression.\n")
    data.append("## Journal Entries\n")

    data.extend(list_items('journal'))

    data.append("## Notebooks\n")

    data.extend(list_items('notebooks'))

    with open('README.md', "w") as readme:
        readme.write(''.join(data))

if __name__ == "__main__":
    main()

