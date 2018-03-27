#!/usr/bin/env python3

import sys


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

    if capital in capitals_cities.values():
        for k in capitals_cities.keys():
            if capitals_cities[k] == capital:
                for state in states.keys():
                    if states[state] == k:
                        print(state)
                        return
    else:
        print("Unknown capital city")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        uneautrefonction(sys.argv[1])
