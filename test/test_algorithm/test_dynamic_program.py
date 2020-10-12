#!/usr/bin/env python3
from src.algorithm.dynamic_program import *
from pytest import mark


TEST_CHANGE_COMBINATIONS = [
	(5, [1,2,5], 4)
]
@mark.parametrize("test_amount, test_coins, expected_response", TEST_CHANGE_COMBINATIONS)
def test_change_combinations(test_amount, test_coins, expected_response):
	response = change_combinations(test_amount, test_coins)
	assert response == expected_response


GET_MEDIAN_TESTS = [
	([2,4,6,7,102,103], [50,100,150], 50),
	([1,2], [3,4], 2.5),
	([0,0], [0,0], 0),
	([2], [], 2),
	([], [1,2,3,4], 2.5),
	([100001], [100000], 100000.5)
]
@mark.parametrize("test_sorted_array1, test_sorted_array2, expected_response", GET_MEDIAN_TESTS)
def test_get_median(test_sorted_array1, test_sorted_array2, expected_response):
	response = get_median(test_sorted_array1, test_sorted_array2)

	assert response == expected_response


GET_MINIMUM_STRING_TRANSFORMATIONS_TESTS = [
	("benyam", "ben", 3),
	("benyam", "ephrem", 5)
]
@mark.parametrize("test_string1, test_string2, expected_response", GET_MINIMUM_STRING_TRANSFORMATIONS_TESTS)
def test_get_minimum_string_transformations(test_string1, test_string2, expected_response):
	response = get_minimum_string_transformations(test_string1, test_string2)

	assert response == expected_response


KNAPSACK_TESTS = [
	(7, {}, 0),
	(0, {5: 60, 3: 50, 4: 70, 2: 30}, 0),
	(5, {5: 60, 3: 50, 4: 70, 2: 30}, 80)
]
@mark.parametrize("test_weight, test_items, expected_response", KNAPSACK_TESTS)
def test_knapsack(test_weight, test_items, expected_response):
	response = knapsack(test_weight,  test_items)
	
	assert response == expected_response


	response = knapsack_recursive(test_weight, test_items)
	assert response == expected_response


MAX_PROFIT_TESTS = [
	([5,11,3,50,60,90], 2, 93)
]
@mark.parametrize("test_prices, test_max_transactions, expected_response", MAX_PROFIT_TESTS)
def test_max_profit(test_prices, test_max_transactions, expected_response):
	response = max_profit(test_prices, test_max_transactions)
	
	assert response == expected_response


MAX_PROFIT_TIME_OPTIMIZED_TESTS = [
	([5,11,3,50,60,90], 2, 93)
]
@mark.parametrize("test_prices, test_max_transactions, expected_response", MAX_PROFIT_TESTS)
def test_max_profit_time_optimized(test_prices, test_max_transactions, expected_response):
	response = max_profit_time_optimized(test_prices, test_max_transactions)
	
	assert response == expected_response
