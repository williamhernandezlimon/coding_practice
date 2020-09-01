#!/usr/bin/env python3


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


