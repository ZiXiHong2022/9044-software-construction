#!/usr/bin/env python3
import sys
import re

for line in sys.argv[1:]:
	if re.findall("[AEIOUaeiou]{3}",line):
	    print(line,end=" ")



print()

