#!/bin/dash

max_lines=0
max_file=""
for files in $@;do 
    lines=$(wc -l < "$files")

    if [ $lines -gt $max_lines ];then
        max_lines=$lines
        max_file=$files
    fi

done

echo $max_file