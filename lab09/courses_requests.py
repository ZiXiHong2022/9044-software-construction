#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup
import re


if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <COURSE_PREFIX>")
    sys.exit(1)

search_name = sys.argv[1]
url = f"http://www.timetable.unsw.edu.au/2024/{search_name}KENS.html"

try:
    response = requests.get(url)
    response.raise_for_status()  
except requests.RequestException as e:
    print(f"Failed to retrieve web page: {e}")
    sys.exit(1)

soup = BeautifulSoup(response.text, 'html5lib')
href_regex = re.compile(r".*[0-9]{4}\.html$")
links = soup.find_all('a', href=href_regex)

count = 0
line = ""
for link in links:
    count += 1
    line += link.get_text().strip() + " "
    if count % 2 == 0:
        print(line.strip())
        line = ""
if line:
    print(line.strip())  



