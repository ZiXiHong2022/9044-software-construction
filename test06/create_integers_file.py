#!/usr/bin/env python3

import sys

file = open(sys.argv[3], 'w')
for index in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    print(index, file=file)