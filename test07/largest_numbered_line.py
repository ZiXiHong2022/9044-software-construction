#!/usr/bin/env python3

# print line of a file containing largest number
# written by d.brotherston@unsw.edu.au for COMP(2041|9044)

import sys
import re

lines = sys.stdin.readlines()
numbers = []
for line in lines:
    numbers.append(list(map(float, re.findall(r'[+-]?(?:[0-9]+\.?[0-9]*|\.[0-9]+)', line))))

M = []
for line in numbers:
    try:
        M.append(max(line))
    except ValueError:
        pass

try:
    M = max(M)
    for index, line in enumerate(numbers):
        if M in line:
            print(lines[index], end='')
except ValueError:
    pass
