#!/usr/bin/env python3
from src.data_structure.array import *
from pytest import mark




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

