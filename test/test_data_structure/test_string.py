#!/usr/bin/env python3
from src.data_structure.string import *
from pytest import mark


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