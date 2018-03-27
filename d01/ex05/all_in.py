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


def encoreunefonction(user_input):
    """Ceci est encore une fonction"""

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

    for s in [" ".join([y.capitalize() for y in x.strip().split(" ")])
              for x in user_input.split(",") if len(x.strip()) > 0]:  # eheheh
        akr = get_key(capitals_cities, s)
        if akr is not None:
            print(
                s, "is the capital of",
                get_key(states, akr),
                "(akr:", akr + ")"
            )
        elif states.get(s):
            print(
                    capitals_cities[states[s]],
                    "is the capital of", s,
                    "(akr:", states[s] + ")"
                )
        else:
            print(s, "is neither a capital city nor a state")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        encoreunefonction(sys.argv[1])
