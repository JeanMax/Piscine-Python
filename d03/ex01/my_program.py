#!/usr/bin/env python3

# import sys
from local_lib.path import Path


def create_dir(p):
    p.mkdir_p()


def create_file(p, my_file, my_content):
    p2 = p / my_file
    p2.write_text(my_content)
    return p2


def read_file(p2, my_file):
    with p2.open("r") as f:
        for l in f:
            print(l)


if __name__ == "__main__":

    my_dir = "/tmp/dir"
    my_file = "file"
    my_content = "blabla content blabla"
    p = Path(my_dir)

    create_dir(p)
    p2 = create_file(p, my_file, my_content)
    read_file(p2, my_file)
