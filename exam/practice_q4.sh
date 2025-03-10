#!/bin/dash
if [ $# -ne 1 ];then

echo "Usage : $0 <filename>"

fi

max_number=$(sort -nr "$1"|head -n 1)
min_number=$(sort -n "$1" | head -n 1)


missing_number=$(seq "$min_number" "$max_number"|grep -Exvf  "$1")

if [ -n "$missing_number" ]; then
    echo "$missing_number"
fi