#!/usr/bin/env python3
from src.data_structure import table as table_obj


def get_larger(s1, s2):
	"""
	Return the larger string delimeted by '-'
	s1:
		string 1 delimited by dash
	s2:
		string 2 delimited by dash
	return:
		return the largest string per ASCII value
	"""
	l1 = s1.split('-')
	l2 = s2.split('-')

	i = 0
	j = 0
	while i < len(l1) and j < len(l2):
		word1 = int(l1[i]) if l1[i].isnumeric() else l1[i]
		word2 = int(l2[j]) if l2[j].isnumeric() else l2[j]
		if  word1 > word2:
			return s1
		if word1 < word2:
			return s2
		i += 1
		j += 1

	return s1 if len(l1) > len(l2) else s2


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


def reverse_integer(number: int) -> int:
	"""
	Given an unsigned integer, reverse the number.
	Return 0 if outside of signed integer range: [−2^31,  2^31 − 1]
	"""
	is_positive = True if number > 0 else False
	number = number if is_positive else number * -1
	reverse = 0
	pointer = number
	while pointer > 0:
		reverse = (reverse * 10) + (pointer % 10)
		pointer = int(pointer / 10)

	# check overflow
	if (reverse < -2**31) or (reverse > (2**31)-1):
		return 0

	return reverse if is_positive else reverse * -1


def is_palindrome_integer(num: int) -> bool:
	"""
	Checks to see if the integer is a valid palindrome
	num:
		signed integer
	return:
		'num' is a valid palindrome
	"""
	if num < 0:
		return False
	num_str = str(num)

	return num_str == num_str[::-1]


def is_valid_parenthesis(string: str) -> bool:
	"""
	Return if parenthesis is valid.
	Example 1:
		Input: "()"
		Output: true
	Example 2:
		Input: "()[]{}"
		Output: true
	Example 3:
		Input: "(]"
		Output: false
	Example 4:
		Input: "([)]"
		Output: false
	Example 5:
		Input: "{[]}"
		Output: true	

	Time Complexity:
		O(n)
	Space Complexity:
		O(n)
	"""
	stack = []
	for c in string:
		# left parenthesis
		if c == '(' or c == '[' or c == '{':
			stack.append(c)
			continue
		
		# right parenthesis
		top = stack.pop() if stack else None
		if top == '(' and c == ')':
			continue
		elif top =='[' and c == ']':
			continue
		elif top =='{' and c == '}':
			continue
		else:
			return False
	return len(stack) == 0


def length_of_longest_substring(string: str) -> int:
	# string:
	# 	contains the string we check for longest substring
	# return:
	#	the longest substring 
	front_ptr = 0
	back_ptr = 0
	max_length = 0 
	char_map = {}

	while back_ptr < len(string):
		char = string[back_ptr]
		if char not in char_map:
			# add new char and increase window size
			char_map[char] = 1
			back_ptr += 1
		else:
			# remove front element and reduce window size
			del char_map[string[front_ptr]]
			front_ptr += 1

		max_length = max(max_length, back_ptr - front_ptr)

	return max_length

