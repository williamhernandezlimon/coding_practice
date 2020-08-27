from src.algorithm import sorting
from pytest import mark



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


# Please note: 
#	Reassigning TEST_SORT allows test_list to be reset
#	Since every test method modifies TEST_SORT's test_list by reference
TEST_SORT = [
	# TODO: add unit-tests for duplicate elements
	([], []),
	([1], [1]),
	([2, 1, 3], [1, 2, 3]),
	([2, 1, 4, 3], [1, 2, 3, 4]),
	([5, 2, 1, 6, 4, 3], [1, 2, 3, 4, 5, 6])
]
@mark.parametrize("test_list, expected_response", TEST_SORT)
def test_heap_sort(test_list, expected_response):
	sorting.heap_sort(test_list)

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
@mark.parametrize("test_list, expected_response", TEST_SORT)
def test_insertion_sort(test_list, expected_response):
	sorting.insertion_sort(test_list)

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
@mark.parametrize("test_list, expected_response", TEST_SORT)
def test_merge_sort(test_list, expected_response):
	sorting.merge_sort(test_list)

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
@mark.parametrize("test_list, expected_response", TEST_SORT)
def test_selection_sort(test_list, expected_response):
	sorting.selection_sort(test_list)
	
	assert test_list == expected_response
