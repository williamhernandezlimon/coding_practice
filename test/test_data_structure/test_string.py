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
