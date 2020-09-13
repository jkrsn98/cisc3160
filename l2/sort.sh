echo "CONTENTS OF CSV FILE:"
cat mycsv.csv
echo -e "\n\nNAME AND GPA SORTED BY GPA:"
cut -d ',' -f 1,4 mycsv.csv > mycolumns.csv
sort -k2 mycolumns.csv