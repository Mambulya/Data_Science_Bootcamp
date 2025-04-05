#!/bin/sh

SRC_FILE="../ex03/hh_positions.csv"
RES_FILE="hh_uniq_positions.csv"

echo "\"name\",\"count\"" > $RES_FILE

count_j=$(grep -i "Junior" $SRC_FILE | wc -l)
count_m=$(grep -i "Middle" $SRC_FILE | wc -l)
count_s=$(grep -i "Senior" $SRC_FILE | wc -l)

echo "\"Junior\","$count_j >> temp.csv
echo "\"Middle\","$count_m >> temp.csv
echo "\"Senior\","$count_s >> temp.csv

cat temp.csv | sort -r -k2 >> $RES_FILE
rm -rf temp.csv