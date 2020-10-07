#!/usr/bin/env python3
import copy
from src.data_structure.array import *
from pytest import mark


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


TEST_FIBONACCI_SEQUENCE = [
	(0, 0),
	(1, 1),
	(2, 1),
	(3, 2),
	(4, 3),
	(5, 5),
	(6, 8),
	(7, 13)
]
@mark.parametrize("test_num, expected_response", copy.deepcopy(TEST_FIBONACCI_SEQUENCE))
def test_fibonacci_sequence(test_num, expected_response):
	response = fibonacci_sequence(test_num)

	assert response == expected_response


@mark.parametrize("test_num, expected_response", copy.deepcopy(TEST_FIBONACCI_SEQUENCE))
def test_fibonacci_sequence_inefficient(test_num, expected_response):
	response = fibonacci_sequence_inefficient(test_num)

	assert response == expected_response


TEST_FOUR_SUMS = [
	([], 0, []),
	([1, 2], 0, []),
	([1, 2, 3, 4], 0, []),
	([1, 2, 3, 4, 5], 0, []),
	([1, 2, 3, 4, 5, 6], 0, []),
	([1, 2, 3, 4, 5, 6, 7], 0, []),
	([1, 2, 3, 4], 10, [[1, 2, 3, 4]]),
	([3, 2, 1, 4], 10, [[1, 2, 3, 4]]),
	([1, 1, 2, 3, 4], 10, [[1, 2, 3, 4]]),
	([1, 1, 2, 2, 3, 3, 4, 4], 10, [[1, 1, 4, 4], [1, 2, 3, 4], [2, 2, 3, 3]]),
	([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
	([-3,-2,-1,0,0,1,2,3], 0, [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
	([-1,0,-5,-2,-2,-4,0,1,-2], -9, [[-5,-4,-1,1],[-5,-4,0,0],[-5,-2,-2,0],[-4,-2,-2,-1]])
]
@mark.parametrize("test_list, test_target, expected_response", copy.deepcopy(TEST_FOUR_SUMS))
def test_four_sums(test_list, test_target, expected_response):
	response = four_sums(test_list, test_target)

	assert response == expected_response


TEST_HIGHEST_POPULATION = [
	([], float("-inf")),
	([("p1", 1990, 2020)], 1990),
	([("p1", 1990, 1990), ("p2", 1990, 1990)], 1990),
	([("p1", 1990, 2020), ("p2", 1980, 2020)], 1990),
	([("p1", 1990, 2020), ("p2", 1980, 2020), ("p3", 1980, 1980)], 1990),
	([("p1", 1990, 2020), ("p2", 1980, 2020), ("p3", 1980, 1985), ("p4", 1980, 1983), ("p3", 1980, 1984)], 1980),
]
@mark.parametrize("test_population, expected_response", TEST_HIGHEST_POPULATION)
def test_highest_population(test_population, expected_response):
	response = highest_population(test_population)

	assert response == expected_response


TEST_PADOVAN_SEQUENCE = [
	(0, 1),
	(1, 1),
	(2, 1),
	(3, 2),
	(4, 2),
	(5, 3),
	(6, 4),
	(7, 5)
]
@mark.parametrize("test_num, expected_response", copy.deepcopy(TEST_PADOVAN_SEQUENCE))
def test_padovan_sequence(test_num, expected_response):
	response = padovan_sequence(test_num)

	assert response == expected_response


@mark.parametrize("test_num, expected_response", copy.deepcopy(TEST_PADOVAN_SEQUENCE))
def test_padovan_sequence_inefficient(test_num, expected_response):
	response = padovan_sequence_inefficient(test_num)

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


TEST_THREE_SUMS = [
	([], []),
	([1, 2], []),
	([1, 2, 3, 4], []),
	([0, 0, 0], [[0, 0, 0]]),
	([0, 0, 0, 1], [[0, 0, 0]]),
	([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]])
]
@mark.parametrize("test_list, expected_response", copy.deepcopy(TEST_THREE_SUMS))
def test_three_sums(test_list, expected_response):
	response = three_sums(test_list)

	assert response == expected_response


@mark.parametrize("test_list, expected_response", copy.deepcopy(TEST_THREE_SUMS))
def test_three_sums_inefficient(test_list, expected_response):
	response = three_sums_inefficient(test_list)

	assert response == expected_response


TEST_TWO_SUM = [
	([], 0, []),
	([1], 0, []),
	([1], 7, []),
	([10, -3], 7, [0, 1]),
	([0, 0], 0, [0, 1]),
	([0, 1, 0], 0, [0, 2]),
	([1, 1], 2, [0, 1]),
	([1, 1], 5, []),
	([1, 3, 2], 5, [1, 2]),
	([1, 3, 6, 8, 9, 1], 2, [0, 5])
]
@mark.parametrize("test_num, test_target, expected_response", TEST_TWO_SUM)
def test_two_sum(test_num, test_target, expected_response):
	response = two_sum(test_num, test_target)

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


