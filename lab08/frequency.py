#!/usr/bin/env python3

import sys
import re
import glob

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <word>")
    sys.exit(1)

word_to_search = sys.argv[1].lower()  
files = glob.glob("lyrics/*.txt")
sorted_files = sorted(files)
for file_path in sorted_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        lyrics = file.read().lower()  

       
        total_words = len(re.findall(r'[a-zA-Z]+', lyrics))

        word_count = len(re.findall(rf'\b{word_to_search}\b', lyrics))

        parts = file_path.split('/')[-1].split('.')[0].split('_')
        
        artist = ' '.join(parts[:])

        frequency = word_count / total_words

      
        print(f"{word_count:4}/{total_words:6} = {frequency:.9f} {artist}")

