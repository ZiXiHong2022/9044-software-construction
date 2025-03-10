#!/bin/dash
if [ $# -eq 0 ]; then
    echo "Usage: $0 <snapshot number>"
    exit 1
fi

n=$1


snapshot-save.sh


if [ -d ".snapshot.$n" ]; then
    echo "Restoring snapshot $n"
    for file in .snapshot.$n/*; do
        cp "$file" .
    done
else
    echo "Snapshot $n does not exist."
fi

