#!/usr/bin/env python3


def alien_sort(words, alphabet):
	"""
	Given a set of words, sort the words using the provided alphabet.
	For fun, the alphabet can be considered an alien alphabet that
	only uses the english alphabet characters. Just in a different order
	complexity:
		time: O(m*n)
		space: O(m*n)
	"""
	if len(words) <= 0 or len(alphabet) <= 0: return None
	if len(words) == 1: return True

	# store alphabet with unique value
	alphabet_hash = {}
	for i, letter in enumerate(alphabet):
		alphabet_hash[letter] = i

	# compare every word in words
	for j, word_j in enumerate(words[1:], 1):
		word_i = words[j - 1]

		# compare letters
		x = 0

		# check within bounds
		while x < len(word_j) and x < len(word_i):
			letter_i = alphabet_hash.get(word_i[x], float("inf"))
			letter_j = alphabet_hash.get(word_j[x], float("inf"))
			
			if letter_i > letter_j:
				return False
			if letter_i < letter_j:
				return True
			x += 1
		
		# words are of similar length
		if len(word_i) > len(word_j):
			return False

	return True


def conflict(array):
	"""
	Given an array off tuples, where every tuple is 3 elements:
		0: name
		1: x1, x2, x3
			this field can contain any integer or None (*)
			if field is 
		2: value
	Example:
		array = [
			(1. [1, 1, 2], 10),
			(2. [1, 1, None], 20),  # conflict
			
		]

	complexity:
		time:
			O(n^2)
		space:
			O(1)
	"""
	# traverse each row
	for i, row_i in enumerate(array[:-1]):
		column_i = row_i[1]
		value_i = row_i[2]

		# traverse neighboring rows
		for row_j in array[i+1:]:
			column_j = row_j[1]
			value_j = row_j[2]

			# check if x1, x2, x3 are identical
			columns_identical = (column_i[0] == column_j[0] or column_i[0] == None or column_j[0] == None) and \
				(column_i[1] == column_j[1] or column_i[1] == None or column_j[1] == None) and \
				(column_i[2] == column_j[2] or column_i[2] == None or column_j[2] == None)

			is_conflict = (columns_identical and value_i != value_j) or \
				((not columns_identical) and value_i == value_j)
			if is_conflict:
				return True

	return False


def contains_duplicates(array):
	"""
	Check if there are duplicates
	"""
	dictionary = {}
	for i in array:
		if i in dictionary:
			return True
		else:
			dictionary[i] = 1

	return False


def climb_stairs(n):
	"""
	Calculates the number of ways 'n' can be split.
	Uses memoization
	via 1 & 2.
	n:
		the number to find total number of combinations
	complexity:
		time:
			O(n)
		space:
			O(n)
	"""
	if n < 0:
		return 0

	combinations = {0: 1}
	combinations[1] = 2
	for i in range(2, n):
		combinations[i] = combinations[i-2] + combinations[i-1]

	return combinations[n-1]


def customSort(array):
	"""
	This method: 
		custom sorts the array, using minimum moves. Custom sorts means
		that all even numbers will be placed on the left
		and all odd numbers will be placed on the right. 
		This means [6, 4, 7, 5] is considered sorted
		A move consists of swapping 2 elements.
		We can expect a minimum of 2 elements
	array:
		list of integers that will be sorted
	return:
		integer representing the minimum number of moves required to custom sort
	"""
	left = 0
	right = len(array) - 1
	moves = 0

	while left < right:
		if array[left] % 2 == 0:
			# even placed correctly
			left += 1
		elif array[right] % 2 == 1:
			# odd placed correctly
			right -= 1
		else:
			# swap misplaced even & odd
			array[left], array[right] = array[right], array[left]
			left += 1
			right -= 1
			moves += 1

	return moves


def equi(a):
	"""
	An array A consisting of N integers is given. An equilibrium index of this array is any integer P such that 0 ≤ P < N and the sum of elements of lower indices is equal to the sum of elements of higher indices, i.e.
	A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
	Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or if P = N−1.
	a:
		list containing the numbers
	Complexity:
		Time: O(n)
		Space: O(1)
	"""
	if len(a) < 1: return -1

	# get the sum of all values
	sums = 0
	for value in a:
		sums += value

	# check left and right sides
	left = 0
	right = 0
	for i, value in enumerate(a):
		right = sums - (left + value)
		if left == right:
			return i
		left += value

	return -1


