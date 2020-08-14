# invocation: awk -f reverse_file.awk file.txt

{
	array[NR] = $0
}
END {
	for(i=NR; 0 < i; i--){
		print array[i]
	}
}