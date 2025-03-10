#!/bin/dash



for jpg_file in *.jpg; do
    
    [ -e "$jpg_file" ] || continue
    

    png_file=$(echo "$jpg_file" | sed 's/\.jpg$/.png/')
    

    if [ -f "$png_file" ]; then
        echo "$png_file already exists"
        exit 1
    fi


    if convert "$jpg_file" "$png_file"; then
        rm "$jpg_file"
    else
        echo "Error converting $jpg_file to $png_file"
        exit 1
    fi
done


