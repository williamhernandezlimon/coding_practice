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


def connect_four_winner(board, move, player):
	"""
	Check to see if the player is winner based on given move

	0 0 0 0
	0 0 0 0
	0 0 0 0
	1 1 1 1

	"""
	# check valid matrix
	if not board:
		return False

	x, y = move[0], move[1]
	# make move
	board[y][x] = player
	print(f"board: {board}")

	# check if move is winning move for player
	def helper(count, x, y):
		print(f"count: {count} x: {x} y: {y}")
		# base case
		if count == 0:
			return True

		winner = False
		# check up
		if y+1 < len(board)-1:
			print(f"checking up")
			if board[y+1][x] == player and helper(count-1, x, y+1):
				return True
			# diagonal right
			if x+1 < len(board[y])-1 and board[y+1][x+1] == player:
				print(f"checking up diagonal")
				if helper(count-1, x+1, y+1):
					return True
			
			# diagonal left
			if x-1 >= 0 and board[y+1][x-1] == player and helper(count-1, x-1, y+1):
				return True

		# check down
		if y-1 >= 0:
			print(f"checking down")
			if board[y-1][x] == player and helper(count-1, x, y-1):
				return True
			# diagonal left
			if x-1 >= 0 and board[y-1][x-1] == player and helper(count-1, x-1, y-1):
				return True
			
			# diagonal right
			if x+1 < len(board[y])-1 and board[y-1][x+1] == player:
				print(f"checking up diagonal")
				if helper(count-1, x+1, y-1):
					return True

		# check left
		if x-1 >= 0:
			print(f"checking left")
			if board[y][x-1] == player and helper(count-1, x-1, y):
				return True

		# check right
		if x+1 < len(board[y])-1 and board[y][x+1] == player:
			print(f"checking right")
			if helper(count-1, x+1, y):
				return True

		return False


	return helper(3, move[0], move[1])


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


def generate(num_rows):
	"""
	Generate the pascal triangle for a given number of rows
	num_rows:
		the number of rows the pascal triangle should have
	return:
		pascal triangle, with the number of num_rows
	complexity:
		time: O(nxm), where n is num_rows and m is len(num_rows)
		space: O(nxm)
	"""
	# base case if 0
	if num_rows == 0:
		return []

	rows = [[1]]
	i = 1
	# loop while num_rows
	while i < num_rows:
		# get prev list
		top_row = rows[i - 1]
		# start 1
		j = 1
		# make new list with 1 inside, rows
		r = [1]

		# loop start < list len -1
		while j < len(top_row):
			# append top_left + top_right
			top_left = top_row[j-1]
			top_right = top_row[j]
			r.append(top_left + top_right)
			j += 1
		# append 1 at end
		r.append(1)
		# add new row and increment i
		rows.append(r)
		i += 1

	# return rows
	return rows


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


def integer_break(n):
	"""
	Given an integer n, break it into the sum of k positive 
	integers, where k>=2 and maximize the product of those
	integers
	n:
		unsigned integer that must be cut into pieces
	return:
		integer with the maximum product value
	complexity:
		time: O(N)
		space: O(1)
	"""
	max_product = 1

	if n < 2: return 0
	if n == 2: return 1
	if n == 3: return 2

	while n > 4:
		max_product *= 3
		n -= 3

	max_product *= n
	return max_product


def intersect(nums1, nums2):
	"""
	Get intersect of numbers between nums1 & nums2
	nums1:
		unsorted integer array
	nums2:
		unsorted integer array
	return:
		the intersect of numbers between nums1 & nums2
	complexity:
		time: O(n+m)
		space: O(n)
	"""
	visited = {}
	larger = nums1 if len(nums1) >= len(nums2) else nums2
	smaller = nums1 if len(nums1) < len(nums2) else nums2

	# loop through smaller to store int as key and count as value
	for i in smaller:
		if i in visited:
			visited[i] += 1
		else:
			visited[i] = 1

	intersect = []
	# loop through larger
	for i in larger:
		# if int in map, append to intersect and decrement from map
		if i in visited and visited[i] > 0:
			intersect.append(i)
			visited[i] -= 1

	return intersect


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


