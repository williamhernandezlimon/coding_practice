import copy
from pytest import mark
from src.algorithm import sorting



TEST_QUICK_SORT = [
	([], 0, 0, []),
	([], 1, 2, []),
	([1, 2, 3], 0, 2, [1, 2, 3]),
	([2, 1, 3], 2, 0, [2, 1, 3]),
	([3, 4, 5, 7, 9, 8], 0, 5, [3, 4, 5, 7, 8, 9])
]

@mark.parametrize("test_list, test_low, test_high, expected_response", TEST_QUICK_SORT)
def test_quick_sort(test_list, test_low, test_high, expected_response):
	sorting.quick_sort(test_list, test_low, test_high)

	assert test_list == expected_response


TEST_SORT = [
	([], []),
	([1], [1]),
	([1, 1, 1], [1, 1, 1]),
	([2, 1, 3], [1, 2, 3]),
	([2, 2, 1, 3], [1, 2, 2, 3]),
	([2, 2, 1, 1, 3, 3], [1, 1, 2, 2, 3, 3]),
	([2, 1, 4, 3], [1, 2, 3, 4])
]
# Note: copy.deepcopy(TEST_SORT) prevents unit-tests from directly 
#		manipulating TEST_SORT for the following unit-test
@mark.parametrize("test_list, expected_response", copy.deepcopy(TEST_SORT))
def test_heap_sort(test_list, expected_response):
	sorting.heap_sort(test_list)

	assert test_list == expected_response


@mark.parametrize("test_list, expected_response", copy.deepcopy(TEST_SORT))
def test_insertion_sort(test_list, expected_response):
	sorting.insertion_sort(test_list)

	assert test_list == expected_response


@mark.parametrize("test_list, expected_response", copy.deepcopy(TEST_SORT))
def test_merge_sort(test_list, expected_response):
	sorting.merge_sort(test_list)

	assert test_list == expected_response


@mark.parametrize("test_list, expected_response", copy.deepcopy(TEST_SORT))
def test_selection_sort(test_list, expected_response):
	sorting.selection_sort(test_list)
	
	assert test_list == expected_response