def fibonacci_sequence(num: int) -> int:
	"""
	Calculate the fibonacci sequence from num
	num:
		number used to calculate fibonacci sequence
	return:
		return the number from fibonacci sequence provided num
	complexity:
		time: O(n)
		space: O(n)
	"""
	if num < 0:
		return None

	sequence = [0, 1]
	for i in range(2, num+1):
		i_value = sequence[i - 1]  + sequence[i - 2]
		sequence.append(i_value)

	return sequence[num]
	

def fibonacci_sequence_inefficient(num: int) -> int:
	"""
	Calculate the fibonacci sequence from num
	num:
		number used to calculate fibonacci sequence
	return:
		return the number from fibonacci sequence provided num
	complexity:
		time: O(2^n)
		space: O(n)
	"""
	if num == 0:
		return 0	
	if num == 1:
		return 1
	return fibonacci_sequence_inefficient(num - 1) + fibonacci_sequence_inefficient(num - 2)


def first_missing_positive(numbers):
	"""
	Return the smallest unsigned integer, given a list of signed integers
	numbers:
		list of signed integers
	return:
		smallest unsigned integer
	complexity:
		time: O(n)
		space: O(n)
	"""
	# convert to set; removes duplicates
	if not numbers: return None

	numbers_set = set(numbers)

	# look for smallest unsigned integer
	i = 1
	while i < len(numbers_set) + 1 and i in numbers_set:
		i += 1

	return i


def four_sums(nums, target):
	"""
	nums:
		list of unsorted, duplicate, and signed integers
	target:
		integer to find the 4 sums for
	return:
		list of 4 unique sums
	complexity:
		time: O(n^3)
	"""
	nums.sort()
	sums = []

	for i, num_i in enumerate(nums[:-2]):
		# avoid duplicate
		if i > 0 and num_i == nums[i-1]:
			continue
		for j, num_j in enumerate(nums[i+1:-1], i+1):
			# avoid duplicate
			if i + 1 != j and num_j == nums[j-1]:
				continue

			new_target = target - num_i - num_j
			
			# sublist for new_target
			left = j + 1
			right = len(nums) - 1

			# find sum pairs for new_target
			while left < right:
				# move window
				if nums[left] + nums[right] < new_target:
					left += 1
				elif nums[left] + nums[right] > new_target:
					right -= 1
				else:
					# quadruple pairs found!
					l = [num_i, num_j, nums[left], nums[right]]
					sums.append(l)
					left += 1
					right -= 1

					# avoid duplicates
					while left < right and nums[left] == nums[left - 1]:
						print(f"duplicate left! nums[{left}]: {nums[left]} nums[{left-1}]: {nums[left-1]}")
						left += 1
					while left < right and nums[right] == nums[right + 1]:
						print(f"duplicate right! nums[{right}]: {nums[right]} nums[{right-1}]: {nums[right-1]}")
						right -= 1

	return sums


def get_index(nums, target):
	"""
	Given a sorted integer array, in ascending order, get the index of the target.
	nums:
		list of sorted numbers, please note the numbers can be rotated
		rotation example:
			[4,5,0,1,2,3]
			note rotation at index 1
	target:
		the number we are trying to find the index for
	complexity:
		time: O(log(n))
		space: O(log(n))
	"""
	return _get_index_helper(nums, target, 0, len(nums)-1)


def highest_population(population):
	"""
	Assume population data structure is built properly, with correct tuple structure.
	Given a list of population, where every element contains a (person, birthyear, deathyear),
	find the year that had the maximum number of people living.
	Assume that a birthyear always adds 1 to population and deathyear subtracts 1 from population.
	
	population:
		Array of tuples, where every tuple is of size 3.
		The tuple contains name (string), birthyear (int), deathyear (int)
	complexity:
		time: O(n)
		space: O(k)
			where k is the number of unique years
	"""
	
	# store year deltas
	years_population = {}
	for person in population:
		birthyear = person[1]
		# birthyear
		if birthyear in years_population:
			years_population[birthyear] += 1
		else:
			years_population[birthyear] = 1

		# deathyear
		deathyear = person[2]
		if deathyear in years_population:
			years_population[deathyear] -= 1
		else:
			years_population[deathyear] = 1

	# get the max year using the deltas
	max_year = float("-inf")
	for year in years_population:
		if max_year == float("-inf") or years_population[year] > years_population[max_year]:
			max_year = year

	return max_year


