#!/bin/sh

SRC_FILE="../ex01/hh.csv"
RES_FILE="hh_sorted.csv"

cat $SRC_FILE | head -n 1 $SRC_FILE > $RES_FILE
cat $SRC_FILE | tail -n 20 | sort -t "," -k2 -k1 >> $RES_FILE