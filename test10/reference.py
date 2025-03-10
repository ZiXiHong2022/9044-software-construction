#!/usr/bin/env python3

import sys
import re

input_lines = sys.stdin.read().strip().split('\n')
output_lines = []
for line in input_lines:
    if "#" in line:
        try:
                
                line_number = int(line[1:])
                
                output_lines.append(input_lines[line_number - 1])
        except ValueError:
                
                output_lines.append(line)
    else:
        output_lines.append(line)

for output_line in output_lines:
        print(output_line)