def is_sum_possible(nums, target):
	"""
	Recursively checks  a list of numbers sum up to the target
	nums:
		list of numbers
	target:
		the target number that the list of nums should be added to
	return:
		True if there are numbers in nums that add up to target
		False otherwise
	complexity:
		time:
			O(2^n)
		space:
			O(n)
	"""
	# run out of numbers
	if not nums: 
		if target == 0: return True
		else: return False

	# base case
	number = nums[0]
	if (target - number) == 0: return True

	# (don't use the current value) or (do use the current value)
	return is_sum_possible(nums[1:], target) or is_sum_possible(nums[1:], target - number)


def jump1(nums):
	"""
	Given an array of non-negative integers, you are initially positioned at the first index of the array.
	Each element in the array represents your maximum jump length at that position.
	Determine if you are able to reach the last index.

	Example:
		Input: nums = [2,3,1,1,4]
		Output: true
		Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
	nums:
		list of steps (integers)
	return:
		return true if we can reach the end
	complexity:
		time: O(n)
		space: O(1)
	"""
	# base case
	steps = nums[0] if nums else 0
	if len(nums) == 1 and steps >= 0: return True

	# current steps
	i = 1
	while steps and i < len(nums):
	    # remove 1 step count
	    steps -= 1
	    
	    # get max steps value
	    steps = max(steps, nums[i])

	    # take a step in nums
	    i += 1
	    
	return i >= len(nums)


def jump2(nums):
	"""
	Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
	Each element in the array represents your maximum jump length at that position.
	Your goal is to reach the last index in the minimum number of jumps.
	You can assume that you can always reach the last index.

	Example:
		Input: nums = [2,3,1,1,4]
		Output: 2
		Explanation: The minimum number of jumps to reach the last index is 2. 
					 Jump 1 step from index 0 to 1, then 3 steps to the last index.

	nums:
		list of steps (integers)
	return:
		minimum number of jumps
	"""
	# start from beginning
	curStep = 0
	i = 0
	level = 0

	while curStep < len(nums) - 1:
	    level += 1
	    
	    # update prestep
	    preStep = curStep
	    
	    # traverse of prestep level to find max step
	    # of this level
	    while i <= preStep:
	        curStep = max(curStep, i + nums[i])
	        i += 1

	return level


def longest_consecutive_subsequence(numbers):
	"""
	Find the longest consecutive subsequence from a given amount of numbers
	numbers:
		list of numbers
	return:
		the largest amount of consecutive subsequence
	complexity:
		time: O(n)
		space: O(n)
			store every element in the hashmap
	"""
	max_consecutive_numbers = 0
	num_set = set(numbers)

	for current_number in num_set:
		# check if current number is a starting point
		is_starting_number = not((current_number - 1) in num_set)
		if is_starting_number:

			# continue incrementing next number as long as it's in the set
			next_number = current_number + 1
			while next_number in num_set:
				next_number += 1

			# store max subsequence
			max_consecutive_numbers = max(max_consecutive_numbers, next_number - current_number)

	return max_consecutive_numbers


def max_subarray_dp(nums):
	"""
	Find the contiguous subarray, which has the largest sum of values.
	This method uses dynamic programming
	nums:
		list of signed integers
	return:
		largest subarray value
	complexity:
		time: O(n)
		space: O(n)
	"""
	# empty nums
	if not nums: return float("-inf")

	# allocate memory for maxes of each index
	maxes = [0] * len(nums)

	# set base case
	maxes[0] = nums[0]


	# check all numbers
	for i, current_number in enumerate(nums[1:], 1):
		previous_number = maxes[i - 1]

		# max between extending array or starting a new sub-array
		maxes[i] = max(previous_number + current_number, current_number)

	return max(maxes)


