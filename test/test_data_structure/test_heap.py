#!/usr/bin/env python3
from src.data_structure import heap
from pytest import mark


TEST_HEAP_MAX = [
	([], []),
	([0], [0]),
	([1], [1]),
	([1, 2], [2, 1]),
	([1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17], [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]),
	([10, 5, 7, 13, 1, 12, 4], [13, 10, 12, 5, 1, 7, 4])
]
@mark.parametrize("test_a, expected_response", TEST_HEAP_MAX)
def test_heap_max(test_a, expected_response):
	heap.heap_max(test_a)

	assert test_a == expected_response


TEST_HEAP_MIN = [
	([], []),
	([0], [0]),
	([1], [1]),
	([2, 1], [1, 2]),
	([17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1], [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]),
	([13, 10, 12, 5, 1, 7, 4], [1, 5, 4, 13, 10, 7, 12])
]
@mark.parametrize("test_a, expected_response", TEST_HEAP_MIN)
def test_heap_min(test_a, expected_response):
	heap.heap_min(test_a)

	assert test_a == expected_response