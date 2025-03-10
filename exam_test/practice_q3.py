#!/usr/bin/env python3

import sys

first_name = set()

lines = sys.stdin.readlines()

for line in lines:
    parts = line.strip().split('|')
    if parts[4] == 'M':
        part = parts[2].split(',')
        first_name.add(part[0])


for i in sorted(first_name):
    print(i)