def max_area(height):
	"""
	Given a list of integers, find the max area between them
	height:
		list of integers
	return:
		max area given heights
	complexity:
		time: O(N)
		space: O(1)
	"""
	area = 0
	i = 0
	j = len(height) - 1
	# traverse to find max area
	while i < j:
		# store max area
		area = max(min(height[i], height[j]) * (j - i), area)

		if height[i] < height[j]:
			i += 1
		else:
			j -= 1
	
	# return max area
	return area


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


def majority_element(nums):
	"""
	Find and return the integer that occurs most frequently
	Assume there's an integer that occurs most frequently
	nums:
		list of integers
	return:
		gets the integer that occurs most frequently in the list
	complexity:
		time: O(n)
		space: O(1)
	"""
	frequency = 0
	majority_element = None
	# loop thorugh elements
	for num in nums:
		# if frequency == 0:
		if frequency == 0:
			# save current element, as new majority, and frequency as 1
			majority_element = num
			frequency = 1
		# elif element == majority element:
		elif num == majority_element:
			# increment value
			frequency += 1
		# else
		else:
			# decrement value
			frequency -= 1

	return majority_element


def max_profit(prices):
	"""	
	Given prices, find the max profit for buying/selling stock market
	prices:
		integer stock market prices
	return:
		max profit from buying/selling
	complexity:
		time: O(n)
		space: O(1)
	"""

	# initialze min
	min_price = float("inf")
	max_profit = float("-inf")
	# loop through prices starting from 1
	for price in prices:
		min_price = min(min_price, price)
		# store min & max based on 
		max_profit = max(max_profit, price - min_price)
	
	return max_profit


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


def merge(nums1, n, nums2, m):
	"""
	Merge 2 sorted arrays to merge into nums1 & nums2 into nums1
	nums1:
		sorted array of integers, with dead space elements
		len(nums1) == n + m
	n:
		the amount of relevant integers
	nums2:
		sorted array of integers
	m:
		the amount of relevant integers in m
	return:
		nums1 sorted containing integers from nums2
	complexity:
		time: O(n)
		space: O(1)
	"""
	# we assume enough space in nums1 to hold nums2
	if m + n != len(nums1):
		return None

	# start at the end of nums1 & nums2
	# loop until reached start of nums1 and nums2 or 
	i = m - 1
	j = n - 1
	k = len(nums1) - 1
	while i >= 0 or j >= 0:
		# i >= j
		if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
			nums1[k] = nums1[i]
			i -= 1
		# i < j
		else:
			nums1[k] = nums2[j]
			j -= 1
		# reduce k
		k -= 1


def minimal_heaviest_setA(arr):
	""""
	Amazon Assessment question
	An Amazon fullfillment associate gas a set of items that need to be
	packed into two boxes. Given an integer array of the item weights (arr)
	to be packed, divide the item weights into two subsets A and B for
	packing into the associated boxes, while respecting the 
	following conditions:
		The intersection of A and B is null
		The union A and B is equal to the original array
		The number of elements in subsetA is minimal
		The sum of A's weights is greater than the sum of B's weights
	arr:
		list of integers representing the weights.
	return:
		The subset A in increasing order where the sum of A's weights 
		is greater than the sum of B's weight's. If more than one subset A
		exists, return the one with the maximal total weight
	complexity:
		time: O(NlogN)
		space: O(N) 
			O(1) if pointer is returned instead of new list
	"""
	# sort arr
	arr.sort()

	# get the sum of all numbers in arr
	total = sum(arr)

	# track A and B sum
	a_sum = 0
	b_sum = total

	# start from the greatest value, end of the array
	# loop while in bounds and sum A < sum B
	for i in range(len(arr)-1, -1, -1):
		a_sum += arr[i]
		b_sum -= arr[i]

		if a_sum > b_sum:
			break

	a = arr[i:]
	b = arr[0:i]

	print(f"i: {i} a_sum: {a_sum} b_sum: {b_sum} a: {a} b: {b}")
	return a


