#!/bin/dash


if [ $# -ne 2 ]; then
    echo "Usage: $0 <number of lines> <string>"
    exit 1
fi


if ! echo "$1" | grep -Eq '^[0-9]+$'; then
    echo "$0: argument 1 must be a non-negative integer"
    exit 1
fi


if echo "$1" | grep -Eq '^-[1-9][0-9]*$'; then
    echo "$0: argument 1 must not be a negative integer"
    exit 1
fi



n=$1
while [ $n -gt 0 ]; do
    echo "$2"
    n=$((n - 1))
done

