#!/usr/bin/env python3
from src.data_structure import table as table_obj


def compress(s):
	"""
	Compress duplicate neighboring characters, by using integer
	to represent the number of occurances.
	Example:
		abbccc --> a2b2c3
	s:
		the string that will be compresed
	return:
		the compressed string

	complexity:
		time: O(n)
		space: O(n)
			using join() instead of += for str
			reduces the space complexity
	"""
	# check for unordinary null cases
	if not s: return ""

	compressed_string = []
	
	# i is the pointer to the last duplicate character
	i = 0; j = 0
	while j < len(s):
		# duplicate character
		if s[i] == s[j]:
			if i == j:
				compressed_string.append(s[j])
		# non-duplicate character
		else:
			if j - i > 1:
				compressed_string.append(str(j - i))
			compressed_string.append(s[j])
			i = j
		j += 1

	if j - i > 1:
		compressed_string.append(str(j - i))

	return "".join(compressed_string)


def get_bad_hosts(hostnames_range, hosts):
	"""
	Given a range of hostnames, email me a single list of hosts running the wrong number of instances of a process.
	Don't worry about authentication, assume ssh keys are in place for user 'root'.
 	Hostname range: web0001-1000.facebook.com
	Process name: "app"
	Number of running "app" instances when healthy: 4	
	hostnames_range:
		string containing the range of hosts
	hosts:
		map of hosts, used to check instances
	"""
	# TODO: store names in a class
	instance_name = "app"
	start = "0001"
	end = "1000"

	bad_hosts = []
	# loop through all hosts
	for i in range(int(start), int(end) + 1):
		# convert "i" integer, to string, with proper padding
		i_str = str(i).zfill(4)
		hostname = f"web{i_str}.facebook.com"

		# get number of running app
		app_instance_count = hosts.get(hostname, {}).get("instances", {}).get("app", 0)

		# append bad hosts
		if hostname in hosts and app_instance_count != 4:
			bad_hosts.append(hostname)


	return bad_hosts


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


def longest_common_prefix(strs):
	"""
	Get the longest common prefix, for a given list of strings
	strs:
		list of strings, to choose the common prefix from
	return:
		longest common prefix
	complexity:
		time: O(s)
		space: O(1)
	"""
	# Example zip:  
	# ["flower", "flow"] --> [('f', 'f'), ('l', 'l'), ('o', 'o'), ('w', 'w')]
	letter_groups = zip(*strs)
	longest_prefix = []
	for letter_group in letter_groups:
		if len(set(letter_group)) > 1: break
		longest_prefix.append(letter_group[0])

	return "".join(longest_prefix)


def longest_common_prefix_inefficient(strs):
	"""
	Get the longest common prefix, for a given list of strings
	strs:
		list of strings, to choose the common prefix from
	return:
		longest common prefix
	complexity:
		time: O(mxn)
			m: is the number of elements in the list
			n: the length of the strings
		space: O(mxn)
	"""
	if len(strs) < 1: return ""
	if len(strs) == 1: return strs[0]

	longest_prefix = strs[0]
	
	# loop list
	for i, curr_string in enumerate(strs[1:], 1):
		prev_string = strs[i-1]

		# loop previous and current string
		j = 0
		print(f"prev_string: {prev_string} len(prev_string): {len(prev_string)} curr_string: {curr_string} len(curr_string): {len(curr_string)} longest_prefix: {longest_prefix} len(longest_prefix): {len(longest_prefix)}")
		while prev_string and curr_string and longest_prefix and \
				j < len(prev_string) and j < len(curr_string) and j < len(longest_prefix) and \
				prev_string[j] == curr_string[j] == longest_prefix[j]:
			print(f"j: {j}")
			j += 1

		longest_prefix = longest_prefix[0:j]
		if longest_prefix == 0: return ""

	return longest_prefix


def longest_palindrome(s: str) -> str:
	"""
   	s:
   		string that will be used to find the longest palindrome
   	return:
   		the largest string palindrome, inside s
	"""
	if not s or len(s) < 1: return ""
	start = 0
	end = 0

	for i in range(len(s)):
		len_odd = _expand_from_middle(s, i, i)  # for odd strings: "aba"
		len_even = _expand_from_middle(s, i, i+1)  # for even strings: "abba"
		len_max = max(len_even, len_odd)
		
		if len_max > end - start:
			# save new max-substring end and start
			# please note: 'i' is considered the middle point
			start = i - int(((len_max - 1) / 2))
			end = i + int((len_max / 2))

	return s[start:end+1]


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


def reverse_words(s: str) -> str:
	"""
	Given a string of words. Reverse the words delimited by space
	s:
		string of words delimited by space
	return:
		s string in reverse order
	complexity:
		time: O(n)
		space: O(n)
	"""
	return " ".join(s.split()[::-1])
	

def roman_to_integer(roman_number: str) -> int:
	"""
	Convert string roman numbers to integer value
	roman_number:
		string that represents the roman number
		please note: assumming valid roman_number
	return:
		integer value of the roman_number
	"""
	roman_map = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	}
	reverse = roman_number[::-1]
	total = roman_map[reverse[0]] if reverse else None
	# traverse reverse string starting from 1
	for i, char in enumerate(reverse[1:], 1):
		previous_number = roman_map[reverse[i-1]]
		current_number = roman_map[reverse[i]]
		if current_number >= previous_number:
			total += current_number
		else:
			total -= current_number

	return total


def to_goat_latin(s: str) -> str:
	"""
	A sentence S is given, composed of words separated by spaces. 
	Each word consists of lowercase and uppercase letters only.

	We would like to convert the sentence to "Goat Latin" 
	(a made-up language similar to Pig Latin.)

	The rules of Goat Latin are as follows:
	1.
	If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
	For example, the word 'apple' becomes 'applema'.
	 
	2.
	If a word begins with a consonant (i.e. not a vowel), 
	remove the first letter and append it to the end, then add "ma".
	For example, the word "goat" becomes "oatgma".
	 
	3.
	Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
	For example, the first word gets "a" added to the end, 
	the second word gets "aa" added to the end and so on.
	
	Return:
	The final sentence representing the conversion from S to Goat Latin. 

	
	Input: "I speak Goat Latin"
	Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"

	complexity:
		time: O(n)
		space: O(n)
	"""
	# if not s: return ""
	words = s.split()
	vowels = {"a", "e", "i", "o", "u"}
	goat_latin = []

	# loop through words
	for i, word in enumerate(words, 1):
		new_word = ""

		if word[0].lower() in vowels:
			new_word = word + "ma"
		else:
			new_word = word[1:] + word[0] + "ma"

		# append "a"
		goat_latin.append(new_word + ("a" * i))
	
	return " ".join(goat_latin)


# PRIVATE METHODS BELOW:
def _expand_from_middle(s: str, left: int, right: int) -> int:
	"""
	Given a string, traverse left and right, respectively
	as long as within bounds and s[left] == s[right]
	Used in method longest_palindrome(s)
	s:
		string that will be traversed
	left:
		integer for left start point before decrementing to the left
	right:
		integer for right start point before incrementing to the right
	return:
		the length between right and left
	"""
	if not s or left > right: return 0

	while left >= 0 and right < len(s) and s[left] == s[right]:
		left -= 1
		right += 1

	return right - left - 1
