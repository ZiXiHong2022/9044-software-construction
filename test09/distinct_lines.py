#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python distinct_lines.py <N>")
        return

    N = int(sys.argv[1])
    unique_lines = set()
    total_lines_read = 0

    while len(unique_lines) < N:
        try:
            line = input()
        except EOFError:
            print(f"End of input reached after {total_lines_read} lines read - {N} different lines not seen.")
            return
        
        normalized_line = ' '.join(line.strip().lower().split())
        unique_lines.add(normalized_line)
        total_lines_read += 1

    print(f"{N} distinct lines seen after {total_lines_read} lines read.")

if __name__ == "__main__":
    main()
