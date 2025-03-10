#!/bin/dash

grep -E 'COMP2041|COMP9044' | cut -d'|' -f3 | cut -d',' -f2 | cut -d' ' -f2 | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
