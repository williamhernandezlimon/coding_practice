#!/usr/bin/env python3

def max_vowels(string, substring_length):
	"""
	string: contains a sequence of chartacter, used to search for vowels
	substring_length: max window of consecutive chars we can search vowels for

	Solution: 
	This is a window problem,
	We move the window along the string until we reach the end
	"""
	if substring_length == 0: return 0
	vowel_count = 0
	vowel_count_max = 0

	for i, letter in enumerate(string):
		if letter in 'aeiou':
			vowel_count += 1
		if i >= substring_length and string[i - substring_length] in 'aeiou':
			vowel_count -= 1
		vowel_count_max = max(vowel_count_max, vowel_count)
	
	return vowel_count_max

