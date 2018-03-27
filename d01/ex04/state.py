#!/usr/bin/env python3

import sys


def get_key(h, v):
    """Super Opti"""

    if v not in h.values():
        return None

    for k in h.keys():
        if h[k] == v:
            return k
    return None


def uneautrefonction(capital):
    """Ceci est une autre fonction"""

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

    akr = get_key(capitals_cities, capital)
    if akr is not None:
        print(get_key(states, akr))
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        uneautrefonction(sys.argv[1])
