#!/usr/bin/env python3


import sys

with open(sys.argv[1],"r") as file:
    files = list(file.readlines())
    files.sort(key=lambda x: (len(x), x))
    for i in files:
	    print(i,end="")