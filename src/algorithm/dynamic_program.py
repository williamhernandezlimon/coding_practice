#!/usr/bin/env python3
import logging 
import math

from src.data_structure import table as table_object
from src import utils


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def get_minimum_string_transformations(s1, s2):
	"""
	Uses dynamic programming to get minimum number of string transformations
	to transform s1 to s2, or vice-versa. Transformations include:
		delete character, add character, remove character, and do nothing
	:return: the minumum number of string tranformations to 
	Time complexity
		O(s1xs2)
	Space complexity
		O(s1xs2)
	"""
	if s1 == s2: return 0
	rows = len(s2) + 1
	columns = len(s1) + 1
	table = table_object.create(rows, columns)

	# base case
	for column in range(columns):
		table[0][column] = column
	for row in range(rows):
		table[row][0] = row

	# dynamic program
	for row in range(1, rows):
		for column in range(1, columns):
			delete_cost = table[row][column-1]
			add_cost = table[row-1][column]
			replace_cost = table[row-1][column-1]
			
			# get minimum cost and assign to cell
			min_cost = utils.get_minimum_number(delete_cost, add_cost, replace_cost)
			table[row][column] = min_cost if s1[column-1] == s2[row-1] else min_cost + 1

	table_object.draw(table)
	return table[rows-1][columns-1]


def minimum_change(amount, coins):
	"""
	Given a list of integer coins. Return the least amount of coins needed to 
	make change that adds up to the provided integer amount
	amount:
		integer amount the coins needs to make change for
	coins:
		denomination used to create amount
	complexity:
		time: O(nxm) where m is the amount and n are the coins
		space: O(m) where m is the amount
	"""
	# TODO: add cases for when no change can be made

	# base case
	if amount <= 0 or len(coins) == 0: return 0

	# create subproblem memory
	subproblem = [float("inf") for i in range(amount + 1)]

	# another base case
	subproblem[0] = 0

	# fill in all subproblems
	for i in range(len(subproblem)):

		# for coin, use sub problem, to find the least amount of coins
		for coin in coins:

			# check within range
			if i - coin >= 0:
				subproblem[i] = min(subproblem[i], subproblem[i - coin] + 1)

	# if no coins can make amount, return -1
	return subproblem[-1] if subproblem[-1] != float("inf") else -1




def knapsack(weight_limit, items):
	"""
	Dynamic program
	weight_limit:
		the maximum weight a user can use
	items:
		weight:
			the weight of a given item
		value:
			the value of a given item
	return:
		the maximum value for a given weight_limit
	"""
	rows = len(items) + 1
	columns = weight_limit + 1
	table = table_object.create(rows, columns)

	# base case
	for row in range(rows):
		table[row][0] = 0
	for column in range(columns):
		table[0][column] = 0

	# dynamic program
	row = 1
	for weight, value in items.items():
		for column in range(1, columns):
			accept_item_cost = table[row-1][column-weight] + value if weight <= column else 0
			ignore_item_cost = table[row-1][column]

			table[row][column] = max(ignore_item_cost, accept_item_cost)
		row += 1
		
	return table[rows-1][columns-1]

def knapsack_recursive(weight_limit, items, max_values={}):
	"""
	Dynamic program that is recursive using memoization.
	weight_limit:
		the maximum weight a user can use
	items: 
		weight:
		 	the weight of  a given item
	 	value:
	 		the value of a given itme
	return:
		the maximum value for a given weight_limit
	"""
	if weight_limit in max_values:
		return max_values[weight_limit]

	max_value = 0
	for weight, value in items.items():
		if weight <= weight_limit:

			sub_max_value = knapsack_recursive(weight_limit - weight, items, max_values) 
			if sub_max_value + value > max_value:
				max_value = sub_max_value + value 

	max_values[weight_limit] = max_value
	return max_value


def max_profit(prices, max_transactions):
	"""
	Get the max profit (buying then selling) of stock
	provided a given amount of transactions
	Time: O(prices^2*transactions)
	Space: O(price*transactions)
	"""
	rows = len(prices) + 1
	columns = max_transactions + 1
	table = table_object.create(rows, columns)


	# base cases
	# no profit with 0 or 1 price
	for row in range(rows):
		table[row][0] = 0
		table[row][1] = 0
	# no profit with 0 or 1 transaction
	for column in range(columns):
		table[0][column] = 0

	# dynamic program
	for row in range(1, rows):
		for column in range(1, columns):
			profit_without_selling = table[row][column-1]
			selling_price = prices[row-1]
			profit_with_selling = 0
			for r in range(row):
				buying_price = prices[r]
				buying_profit = table[r][column-1]

				LOGGER.debug(f"selling_price + buying_price + buying_profit: {selling_price + buying_price + buying_profit}")
				if selling_price - buying_price + buying_profit > profit_with_selling:
					profit_with_selling = selling_price + table[r][column-1] - buying_price
				
			table[row][column] = max(profit_without_selling, profit_with_selling)

	table_object.draw(table)
	return table[rows-1][columns-1]


