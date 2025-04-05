#!/bin/sh

RES_FILE="./result.csv"
TEMP="./temp.csv"

if [ -e $RES_FILE ]; then
  rm -rf $RES_FILE
fi

touch $RES_FILE
touch $TEMP

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $RES_FILE

for file in *.csv; do
    if [ "$file" != "temp.csv" ] && [ "$file" != "result.csv" ]; then
        tail -n +2 $file >> $TEMP
    fi
done

cat $TEMP | sort -t "," -k2 -k1 >> $RES_FILE
rm -rf $TEMP