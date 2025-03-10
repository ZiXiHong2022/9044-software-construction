#!/usr/bin/env python3

import sys

# Check if a command line argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <count>")
    sys.exit(1)

# Initialize the dictionary to store counts
count = {}

# Convert command line argument to an integer
total_count = int(sys.argv[1])

# Process each line from standard input
for line in sys.stdin:
    # Strip the newline character from the end of the line
    line = line.strip()
    
    # Update the count of the line
    if line in count:
        count[line] += 1
    else:
        count[line] = 1
    
    # Check if the count for the current line has reached the total_count
    if count[line] == total_count:
        print(f"Snap: {line}")
        break
