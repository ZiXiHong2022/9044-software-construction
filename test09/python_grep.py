#!/usr/bin/env python3

#!/usr/bin/env python3

import sys
import re

  
regex_pattern = sys.argv[1]
file_path = sys.argv[2]

pattern = re.compile(regex_pattern)

with open(file_path, 'r') as file:
    for line in file:
        if pattern.search(line):
            print(line.strip())


