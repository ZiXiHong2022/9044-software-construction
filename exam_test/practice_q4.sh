#!/bin/dash

if [ $# -ne 1 ];then
    echo "Usage: $1 <filename>"
    exit 1

fi

filename=$1

min=$(sort -n $filename|head -n 1 )
max=$(sort -nr $filename|head -n 1 )

total_seq=$(seq "$min" "$max"|grep -Exvf "$filename") 

if [ -n $total_seq ];then
    echo "$total_seq"
fi







