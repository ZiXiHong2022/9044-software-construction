#!/bin/dash

# 遍历所有传入的文件名参数
for src_file in "$@"; do

    grep -oh '#include "[^"]*"' "$src_file" | while IFS= read -r line; do

        include_file=$(echo "$line" | sed 's/#include "//;s/"$//')

        if [ ! -f "$include_file" ]; then
      
            echo "$include_file included into $src_file does not exist"
        fi
    done
done
