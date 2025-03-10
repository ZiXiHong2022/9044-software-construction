#!/bin/dash

small=""
medium=""
large=""

for file in *; do
    if [ -f "$file" ]; then 
        lines=$(wc -l < "$file" | tr -d ' ')  

        if [ "$lines" -lt 10 ]; then
            small="$small $file"
        elif [ "$lines" -lt 100 ]; then
            medium="$medium $file"
        else
            large="$large $file"
        fi
    fi
done

echo "Small files:$small"
echo "Medium-sized files:$medium"
echo "Large files:$large"

