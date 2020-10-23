# invocation: awk -f reverse_file.awk file.txt

{
	array[NR] = $0
}
END {
	for(i=NR; 0 < i; i--){
		print array[i]
	}
}


# get the word count for every word in a file
# BEGIN { FS="[^a-zA-Z]+" } {
#         for (i=1; i<=NF; i++) {
#             word = tolower($i)
#             words[word]++
#         }
#     }
#     END {
#         for (w in words)
#              printf("%d %s\n", words[w], w)
#     } ' test_words.txt