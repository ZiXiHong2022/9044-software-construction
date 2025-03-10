#!/usr/bin/env python3

import sys
import re

match_number = 0
textbook_search = sys.stdin

for line in sys.stdin:
    m = re.findall(r'[a-zA-Z]+', line)
    match_number += len(m)


print(f"{match_number} words")