def minimum_path_sum(grid):
	"""
	Given a m x n grid filled with non-negative numbers, 
	find a path from top left to bottom right, 
	which minimizes the sum of all numbers along its path.
	Note you can only move either down or right at any point in time.
	Used dynamic programming
	grid:
		list of lists containing positive numbers.
	"""
	# for each cell, update cell to have new value (min(left, up))
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			up = grid[y-1][x] if y > 0 else float("inf")
			left = grid[y][x-1] if x > 0 else float("inf")

			if up == float("inf") and left == float("inf"):
				continue

			grid[y][x] += min(up, left)

	# return bottom right cell value
	return grid[-1][-1]


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


def missing_number(nums):
	"""
	Return the missing number in nums
	nums:
		contains integer numbers from 0-n, where there's 1 missing n
	return:
		missing number
	complexity:
		time: O(N)
		space: O(1)
	"""
	# caclulate the expected total & calculate actual total
	total = 0
	total_nums = 0
	for i, num in enumerate(nums, 1):
		total += i
		total_nums += num

	# compare the 2 to find the missing number
	return total - total_nums


def most_visited_pattern(username, timestamp, website):
	"""
	A 3-sequence is a list of websites of length 3 sorted 
	in ascending order by the time of their visits.  
	(The websites in a 3-sequence are not necessarily distinct.)

	Find the 3-sequence visited by the largest number of users. 
	If there is more than one solution, 
	return the lexicographically smallest such 3-sequence.
	
	username:
		list of strings containing of the website visitors
	timestamp:
		list of strings containing the timestamp of the visitation
	website:
		list of strings containing the website that was visited
	"""
	# ---> [(3, 'joe', 'career'),....]
	packed_tuple = zip(timestamp, username, website) 
	# sort by timestamp (By default tuple always sorted by first item )
	sorted_packed_tuple = sorted(packed_tuple) 

	mapping = {}
	for t, u, w in sorted_packed_tuple:
		# joe: [home, about, career]  
		# websites in list are in ascending timestamp order
	    if u in mapping:
	    	mapping[u].append(w)
	    else:
	    	mapping[u] = [w]

	# use a dict for counting
	counter_dict = {}
	from itertools import combinations
	for website_list in mapping.values():

		# size of combination is set to 3 
		combs = set(combinations(website_list, 3))
		for comb in combs:
			 # Tuple as key, counter as value: ('home', 'about', 'career') : 2
			if comb in counter_dict:
				counter_dict[comb] += 1      
			else:
				counter_dict[comb] = 1

	# sort descending by value, then lexicographically
	sorted_counter_dict = sorted(
		counter_dict, 
		key=lambda x: (-counter_dict[x], x)
	)

	return sorted_counter_dict[0]


def move_zeros(nums):
	"""
	nums:
		list of integers where all zeros must be moved to the right
		after the execution completion.
	return:
		return nums list, where all zeros are moved to the right
	"""
	i = 0
	j = 1
	# loop until j < len(nums)
	while j < len(nums):
		# if i == 0 and j != 0
		if nums[i] == 0 and nums[j] != 0:
			# swap
			nums[i], nums[j] = nums[j], nums[i]
			i += 1

		# if i != 0
		if nums[i] != 0:
			i += 1
			# increment i

		# increment j
		j += 1

	return nums


def num_pairs_divisible_by_60(time):
	"""
	Given a list of songs where ith song has a duration of time[i] seconds,
	get the number of pair songs for which their total duration in seconds
	is divisible by 60
	time:
		seconds of song duration time
	return:
		number of pairs of songs for which their total duration in seconds
		is divisible by 60
	"""
	c = [0] * 60
	res = 0
	for t in time:
		# increment value of missing pair
	    res += c[-t % 60]
	    
		# track seen value
	    c[t % 60] += 1

	return res


