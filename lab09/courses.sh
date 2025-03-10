#!/bin/dash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <COURSE_PREFIX>"
    exit 1
fi


URL="http://www.timetable.unsw.edu.au/2024/${1}KENS.html"


curl --location --silent "$URL" |
grep -E '<a href=".*[0-9]{4}\.html">' | 
sed -n 's/.*<a href.*>\(.*\)<\/a>.*/\1/ p '| 
sed '$!N;s/\n/ /'|
sort -t' ' -k1.5,1n|
uniq 

exit 0







