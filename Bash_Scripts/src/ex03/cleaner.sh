#!/bin/sh

SRC_FILE="../ex02/hh_sorted.csv"
RES_FILE="hh_positions.csv"

head -n 1 $SRC_FILE > $RES_FILE
tail +2 $SRC_FILE | while read -r line
do
  line=${line:1:$((${#line}-2))}
  IFS='"' read -r id c1 created_at c2 name has_test alternate_url <<< "$line"
  has_test=${has_test:1:$((${#has_test}-2))}
  level=""
  if echo "$name" | grep -q "Junior"; then
        level="Junior"
        fi
  if echo "$name" | grep -q "Middle"; then
    if [ -z "$level" ]; then
        level="Middle"
        else
        level="$level/Middle"
        fi
    fi
  if echo "$name" | grep -q "Senior"; then
        if [ -z "$level" ]; then
          level="Senior"
        else
           level="$level/Senior"
        fi
    fi
    if [ "$level" = "" ]; then
        level="-"
    fi
  echo "\"$id\",\"$created_at\",\"$level\",$has_test,\"$alternate_url\"" >> $RES_FILE
done