def max_profit_time_optimized(prices, max_transactions):
	"""
	Dynamic program
	Get the max profit (buying then selling) of stock
	provided a given amount of transactions
	Time: O(prices*transactions)
	Space: O(price*transactions)

	# Source: https://www.youtube.com/watch?v=Pw6lrYANjz4
	"""
	if len(prices) == 0 or max_transactions == 0: return 0
	columns = len(prices)
	rows = max_transactions + 1
	table = [[0 for column in range(columns)] for row in range(rows)]

	for row in range(1, rows):

		# max_buy_price_previous_profit stores redundant computation
		max_previous_profit = float("-inf")  
		for column in range(1, columns):
			buying_price = prices[column-1]
			previous_profit = table[row-1][column-1]
			max_previous_profit = max(max_previous_profit, -buying_price + previous_profit)
			
			# selling vs not-selling
			selling_price = prices[column]
			profit_with_selling = selling_price + max_previous_profit
			profit_without_selling = table[row][column-1]
			
			LOGGER.debug(f"buying_price: {buying_price} previous_profit: {previous_profit} max_previous_profit: {max_previous_profit}")
			table[row][column] = max(profit_without_selling, profit_with_selling)

	# table_object.draw(table)
	return table[-1][-1]


def change_combinations(amount, coins):
	"""
	Dynamic program
	Return the total number of ways to make change,
	given the total amount and the type of coins
	"""
	table = [[0] * (amount+1) ] * (len(coins)+1)
	
	for row in range(len(coins)+1):
		for column in range(amount+1):
			if column == 0:
				table[row][column] = 1
			elif row == 0:
				table[row][column] = 0
			elif column - coins[row-1] < 0:
				table[row][column] = table[row-1][column]
			elif column - coins[row-1] >= 0:
				table[row][column] = table[row-1][column] \
					+ table[row][column - coins[row-1]]
			else:
				print("Should not be here!")

	print (f"number of ways: {table[len(coins)][amount]}")
	return table[len(coins)][amount]


def get_median(array1, array2):
	"""
	arrray1: sorted float array
	array2: sorted float array
	Returns the median between array1 and array2
	"""

	## both are empty arrays
	if array1 == [] and array2 == []: return None

	array1_len = len(array1)
	array2_len = len(array2)
	combined_length = array1_len + array2_len
	combined_array_is_even = combined_length % 2 == 0
	theres_an_empty_array = combined_length == array1_len or combined_length == array2_len

	# one empty array
	if theres_an_empty_array:
		new_array = array1 if array1_len > 0 else array2
		median_position = int(combined_length/2)
		median = (new_array[median_position] + new_array[median_position-1])/2 if combined_array_is_even else new_array[median_position]
		return median

	## no empty arrays
	i = 0
	ptr_array1 = 0
	ptr_array2 = 0
	new_array = []
	new_array_length = int(combined_length/2) + 1
	while i < new_array_length:
			print(f"ptr_array1: {ptr_array1} ptr_array2: {ptr_array2}")
			array1_explored = ptr_array1 >= array1_len
			array2_explored = ptr_array2 >= array2_len

			if array2_explored or (not(array1_explored) and (array1[ptr_array1] <= array2[ptr_array2])):
				new_array.append(array1[ptr_array1])
				ptr_array1 += 1
			elif array1_explored or (not(array2_explored) and (array1[ptr_array1] >= array2[ptr_array2])):
				new_array.append(array2[ptr_array2])
				ptr_array2 += 1
			else:
				print(f"ERROR: ptr_array1: {ptr_array1} ptr_array2: {ptr_array2} new_array: {new_array}")
			i += 1
	median = (new_array[-1] + new_array[-2])/2 if combined_array_is_even else new_array[-1]
	return median


def trailing_zeros(n):
	"""
	Given a number, n. Find how many trailing zeros there are,
	for the fibonacci sequence number.
	n:
		interger, to get the fib number and trailing zeros
	return:
		return the number of trailing zeros
	"""

	# get factorial value
	factorial = 1
	i = 1
	while i <= n:
		factorial *= i
		i += 1

	# get trailing zeros count from factorial
	trailing_zeros_count = 0
	while factorial % 10 == 0:
		factorial //= 10
		trailing_zeros_count += 1


	return trailing_zeros_count

# def get_first_missing_positive(array):
# 	"""
# 	Get the smallest positive number.
# 	Accomplished by storing only the first hole in the sorted array
# 	"""

# 	# assumes len(array) > 2
# 	holes = {}
# 	current = 0
# 	next = 1
# 	while current < len(array):
# 		if current == next or current in holes: continue

# 		hole_is_patched = (i == key + 1) and (i == value - 1)
# 		if hole_is_patched:
# 			print("hole is patched")
# 			# remove hole
# 			pass
# 		elif current in holes:
# 			# add hole

# 	if key == value:
# 		first_missing_number = 1 if key > 1 else key + 1
# 	if