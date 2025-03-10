#!/bin/dash


for file in *.htm; do
    
    if [ ! -e "$file" ]; then
        continue
    fi

    create_name="${file%.htm}.html"


    if [ -e "$create_name" ]; then
        echo "$create_name exists"
        exit 1
    fi


    mv "$file" "$create_name"
done
