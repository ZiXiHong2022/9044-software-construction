#!/bin/dash



n=$1  
name=$2  


i=1
while [ $i -le $n ]; do
    echo "hello $name" > "hello$i.txt"
    i=$((i + 1)) 
done
