#!/usr/bin/env python3

import sys

orca_total = 0

files = sys.argv[1:]

for file_name in files:
    with open(file_name, 'r') as file:
        for line in file:
            fields = line.strip().split()
           
            if len(fields) >= 3 and fields[2] == "Orca":
                try:
                    orca_total += int(fields[1])
                except ValueError:
                    pass

print(f"{orca_total} Orcas reported")

