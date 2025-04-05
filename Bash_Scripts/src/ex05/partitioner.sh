#!/bin/sh

SRC_FILE="../ex03/hh_positions.csv"

#очистка файлов перед работой
tail +2 $SRC_FILE | while read -r line
do
  line=${line:1:$((${#line}-2))}
  IFS='"' read -r id c1 created_at c2 name has_test alternate_url <<< "$line"
  has_test=${has_test:1:$((${#has_test}-2))}

  file_name="${created_at:0:10}.csv"

  if [ -e $file_name ]
  then
    rm -rf $file_name
  fi
done


tail +2 $SRC_FILE | while read -r line
do
  line=${line:1:$((${#line}-2))}
  IFS='"' read -r id c1 created_at c2 name has_test alternate_url <<< "$line"
  has_test=${has_test:1:$((${#has_test}-2))}

  file_name="${created_at:0:10}.csv"

  if [ -e $file_name ]
  then
    echo "\"$line\"" >> $file_name
  else
    touch $file_name
    echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $file_name
    echo "\"$line\"" >> $file_name
  fi
done

