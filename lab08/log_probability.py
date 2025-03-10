#!/usr/bin/env python3

import sys
import re
import glob
import math  

if len(sys.argv[1:]) < 1:
    print(f"Usage: {sys.argv[0]} <words....>")
    sys.exit(1)

files = glob.glob("lyrics/*.txt")
sorted_files = sorted(files)


for file_path in sorted_files:
    with open(file_path, 'r', encoding='utf-8') as file:
        lyrics = file.read().lower()

  
        total_words = len(re.findall(r'[a-zA-Z]+', lyrics)) 

        log_prob = 0

        for word in sys.argv[1:]:
            word_count = len(re.findall(rf'\b{word}\b', lyrics)) + 1  
            word_prob = word_count / total_words  
            log_prob += math.log(word_prob) 

        
        parts = file_path.split('/')[-1].split('.')[0].split('_')
        artist = ' '.join(parts)

        
        print(f"{log_prob:10.5f} {artist}")

