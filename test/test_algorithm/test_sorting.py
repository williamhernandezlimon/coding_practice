from src.algorithm import sorting
from pytest import mark


TEST_QUICKSORT = [
	([], 0, 0, []),
	([], 1, 2, []),
	([1, 2, 3], 0, 2, [1, 2, 3]),
	([2, 1, 3], 2, 0, [2, 1, 3]),
	([3, 4, 5, 7, 9, 8], 0, 5, [3, 4, 5, 7, 8, 9])
]

@mark.parametrize("test_list, test_low, test_high, expected_response", TEST_QUICKSORT)
def test_quicksort(test_list, test_low, test_high, expected_response):
	sorting.quicksort(test_list, test_low, test_high)

	assert test_list == expected_response


TEST_MERGESORT = [
	([], []),
	([1], [1]),
	([1, 1, 1], [1, 1, 1]),
	([2, 1, 3], [1, 2, 3]),
	([2, 2, 1, 3], [1, 2, 2, 3]),
	([2, 2, 1, 1, 3, 3], [1, 1, 2, 2, 3, 3]),
	([2, 1, 4, 3], [1, 2, 3, 4])
]
@mark.parametrize("test_list, expected_response", TEST_MERGESORT)
def test_mergesort(test_list, expected_response):
	sorting.mergesort(test_list)

	assert test_list == expected_response