def number_of_islands(grid):
	"""
	Return the number of islands. Do not check diagonals.
	grid:
		list of list containing either "0" or "1"
		where "1" represents land and "0" represents water
	complexity:
		time: O(NxM)
		space: O(N+M)
	"""
	# helper method
	def land_to_water(y, x):
		# base case
		if grid[y][x] != "1":
			return

		# convert current cell to water
		grid[y][x] = "0"

		# up
		if y > 0:
			land_to_water(y-1, x)
		# down
		if y < len(grid)-1:
			land_to_water(y+1, x)			
		# left
		if x > 0:
			land_to_water(y, x-1)
		# right
		if x < len(grid[y])-1:
			land_to_water(y, x+1)

	island_count = 0
	# for each cell, run dfs checking island count
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			# if cell == 1:
			if grid[y][x] == "1":
				# change land (1) to water (0) for neighbors
				land_to_water(y, x)
				# increment island count
				island_count += 1

	# return island count
	return island_count


def trap(height):
	"""
	Given n non-negative integers representing an elevation map
	where the width of each bar is 1, 
	compute how much water it can trap after raining.
	height:
		string of unsigned integers representing the height of the wall
	complexity:
		time: O(N)
		space: O(N)
	"""
	# store left max
	left_map = {}
	left_max = 0 
	for i in range(len(height)):
		left_max = max(height[i], left_max)
		left_map[i] = left_max

	# store right max
	right_map = {}
	right_max = 0
	for i in range(len(height)-1, -1, -1):
		right_max = max(height[i], right_max)
		right_map[i] = right_max

	# get min between left max & right max
	total_water = 0
	for i in range(len(height)):
		total_water += min(left_map[i], right_map[i]) - height[i]

	return total_water


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


def permute(nums):
	"""
	Caclulate all permutations of order of list nums
	nums:
		list of unique integers
	return:
		all permutations from list nums
	complexity:
		time: O(N^2)
		space: O(N)
	"""
	perms = []
	temp = []

	def backtrace(perms, temp, nums):
		if temp and len(temp) == len(nums):
			# make sure to copy temp, otherwise will be empty in the end
			perms.append(temp.copy())
		else:
			# loop through everything but skip what has already been added
			for num in nums:
				# append if not in list
				if num in temp: continue
				temp.append(num)

				# add other perms
				backtrace(perms, temp, nums)

				# remove num
				temp.pop(-1)

	backtrace(perms, temp, nums)
	return perms


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


def rotate(matrix):
	"""
	Rotate matrix 90 degrees clockwise
	matrix:
		NxN arrays 
	complexity:
		time: O(NxM)
		space: O(1)
	"""
	# reverse
	l = 0
	r = len(matrix) -1
	while l < r:
		matrix[l], matrix[r] = matrix[r], matrix[l]
		l += 1
		r -= 1

	# transpose
	for i in range(len(matrix)):
		for j in range(i):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def search(nums, target):
	"""
	Find the index of the target in nums
	nums:
		list of integers, non-duplicate. Sorted, but rotated at unknown pivot
	return:
		integer representing the index of target otherwise -1
	complexity:
		time: O(logN)
		space: O(logN)
	"""

	def helper(nums, target, start, end):
		if not nums or start > end: 
			return -1		
		# mid = start + ((end-start)//2)
		mid = (start+end) // 2
		if nums[mid] == target:
			return mid

		# ascending
		if nums[start] <= nums[mid]:
			# within range
			if nums[start] <= target and target <= nums[mid]:
				end = mid-1
			else:
				start = mid+1

		# descending
		else:
			if nums[mid] <= target and target <= nums[end]:
				start = mid + 1
			else:
				end = mid - 1

		return helper(nums, target, start, end)


	return helper(nums, target, 0, len(nums)-1)


