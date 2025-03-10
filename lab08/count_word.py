#!/usr/bin/env python3

import re
import sys


word = sys.argv[1]
count_number = 0
if len(sys.argv) != 2:
    print(f"usage:{sys.argv[0]} <words>")
    sys.exit(1)



for line in sys.stdin:
    search_words = re.findall(rf'\b{word}\b', line,re.IGNORECASE) 
    count_number += len(search_words)

print(f"{word} occurred {count_number} times")






