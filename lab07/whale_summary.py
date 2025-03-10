#!/usr/bin/env python3

import sys

def to_singular(word):
    if word.endswith('s'):
        return word[:-1]
    else:
        return word

def print_summary(species_count):
    for species in sorted(species_count):
        pods, whales = species_count[species]
        print(f"{species} observations: {pods} pods, {whales} individuals")

def main():
    if len(sys.argv) < 2:
        print("Usage: ./whale_summary.py <file1> [<file2> ...]")
        sys.exit(1)
    
    species_count = {}

    for file_name in sys.argv[1:]:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split()

                species_name = " ".join(parts[2:]).lower()
                species_name = to_singular(species_name)
                try:
                    pods = int(parts[1])
                except ValueError:
                    print(f"Ignore line: {line.strip()}")
                    continue

                species_count[species_name] = species_count.get(species_name, [0, 0])
                species_count[species_name][0] += 1  # Counting the number of occurrences of the species
                species_count[species_name][1] += pods  # Accumulating the total number of pods

    print_summary(species_count)

if __name__ == "__main__":
    main()
