#!/usr/bin/env python3

import sys
import requests as req
import dewiki
# import json


def z(q):
    url = "https://en.wikipedia.org/w/api.php"
    param = (
        "?action=query&titles=" + q +
        "&prop=revisions&rvprop=content&format=json&formatversion=2"
    )

    r = req.get(url + param)
    if r.status_code != 200:
        print("Request failed", file=sys.stderr)
        return

    try:
        content = r.json()["query"]["pages"][0]["revisions"][0]["content"]
    except KeyError as e:
        if "invalidreason" in r.json()["query"]["pages"][0].keys():
            print(
                "Invalid query:",
                r.json()["query"]["pages"][0]["invalidreason"],
                file=sys.stderr
            )
        else:
            print("Nothing found ):", file=sys.stderr)
        return
    except Exception as e:
        print(repr(e), file=sys.stderr)
        return

    if (type(content) != str or len(content) == 0):
        print("Nothing found ):", file=sys.stderr)  # parano

    out_file = "".join(q.split()) + ".wiki"
    with open(out_file, "w") as f:
        print(dewiki.from_string(content), file=f)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        z(sys.argv[1])
    else:
        print("Usage:", sys.argv[0], "query", file=sys.stderr)
