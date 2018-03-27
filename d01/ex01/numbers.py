#!/usr/bin/env python3


def sort_file(filename):
    """Another useful function"""

    numbers = []
    with open(filename, "r") as f:
        for line in f:
            numbers += line.replace("\n", "").split(",")

    for n in numbers:
        print(n)


if __name__ == '__main__':
    sort_file("./ex01/numbers.txt")  # TODO: do not hardcode filename
