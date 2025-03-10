#!/usr/bin/env python3
import sys
import re

lines =sys.stdin
surnames = set()
for line in lines:
    part = line.strip().split('|')
    if part[4] == 'M':
        surname = part[2].split(',')[0].strip()
        surnames.add(surname)

for surname in sorted(surnames):
   print(surname)
