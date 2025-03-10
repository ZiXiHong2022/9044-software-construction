#!/bin/dash

for i in "$@"; do 
    if [ -e "$i" ]; then 

        modTime=$(stat -c %Y "$i")

        formattedTime=$(date -d "@$modTime" +"%b %d %H:%M")
        convert "$i" -gravity south -pointsize 36 -annotate +0+10 "$formattedTime" "${i%.jpg}_dated.jpg"
    else
        echo "File $i not found"
    fi
done

