#!/usr/bin/env python3

import sys
import os
import re
import settings


def getSettings():
    ret = {}
    for k in settings.__dict__.keys():
        if not (k.startswith('__') or k.startswith('_')):
            ret[k] = settings.__dict__[k]
    return ret

def render(template_file):
    out_file = re.sub(".template$", ".html", template_file)
    stg = getSettings()

    with open(template_file, "r") as rf,\
            open(out_file, "w") as wf:
        for line in rf:
            for k in stg.keys():
                line = re.sub("\{" + k + "\}", stg[k], line)
            print(line, end='', file=wf)

if __name__ == '__main__':
    if len(sys.argv) == 2 \
           and re.search(".template$", sys.argv[1]) \
           and os.access(sys.argv[1], os.R_OK):
        render(sys.argv[1])
    else:
        print("Usage:", sys.argv[0], "FILE.template")