def search_range(nums, target):
	"""
	Find the range of indicies where target is represented in nums
	nums:
		sorted integers, that could have duplicates
	complexity:
		time: O(logN)
		space: O(1)
	"""
	# find first instance's index of target
	index, start, end = -1, 0, len(nums) - 1
	while start <= end:
		mid = (start + end)//2
		# target found
		if nums[mid] == target:
			index = mid
			break

		# target in left?
		if nums[start] <= target and target <= nums[mid]:
			end = mid - 1

		# target in right?
		else:
			start = mid + 1

	# move left and right to include all occurences of target
	i, j = index, index
	while i > 0 and nums[i-1] == target:
		i -= 1
	while j < len(nums)-1 and nums[j+1] == target:
		j += 1

	return [i, j]


def solution1(A):
	"""
	Microsoft OTS: fix bug return the smallest element from array

	"""
	# before:
	# ans = 0
	# after:
	ans = A[0]  # should start from 0th element
	for i in range(1, len(A)):
	    if A[i] < ans:
	        ans = A[i]
	return ans


def solution2(A):
	"""
	Microsoft OTS: 
	Return 0 if there's a 0
	Return 1 if sum is positive
	Return -1 if sum is negative
	"""
	# neg_counter
	neg_counter = 0
	# loop through all elements
	for i in range(len(A)):
		# if i is 0: return 0
		if A[i] == 0:
			return 0

		# if neg num: add to neg_counter
		if A[i] < 0:
			neg_counter += 1

	# if neg_counter is even return 1 else -1
	return 1 if neg_counter % 2 == 0 else -1


def sort_colors(nums):
	"""
	Sort the colors red, white, and blue. Where each color has the value 0,1,2
	respectively. 
	"""
	red, white, blue = 0, 0, len(nums)-1

	while white <= blue:
	    if nums[white] == 0:
	        nums[red], nums[white] = nums[white], nums[red]
	        white += 1
	        red += 1
	    elif nums[white] == 1:
	        white += 1
	    else:
	        nums[white], nums[blue] = nums[blue], nums[white]
	        blue -= 1


def storage(n, m, h, v):
	"""
	Amazon online assessment
	Amazon is experimenting with a flexible storage system for their 
	warehouses. The storage unit consists of a shelving system which 
	is one meter deep with removable vertical and horizontal separators.
	When all separators are installed, each storage space is 
	one cubic meter (1'x1'x1'). 

	n: horizontal separators
	m: vertical separator
	h: horizontals to be removed
	v: verticals to be be removed
	return: 
		the volume of the alrgest space when a series of 
		horizontal and vertical separators are removed.
	complexity:
		time: O(N)
		space: O(N)
	"""
	max_h_gap = 0
	max_v_gap = 0

	# convert list to set for O(1) lookup time
	h = set(h)
	v = set(v)

	# store max h gap
	h_gap = 1
	for i in range(n+1):
		# if gap increment space
		if i in h:
			h_gap += 1
		# if not gap, reset
		else: 
			h_gap = 1

		max_h_gap = max(max_h_gap, h_gap)

	# store max v gap
	v_gap = 1
	for i in range(m+1):
		if i in v:
			v_gap += 1
		else:
			v_gap = 1
		max_v_gap = max(max_v_gap, v_gap)


	# return max_h_gap * max_v_gap
	return max_h_gap * max_v_gap


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


def sum_zero(n):
	"""
	Add n elements in array where their sum must be 0
	n:
		integer number that defines the number of elements
	return:
		list containing n elements that add up to zero
	complexity:
		time: O(N)
		space: O(N)
	"""
	a = []
	num = n
	# if n and odd:
	if num and num%2 == 1:
		# add 0 to array
		a.append(0)
		# make num even
		num -= 1

	num //= 2
	# add i, -i to array until n-1
	for i in range(1, num+1):
		a.append(-1*i)
		a.append(i)

	# return a
	return a


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