#!/usr/bin/env python3

import sys
import re

def sum_numbers_in_file(file_name):
    total_sum = 0

    with open(file_name, 'r') as file:
        for line in file:
            # 使用正则表达式找到所有数字（包括可能的负号、小数点和冒号）
            numbers = re.findall(r'[+-]?\d+(?:\.\d+)?', line)
            # 对每个找到的数字进行求和
            for number in numbers:
                total_sum += int(number)

    return total_sum

def main():
    if len(sys.argv) != 2:
        print("Usage: ./summing_numbers.py <file>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    total_sum = sum_numbers_in_file(file_name)
    print(total_sum)

if __name__ == "__main__":
    main()
