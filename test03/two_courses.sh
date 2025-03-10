#!/bin/dash


cut -d '|' -f 2 | sort | uniq -c | grep '^ *2 ' | awk '{print $NF}'

