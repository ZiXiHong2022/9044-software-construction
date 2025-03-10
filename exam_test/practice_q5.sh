#!/bin/dash


years=$(grep -E "^$1\|" "$2" |cut -d'|' -f2|sort)


start=$(echo "$years" | head -n1)
end=$(echo "$years" | tail -n1)

for year in $(seq "$start" "$end"); do
    if ! echo "$years" | grep -q "$year"; then
        echo "$year"
    fi
done