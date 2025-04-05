#!/bin/sh

VACANCY="$1"

if [ $# -eq 1 ];
 then
 curl -H 'User-Agent: api-test-agent' "https://api.hh.ru/vacancies?text=$VACANCY&page=0&per_page=20" | jq > hh.json
 fi
