#!/usr/bin/env python3


import sys

indexs = int(sys.argv[1])
list_1 =[]
filename = sys.argv[2]
with open(filename, "r") as file:
    for index in file:
        list_1.append(index.strip())

if indexs > len(list_1):
    pass
else:
    print(list_1[indexs-1])	