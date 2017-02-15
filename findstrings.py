#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re

chars = r"A-Za-z0-9/\-:.,_$%'()[\]<> "
shortest_run = 4

regexp = '[%s]{%d,}' % (chars, shortest_run)
pattern = re.compile(regexp)

def process(stream):
    data = stream.read()
    return pattern.findall(data)

if __name__ == "__main__":
    for found_str in process(sys.stdin):
        print found_str