#!/bin/dash



if [ $# -ne 2 ]; then
    echo "Usage: $0 <directory1> <directory2>"
    exit 1
fi

dir1=$1
dir2=$2


for file in "$dir1"/*; do
    filename=$(basename "$file")
   
    if [ -f "$dir2/$filename" ]; then
  
        if diff -q "$file" "$dir2/$filename" > /dev/null; then
            echo "$filename"
        fi
    fi
done | sort  


