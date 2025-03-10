#!/bin/dash

if [ $# -ne 2 ];then
    echo " Usage : $0 <regex><file_name>" 1>&2
    exit 1
fi

file_name="$2"


years_regex=$(grep -E "^$1\|" "$file_name" |sort -t"|" -k2 |cut -d'|' -f2)



max_year=$(echo "$years_regex"|head -n 1)
min_year=$(echo "$years_regex" | head -n 1)

all_range=$(seq "$min_year" "$max_year")

not_given=$("$all_range"| grep -Fxvf "$years_regex")

echo "$not_given"

