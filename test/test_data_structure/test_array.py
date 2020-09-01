#!/usr/bin/env python3
from src.data_structure.array import *
from pytest import mark


TEST_THREE_SUMS = [
	([], []),
	([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]])
]
@mark.parametrize("test_list, expected_response", TEST_THREE_SUMS)
def test_three_sums_inefficient(test_list, expected_response):
	response = three_sums_inefficient(test_list)

	assert response == expected_response


TEST_REMOVE_DUPLICATES = [
	([], 0),
	([1], 1),
	([1,1,1,1,1], 1),
	([1,1,2,2,3,3,4,4,5,5,6,6,7,7], 7)
]
@mark.parametrize("test_array, expected_response", TEST_REMOVE_DUPLICATES)
def test_remove_duplicates(test_array, expected_response):
	response = remove_duplicates(test_array)
	
	assert response == expected_response


TEST_CONTAINS_DUPLICATES = [
	([], False),
	([1], False),
	([1,1], True),
	([1,2,3,4,5,6,7,1], True),
	([1,2,3,4,5,6,7], False)
]
@mark.parametrize("test_array, expected_response", TEST_CONTAINS_DUPLICATES)
def test_contains_duplicates(test_array, expected_response):
	response = contains_duplicates(test_array)

	assert response == expected_response

# TODO: fix test case
# TEST_IS_PREFIX_OF_WORD = [
# 	("i love eating burger", "burg", 4),
# 	("this problem is an easy problem", "pro", 2),
# 	("i am tired", "you", -1),
# 	("i use triple pillow", "pill", 4),
# 	("hello from the other side", "they", -1),
# 	("love errichto jonathan dumb", "dumb", 4)
# ]
# @mark.parametrize("test_sentance, test_search_word, expected_response", TEST_IS_PREFIX_OF_WORD)
# def test_is_prefix_of_word(test_sentance, test_search_word, expected_response):
# 	response = is_prefix_of_word(test_sentance, test_search_word)

# 	assert response == expected_response


