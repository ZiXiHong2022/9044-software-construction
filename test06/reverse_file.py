#!/usr/bin/env python3

import sys
list_1 = []
with open(sys.argv[1],"r") as file_1:
	lines = file_1.readlines()
	for i in lines:
		list_1.append(i.strip())
with open(sys.argv[2],"w") as file_2:
	for line in reversed(list_1):
	    print(line,file=file_2)
