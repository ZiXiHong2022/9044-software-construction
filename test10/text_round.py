#!/usr/bin/env python3
import sys
import re


input_lines = sys.stdin.read().strip().split('\n')

number_pattern = re.compile(r'\d*\.\d+|\d+')


for line in input_lines:
    
    numbers = number_pattern.findall(line)
    
    for number in numbers:
        
        rounded_number = str(round(float(number)))
        
        line = line.replace(number, rounded_number, 1)

    print(line)