def max_subarray_ptrs(nums):
	"""
	Find the contiguous subarray, which has the largest sum of values.
	This method uses pointers
	nums:
		list of signed integers
	return:
		largest subarray value
	complexity:
		time: O(n)
		space: O(1)
	"""
	max_sum = float("-inf")
	sub_sum = 0
	start = 0
	end = 0
	i = 0

	# loop through list
	for j, number in enumerate(nums):
		sub_sum += number

		# new max found
		if sub_sum > max_sum:
			max_sum = sub_sum
			start = i
			end = j

		# anything less than 0 is useless
		if sub_sum < 0:
			i += 1
			sub_sum = 0

	return max_sum


def minion_game(s):
	"""
	There are 2 players, Kevin and Stuart, where each player gets a point
	for each occurence of the substring in the string

	complexity:
		time: O(n)
		space: O(1)

	"""
	# store vowels in set
	vowels = {'A','E','I','O','U'}

	kevsc = 0
	stusc = 0
	for i in range(len(s)):
	    if s[i] in vowels:
	        kevsc += (len(s)-i)
	    else:
	        stusc += (len(s)-i)

	# announce winner
	if kevsc > stusc:
	    winner, score =  "Kevin", kevsc
	elif kevsc < stusc:
	    winner, score = "Stuart", stusc
	else:
	    winner, score = "Draw", kevsc

	print(f"{winner} {score}")
	return (winner, score)


def two_city_sched_cost(costs):
	"""
	A company is planning to interview 2n people. 
	Given the array costs where costs[i] = [aCosti, bCosti], 
	the cost of flying the ith person to city a is aCosti, 
	and the cost of flying the ith person to city b is bCosti.
	Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

	What we do is sort, by the difference between the 2 destination, which allows us to get the smallest 0th element
	costs:
		array of arrays where each element contains a cost to [city-a, city-b]
	complexity:
		time: O(nlogn)
		space: O(1)
	"""
	costs.sort(key=lambda x: x[0]-x[1])
	half_costs_size = len(costs) / 2
	total_min_costs = 0

	for i, cost in enumerate(costs):
	    if i < half_costs_size:
	        total_min_costs += cost[0]
	    else:
	        total_min_costs += cost[1]

	return total_min_costs


def padovan_sequence(num: int) -> int:
	"""
	Calculate the padovan sequence from num
	num:
		number used to calculate padovan sequence
	return:
		return the number from padovan sequence provided num
	complexity:
		time: O(n)
		space: O(n)
	"""
	if num < 0:
		return None
	sequence = [1,1,1]
	for i in range(3, num + 1):
		i_value = sequence[i - 2] + sequence[i - 3]
		sequence.append(i_value)

	return sequence[num]
			

def padovan_sequence_inefficient(num: int) -> int:
	"""
	Calculate the padovan sequence from num
	num:
		number used to calculate padovan sequence
	return:
		return the number from padovan sequence provided num
	complexity:
		time: O(2^n)
		space: O(n)
	"""
	if num < 0:
		return None
	if num == 0 or num == 1 or num == 2:
		return 1

	return padovan_sequence_inefficient(num - 2) + padovan_sequence_inefficient(num - 3)


def plus_one(digits):
	"""
	Given a list of integers, representing an integer, increment by one
	Example: 
		[1,2,3] => [1,2,4] => (123 + 1 = 124)
		[4,3,2,1] => [4,3,2,2] => (4321 + 1 = 4322)
	digits:
		list of integers representing the integer
	return:
		list of integers incremented by
	complexity:
		time: O(n)
		space: O(1)
	"""
	if not digits: return [0]
	
	# loop through digits starting from end
	i = len(digits) - 1
	while i >= 0:
		if digits[i] < 9:
			# increment current digit and return list
			digits[i] += 1
			return digits
		else:
			digits[i] = 0
		i -= 1
	
	# add 1 
	return [1] + digits


