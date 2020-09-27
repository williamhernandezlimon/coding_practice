#!/usr/bin/env bash

PROJECT_ROOT="../../"

test_count=0

### awk ###
# print the 3rd column of a table
echo "test: $((test_count++))"
awk '//{print $8}' ${PROJECT_ROOT}test/test_unix/test_data/test_table.txt | sed '/^$/d'
# print the count of every word using awk
echo -e "\n\ntest: $((test_count++))"
awk 'BEGIN{RS=" \n"} {a[$1]++} END{for(k in a)print k,a[k]}' ../../test/test_unix/test_data/test_words.txt


### find ###
#	{} symbol is what would be the file in question
#	\; is to syntax termination for -exec
# find all *.pyc files in the current directory and remove them
find . -name '*.pyc' -exec rm -rf {} \;


### gsed ###
# prints the count of every word occurence
echo -e "\ntest: $((test_count++))"
gsed -e 's/^\s*//' -e 's/\s*$//' ${PROJECT_ROOT}test/test_unix/test_data/test_words.txt | tr -s ' ' | tr ' ' '\n' | sort | uniq -c | awk '{print $2" "$1}'
# remove all leading white space
echo -e "\ntest: $((test_count++))"
gsed -e 's/^[ \t]*//' ../../test/test_unix/test_data/test_words.txt
# prints the 10th line number
# 	q: quits sed at 10 
# 	d: deleted everything else
echo -e "\ntest: $((test_count++))"
sed '10q;d' bash.sh


### tail ###
# prints file in reverse
echo -e "\ntest: $((test_count++))"
tail -r ${PROJECT_ROOT}test/test_unix/test_data/test_words.txt

