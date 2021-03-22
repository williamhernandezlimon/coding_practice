#!/usr/bin/env python3
import copy
from src.data_structure.array import *
from pytest import mark


@mark.parametrize(
	"test_words, test_alphabet, expected_response", 
	[
		([], "", None),
		([], "abc", None),
		(["app", "web"], "", None),
		(["app", "web"], "webapp", False),
		(["apple", "app"], "webapp", False),
		(["app", "apple"], "aple", True),
		(["web", "app"], "webapp", True),
		(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
		(["word", "world", "row"], "worldabcefghijkmnpqrstuvxyz", False),
		(["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False)
	]
)
def test_alien_sort(test_words, test_alphabet, expected_response):
	response = alien_sort(test_words, test_alphabet)

	assert response == expected_response


@mark.parametrize(
	"test_array, expected_response",
	[
		([], False),
		([(1, [1, 1, 2], 10), (2, [1, 1, None], 10)], False),
		([(1, [1, 1, 2], 10), (2, [1, 1, None], 20)], True),
		([(1, [1, 1, 2], 10), (2, [1, 1, 2], 20)], True),
	]
)
def test_conflict(test_array, expected_response):
	response = conflict(test_array)

	assert response == expected_response


@mark.parametrize(
	"test_array, expected_response", 
	[
		([], False),
		([1], False),
		([1,1], True),
		([1,2,3,4,5,6,7,1], True),
		([1,2,3,4,5,6,7], False)
	]

)
def test_contains_duplicates(test_array, expected_response):
	response = contains_duplicates(test_array)

	assert response == expected_response


@mark.parametrize(
	"test_n, expected_response", [
		(1, 1),
		(2, 2),
		(3, 3),	
		(38, 63245986)
	]
)
def test_climb_stairs(test_n, expected_response):
	response = climb_stairs(test_n)

	assert response == expected_response


@mark.parametrize(
	"test_array, expected_response", [
		# minimum 2 elements expected
		([1, 2], 1),
		([2, 1], 0),
		([4, 13, 10, 21, 20], 1),
		([5, 8, 5, 11, 4, 6], 2)
	]
)
def test_customSort(test_array, expected_response):
	response = customSort(test_array)

	assert response == expected_response


@mark.parametrize(
	"test_array, expected_response", [
		([-1,3,-4,5,1,-6,2,1], 1),
		([-1,3,-4], -1)
	]
)
def test_equi(test_array, expected_response):
	response = equi(test_array)

	assert response == expected_response



@mark.parametrize(
	"test_num, expected_response", 
	[
		(0, 0),
		(1, 1),
		(2, 1),
		(3, 2),
		(4, 3),
		(5, 5),
		(6, 8),
		(7, 13)
	]

)
def test_fibonacci_sequence(test_num, expected_response):
	response = fibonacci_sequence(test_num)

	assert response == expected_response


@mark.parametrize(
	"test_num, expected_response", 
	[
		(0, 0),
		(1, 1),
		(2, 1),
		(3, 2),
		(4, 3),
		(5, 5),
		(6, 8),
		(7, 13)
	]

)
def test_fibonacci_sequence_inefficient(test_num, expected_response):
	response = fibonacci_sequence_inefficient(test_num)

	assert response == expected_response


@mark.parametrize(
	"test_numbers, expected_response",
	[
		([], None),
		([-1], 1),
		([1], 2),
		([1, -1], 2),
		([1, 2], 3),
		([3,4,-1,1], 2),
		([7,8,9,11,12], 1)
	]
)
def test_first_missing_positive(test_numbers, expected_response):
	response = first_missing_positive(test_numbers)

	assert response == expected_response


@mark.parametrize(
	"test_list, test_target, expected_response",
	[
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

)
def test_four_sums(test_list, test_target, expected_response):
	response = four_sums(test_list, test_target)

	assert response == expected_response



@mark.parametrize(
	"test_num_rows, expected_response", [
		(0, []),
		(1, [[1]]),
		(5, [
			     [1],
			    [1,1],
			   [1,2,1],
			  [1,3,3,1],
			 [1,4,6,4,1]
		]),
		(6, [
			     [1],
			    [1,1],
			   [1,2,1],
			  [1,3,3,1],
			 [1,4,6,4,1],
			[1,5,10,10,5,1]
		]),
	]
)
def test_generate(test_num_rows, expected_response):
	response = generate(test_num_rows)

	assert response == expected_response



@mark.parametrize(
	"test_nums, test_target, expected_response", [
		([1], 2, None),
		([1], 1, 0),
		([1,2,3], 2, 1),
		# nums below are sorted, but rotated
		([4,5,0,1,2,3], 0, 2),
		([4,5,6,0,1,2,3], 0, 3),
		

	]
)
def test_get_index(test_nums, test_target, expected_response):
	response = get_index(test_nums, test_target)

	assert response == expected_response


@mark.parametrize(
	"test_population, expected_response",
	[
		([], float("-inf")),
		([("p1", 1990, 2020)], 1990),
		([("p1", 1990, 1990), ("p2", 1990, 1990)], 1990),
		([("p1", 1990, 2020), ("p2", 1980, 2020)], 1990),
		([("p1", 1990, 2020), ("p2", 1980, 2020), ("p3", 1980, 1980)], 1990),
		([("p1", 1990, 2020), ("p2", 1980, 2020), ("p3", 1980, 1985), ("p4", 1980, 1983), ("p3", 1980, 1984)], 1980)
	]
)
def test_highest_population(test_population, expected_response):
	response = highest_population(test_population)

	assert response == expected_response




@mark.parametrize(
	"test_nums1, test_nums2, expected_response", [
		([1,2,2,1], [2,2], [2,2]),
		([4,9,5], [9,4,9,8,4], [9,4]),
		([1,2], [1,1], [1]),
	]
)
def test_intersect(test_nums1, test_nums2, expected_response):
	response = intersect(test_nums1, test_nums2)
	
	assert response == expected_response



@mark.parametrize(
	"test_nums, test_target, expected_response", [
		([], 1, False),
		([2, 3], 1, False),
		([], 0, True),
		([1, 2, 3, 4], 10, True),
		([1, 2, 3, 4], 6, True),
		([1, 2, 1, 3], 2, True),
		([1, 2, 1, 3], 7, True),
		([1, 10, 20, 30], 41, True)
	]
)
def test_is_sum_possible(test_target, test_nums, expected_response):
	response = is_sum_possible(test_nums, test_target)
	
	assert response == expected_response


@mark.parametrize(
	"test_nums, expected_response", [
		([0], True),
		([1], True),
		([2,3,1,1,4], True)
	]
)
def test_jump1(test_nums, expected_response):
	response = jump1(test_nums)

	assert response == expected_response


@mark.parametrize(
	"test_nums, expected_response", [
		([1], 0),
		([2,3,1,1,4], 2),
		([2,3,0,1,4], 2)

	]
)
def test_jump2(test_nums, expected_response):
	response = jump2(test_nums)

	assert response == expected_response


@mark.parametrize(
	"test_numbers, expected_response",
	[
		([], 0),
		([1, 2], 2),
		([1, 8, 8, 5, 2, 3], 3),
		([1, 1, 1, 1], 1),
		([-1, -2], 2),
		([-10, -11, -12], 3)
	]
)
def test_longest_consecutive_subsequence(test_numbers, expected_response):
	response = longest_consecutive_subsequence(test_numbers)

	assert response == expected_response


@mark.parametrize(
	"test_nums, expected_response", [
		([3,2,3], 3),
		([2,2,1,1,1,2,2], 2),
	]
)
def test_majority_element(test_nums, expected_response):
	response = majority_element(test_nums)
	
	assert response == expected_response


@mark.parametrize("test_height, expected_response", [
		([], 0),
		([1,1], 1),
		([1,8,6,2,5,4,8,3,7], 49)
	]
)
def test_max_area(test_height, expected_response):
	response = max_area(test_height)

	assert response == expected_response


@mark.parametrize(
	"test_prices, expected_response", [
		([7,1,5,3,6,4], 5),
		([7,6,4,3,1], 0)
	]
)
def test_max_profit(test_prices, expected_response):
	response = max_profit(test_prices)
	
	assert response == expected_response



@mark.parametrize(
	"test_nums, expected_response", [
		([], float("-inf")),
		([1], 1),
		([1, 2], 3),
		([1, -1], 1),
		([-2,1,-3,4,-1,2,1,-5,4], 6)
	]
)
def test_max_subarray(test_nums, expected_response):
	response = max_subarray_ptrs(test_nums)
	assert response == expected_response

	response = max_subarray_dp(test_nums)
	assert response == expected_response


@mark.parametrize(
	"test_nums1, test_n, test_nums2, test_m, expected_response", [
		([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6]),
		([4,5,6,0,0,0], 3, [1,2,3], 3, [1,2,3,4,5,6])
	]
)
def test_merge(test_nums1, test_n, test_nums2, test_m, expected_response):
	merge(test_nums1, test_n, test_nums2, test_m)

	assert test_nums1 == expected_response


@mark.parametrize(
	"test_s, expected_response", [
		("BANANA", ("Stuart", 12)),
		("W", ("Stuart", 1)),
		("WW", ("Stuart", 3)),
		("A", ("Kevin", 1)),
		("AA", ("Kevin", 3)),
		("", ("Draw", 0))
	]
)
def test_minion_game(test_s, expected_response):
	response = minion_game(test_s)

	assert response == expected_response


@mark.parametrize("test_nums, expected_response", [
		([3,0,1], 2),
		([0,1], 2),
		([9,6,4,2,3,5,7,0,1], 8),
		([0], 1)
	]
)
def test_missing_number(test_nums, expected_response):
	response = missing_number(test_nums)

	assert response == expected_response


@mark.parametrize(
	"test_nums, expected_response", [
		([0], [0]),
		([1], [1]),
		([0, 1], [1, 0]),
		([0,1,0,3,12], [1,3,12,0,0]),
		([4,2,4,0,0,3,0,5,1,0], [4,2,4,3,5,1,0,0,0,0])
	]
)
def test_move_zeros(test_nums, expected_response):
	move_zeros(test_nums)

	assert test_nums == expected_response


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


@mark.parametrize("test_nums, expected_response", [
		([], []),
		([1], [[1]]),
		([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
	]
)
def test_permute(test_nums, expected_response):
	response = permute(test_nums)

	assert response == expected_response


@mark.parametrize(
	"test_digits, expected_response", [
		([], [0]),
		([0], [1]),
		([1], [2]),
		([1, 2], [1, 3]),
		([1, 2, 3], [1, 2, 4]),
		([9], [1, 0]),
		([9, 9], [1, 0, 0]),
		([9, 9, 9], [1, 0, 0, 0])
	]
)
def test_plus_one(test_digits, expected_response):
	response = plus_one(test_digits)

	assert response == expected_response


@mark.parametrize(
	"test_array, expected_response",
	[
		([], 0),
		([1], 1),
		([1,1,1,1,1], 1),
		([1,1,2,2,3,3,4,4,5,5,6,6,7,7], 7)
	]
)
def test_remove_duplicates(test_array, expected_response):
	response = remove_duplicates(test_array)
	
	assert response == expected_response


@mark.parametrize("test_matrix, expected_response", [
		([[]], [[]]),
		([[1]], [[1]]),
		([[1,2],[3,4]], [[3,1],[4,2]]),
		([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]]),
		([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
	]
)
def test_rotate(test_matrix, expected_response):
	rotate(test_matrix)

	assert test_matrix == expected_response

@mark.parametrize("test_nums, test_target, expected_response", [
		([], 0, -1),
		([1,3], 3, 1),
		([3,4,5,6,7,8,1,2], 2, 7),
		([2], 3, -1),
		([2,1], 0, -1),
		([4,5,6,7,0,1,2], 0, 4)
	]
)
def test_search(test_nums, test_target, expected_response):
	response = search(test_nums, test_target)

	assert response == expected_response


@mark.parametrize("test_nums, test_target, expected_response", [
		([5,7,7,8,8,10], 8, [3,4]),
		([5,7,7,8,8,10], 7, [1,2]),
		([5,7,7,8,8,10], 5, [0,0]),
		([5,7,7,8,8,10], 21, [-1,-1]),
		([0], 0, [0,0]),
		([0,1], 0, [0,0]),
		([0,0], 0, [0,1]),
		([1,4], 4, [1,1]),
		([0,0,0,0,0,0,0], 0, [0,6]),
	]
)
def test_search_range(test_nums, test_target, expected_response):
	response = search_range(test_nums, test_target)

	assert response == expected_response


@mark.parametrize("test_nums, expected_response", [
		([2,0,2,1,1,0], [0,0,1,1,2,2]),
		([2,0,1], [0,1,2]),
		([0], [0]),
		([1], [1]),
	]
)
def test_sort_colors(test_nums, expected_response):
	sort_colors(test_nums)

	assert test_nums == expected_response


@mark.parametrize(
	"test_matrix, test_start_coordinate, test_end_coordinate, expected_response", [
		([[]], (0,0), (2,2), 0),
		([[1,2,3],[4,5,6],[7,8,9]], (0,0), (0,0), 1),
		([[1,2,3],[4,5,6],[7,8,9]], (-1,0), (0,0), 0),
		([[1,2,3],[4,5,6],[7,8,9]], (10,0), (0,0), 0),
		([[1,2,3],[4,5,6],[7,8,9]], (0,0), (2,2), 45),
		([
			[0, 2, 5, 4, 1],
			[4, 8, 2, 3, 7],
			[6, 3, 4, 6, 2],
			[7, 3, 1, 8, 3],
			[1, 5, 7, 9, 4]
		], (1,1), (3,3), 38)
	]
)
def test_submatrix_sum(test_matrix, test_start_coordinate, test_end_coordinate, expected_response):
	response = submatrix_sum(test_matrix, test_start_coordinate, test_end_coordinate)

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


@mark.parametrize(
	"test_costs, expected_response", 
	[
		([], 0),
		([[3, 4]], 3),
		([[3, 4], [5, 6]], 9),
		([[3, 4], [5, 6], [7, 8]], 16),
		([[10,20],[30,200],[400,50],[30,20]], 110),
		([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]], 1859),
		([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]], 3086)
	]
)
def test_two_city_sched_cost(test_costs, expected_response):
	response = two_city_sched_cost(test_costs)

	assert response == expected_response


@mark.parametrize(
	"test_num, test_target, expected_response",
	[
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
)
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