def remove_duplicates(array):
	"""
	Remove all duplicates from sorted array "in place"
	"""
	if len(array) == 0 or len(array) == 1: return len(array)

	left_ptr = 0
	right_ptr = 1


	while right_ptr < len(array):
		if array[left_ptr] == array[right_ptr]:
			del array[right_ptr]
		else:
			left_ptr += 1
			right_ptr += 1

	return len(array)


def submatrix_sum(matrix, start_coordinate, end_coordinate):
	"""
	Given a matrix and starting and ending coordinates, 
	that define a submatrix, return the total of the submatrix
	matrix:
		list of list of integers
	start_coordinate:
		(start_column, start_row)
	end_coordinate:
		(end_column, end_row)
	complexity:
		time:
			O(mxn)
		space:
			O(1)
	return:
		sum of defined submatrix
	"""
	# get starting row and column
	column = start_coordinate[0]
	row = start_coordinate[1]

	total = 0

	# store column and row bounds
	end_column = end_coordinate[0]
	end_row = end_coordinate[1]

	empty_matrix = not matrix or not matrix[0]
	out_of_bounds = len(matrix) <= end_row or len(matrix[0]) <= end_column or \
		column < 0 or row < 0
	if empty_matrix or out_of_bounds: return 0

	# loop while until rows within bounds
	while row <= end_row:
		# reset column count
		column = start_coordinate[0]
		# loop while column within bounds
		while column <= end_column:
			# store sum
			total += matrix[row][column]
			column += 1

		row += 1

	return total


def three_sums(nums):
	"""
	Find a list of non-duplicate order of numbers that add up to zero
	nums:
		list of signed integers
	return:
		three numbers that do not add up to zero
	"""
	three_sums = []
	for i, num_i in enumerate(nums[:-1]):
		nums_set = set()
		for j, num_j in enumerate(nums[i+1:], i+1):
			target_num = 0 - num_i - num_j
			if target_num in nums_set:
				three_nums = sorted([num_i, num_j, target_num])
				if three_nums not in three_sums:
					three_sums.append(three_nums)
			nums_set.add(num_j)


	return three_sums


def three_sums_inefficient(nums):
	"""
	Find a list of non-duplicate order of numbers that add up to zero
	nums:
		list of signed integers
	return:
		three numbers that do not add up to zero
	"""
	three_sums = []
	for i, num_i in enumerate(nums):
		for j, num_j in enumerate(nums[i+1:], i+1):
			for k, num_k in enumerate(nums[j+1:], j+1):
				if num_i + num_j + num_k == 0:
					l = sorted([num_i, num_j, num_k])
					if l not in three_sums:
						three_sums.append(l)
	return three_sums


def two_sum(nums, target):
	"""
	nums:
		list of numbers
	target:
		the number to target, with 2 numbers from nums
	return:
		list of indexes for the corresponding 2 numbers in nums adding to the target
	complexity:
		time: O(n)
		space: O(n)
	"""
	m = {}

	# loop though all nums
	for i, num in enumerate(nums):
		# get new target
		new_target = target - num

		# if target in map: return current index and index in map
		if new_target in m:
			return [m[new_target], i]

		# add number to max and its index
		m[num] = i

	return []


def _get_index_helper(nums, target, start, end):
	"""
	Helper method for get_index.
	Please see get_index for additional details
	"""
	mid = start +  (end - start)//2
	
	# index found
	if nums[mid] == target:
		return mid

	# does not exist
	if end-start <= 0:
		return None

	# note: select which half of array to traverse

	# 0 - mid ordered? 
		# check if in range
		# else mid - end
	# mid - end ordered?
		# check if in range
		# else 0 - mid
	# return non exists
	
	# check first half is ascending order
	if nums[start] <= nums[mid]:
		# get first half if in range 
		if nums[start] <= target and target <= nums[mid]:
			return _get_index_helper(nums, target, start, mid-1)
		# otherwise get second half
		else:
			return _get_index_helper(nums, target, mid, end)

	elif nums[mid] <= nums[end]:
		# get second half if in range
		if nums[mid] <= target and target <= nums[-1]:
			return _get_index_helper(nums, target, mid, end)
		# otherwise get first half
		else:
			return _get_index_helper(nums, target, start, mid-1)
	else:
		print(f"Should not be here!!!")
		return []