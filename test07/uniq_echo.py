#!/usr/bin/env python3

import sys

unique = set()
for arg in sys.argv[1:]:
	if arg not in unique:
		unique.add(arg)
		print(arg,end="")

print()
	