#!/bin/dash


if [ "$#" -ne 2 ]; then
    echo "Usage: ./scraping_courses.sh <year> <course-prefix>"
    exit 1
fi


YEAR=$1
if [ "$YEAR" -lt 2019 ] || [ "$YEAR" -gt 2023 ]; then
    echo "./scraping_courses.sh: argument 1 must be an integer between 2019 and 2023"
    exit 1
fi

PREFIX=$2
UNDERGRAD_URL="https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:${YEAR}%20+unsw_psubject.studyLevel:undergraduate%20+unsw_psubject.educationalArea:${PREFIX}*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:ugrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0"
POSTGRAD_URL="https://www.handbook.unsw.edu.au/api/content/render/false/query/+unsw_psubject.implementationYear:${YEAR}%20+unsw_psubject.studyLevel:postgraduate%20+unsw_psubject.educationalArea:${PREFIX}*%20+unsw_psubject.active:1%20+unsw_psubject.studyLevelValue:pgrd%20+deleted:false%20+working:true%20+live:true/orderby/unsw_psubject.code%20asc/limit/10000/offset/0"


curl -sL "$UNDERGRAD_URL" > undergrad_courses.json
curl -sL "$POSTGRAD_URL" > postgrad_courses.json


grep -o '"code":"[^"]*' undergrad_courses.json | sed 's/"code":"//' > courses.txt
grep -o '"title":"[^"]*' undergrad_courses.json | sed 's/"title":"//' >> courses.txt
grep -o '"code":"[^"]*' postgrad_courses.json | sed 's/"code":"//' >> courses.txt
grep -o '"title":"[^"]*' postgrad_courses.json | sed 's/"title":"//' >> courses.txt

sort courses.txt | uniq | tr '\n' ' ' 

rm undergrad_courses.json postgrad_courses.json courses.txt
