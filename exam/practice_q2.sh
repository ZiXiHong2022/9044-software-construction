#!/bin/dash

grep -E '.*\|[0-9]{4}(\s{2}|\/[0-9]?)\|M'| cut -d '|' -f3 | cut -d ',' -f1 |sort|uniq 