#!/usr/bin/env python3

import sys


def unefonction(state):
    """Ceci est une fonction"""

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capitals_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if states.get(state):
        print(capitals_cities[states[state]])
    else:
        print("Unknown state")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        unefonction(sys.argv[1])
