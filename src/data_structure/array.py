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
		while x < len(word_j) and x < len(word_i):  # within bounds
			letter_i = alphabet_hash[word_i[x]] if word_i[x] in alphabet_hash else float("inf")
			letter_j = alphabet_hash[word_j[x]] if word_j[x] in alphabet_hash else float("-inf")
			
			print(f"word_i: {word_i} letter_i {letter_i} word_j: {word_j} letter_j {letter_j}")
			if letter_i > letter_j:
				return False
			if letter_i < letter_j:
				return True
			x += 1
		
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
	for j, num in enumerate(nums):
		new_target = target - num
		if new_target in m:
			i = m[new_target]
			return [i, j]
		else:
			m[num] = j
	
	return []







