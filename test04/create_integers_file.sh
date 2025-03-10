#!/bin/dash

start=$1

End=$2

filename=$3


i=$start


while [ $i -le $End ]
do
   
   echo $i >> $filename
   

   i=$((i + 1))
done
