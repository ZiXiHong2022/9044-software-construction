#!/usr/bin/env python3

import sys
import subprocess

if len(sys.argv[1:]) != 1:
    print(f"Usage: {sys.argv[0]} <COURSE_PREFIX>")
    sys.exit(1) 

search_name = sys.argv[1]
url = f"http://www.timetable.unsw.edu.au/2024/{search_name}KENS.html"

commands = f"""
curl --location --silent "{url}" | 
grep -E '<a href=".*[0-9]{{4}}\\.html">' |
sed -n 's/.*<a href.*>\\(.*\\)<\\/a>.*/\\1/ p' |
sed '$!N;s/\\n/ /' |
sort -t' ' -k1.5,1n |
uniq
"""

result = subprocess.run(commands, shell=True, text=True, capture_output=True)



print(result.stdout.strip())