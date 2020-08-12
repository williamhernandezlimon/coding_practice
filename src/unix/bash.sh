#!/usr/bin/env bash

PROJECT_ROOT="../../"

test_count=0

# print the 3rd column of a table
# test input:
#	/test/test_unix/test_data/test_table.txt
# test output:
#	country
# 	usa
# 	mx
# 	china
# 	eu
echo "test: $((test_count++))"
awk '//{print $8}' ${PROJECT_ROOT}test/test_unix/test_data/test_table.txt | sed '/^$/d'

# prints the count of every word occurence
echo -e "\ntest: $((test_count++))"
gsed -e 's/^\s*//' -e 's/\s*$//' ${PROJECT_ROOT}test/test_unix/test_data/test_words.txt | tr -s ' ' | tr ' ' '\n' | sort | uniq -c | awk '{print $2" "$1}'

# prints file in reverse
echo -e "\ntest: $((test_count++))"
tail -r ${PROJECT_ROOT}test/test_unix/test_data/test_words.txt
