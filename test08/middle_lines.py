#!/usr/bin/env python3

import sys


for file in sys.argv[1:]:
    with open(file, "r") as f:
        lines = f.readlines()  

    line_count = len(lines)  

    if line_count == 0:
        continue

   
    if line_count % 2 == 0:
        middle_index = line_count // 2
        print(lines[middle_index - 1], end='')  
        print(lines[middle_index], end='')  

    else:
        middle_index = line_count // 2
        print(lines[middle_index], end='')  


