#!/usr/bin/env python3
from src.data_structure.string import *
from pytest import mark

TEST_GET_LARGER = [
	("", "", ""),
	("", "-", "-"),
	("", "a", "a"),
	('aa', 'a', 'aa'),
	('---', '--', '---'),
	('hello-12', 'hello-1', 'hello-12'),
	('hello-world', 'hello-earth', 'hello-world')
]
@mark.parametrize("test_s1, test_s2, expected_response", TEST_GET_LARGER)
def test_get_larger(test_s1, test_s2, expected_response):
	response = get_larger(test_s1, test_s2)

	assert response == expected_response


TEST_LONGEST_PALINDROME = [
	("", ""),
	("a", "a"),
	("aba", "aba"),
	("abba", "abba"),
	("cbbd", "bb"),
	("abcdefg", "g")
]
@mark.parametrize("test_s, expected_response", TEST_LONGEST_PALINDROME)
def test_longest_palindrome(test_s, expected_response):
	response = longest_palindrome(test_s)

	assert response == expected_response


TEST_MAX_VOWELS = [
	("abciiidef", 3, 3),
	("aeiou", 2, 2),
	("leetcode", 3, 2),
	("rhythms", 4, 0),
	("tryhard", 4, 1),
	("", 4, 0),
	("aeiou", 0, 0),
	("wzx", 7, 0)
]
@mark.parametrize("test_str, test_substr_len, expected_response", TEST_MAX_VOWELS)
def test_max_vowels(test_str, test_substr_len, expected_response):
	response = max_vowels(test_str, test_substr_len)

	assert response == expected_response


TEST_REVERSE_INTEGER = [
	(123, 321),
	(-123, -321),
	(1534236469, 0),
	(1, 1),
	(0, 0)
]
@mark.parametrize("test_number, expected_response", TEST_REVERSE_INTEGER)
def test_reverse_integer(test_number, expected_response):
	response = reverse_integer(test_number)

	assert response == expected_response

TEST_ROMAN_TO_INTEGER = [
	("I", 1),
	("V", 5),
	("X", 10),
	("L", 50),
	("C", 100),
	("D", 500),
	("M", 1000),
	("III", 3),
	("IV", 4),
	("III", 3),
	("IV", 4),
	("LVIII", 58),
	("MCMXCIV", 1994)
]
@mark.parametrize("test_roman_number, expected_response", TEST_ROMAN_TO_INTEGER)
def test_roman_to_integer(test_roman_number, expected_response):
	response = roman_to_integer(test_roman_number)

	assert response == expected_response



TEST_IS_PALINDROME_INTEGER = [
	(-1, False),
	(-11, False),
	(1211, False),
	(948, False),
	(0, True),
	(1, True),
	(11, True),
	(121, True),
	(1221, True)
]
@mark.parametrize("test_number, expected_response", TEST_IS_PALINDROME_INTEGER)
def test_is_palindrom_integer(test_number, expected_response):
	response = is_palindrome_integer(test_number)

	assert response == expected_response


TEST_IS_VALID_PARENTHESIS = [
	("", True),
	("()", True),
	("()[]{}", True),
	("([{}])", True),
	("(]", False),
	("([)]", False),
	("()]", False),
	("]]", False),
	("((", False)
]
@mark.parametrize("test_string, expected_response", TEST_IS_VALID_PARENTHESIS)
def test_is_valid_paranthesis(test_string, expected_response):
	response = is_valid_parenthesis(test_string)

	assert response == expected_response


TEST_LENGTH_OF_LONGEST_SUBSTRING = [
	("", 0),
	("abcabcbb", 3),
	("abc", 3),
	("a", 1),
	("aaaaa", 1)
]
@mark.parametrize("test_input, expected_response", TEST_LENGTH_OF_LONGEST_SUBSTRING)
def test_length_of_longest_substring(test_input, expected_response):
	response = length_of_longest_substring(test_input)

	assert response == expected_response




