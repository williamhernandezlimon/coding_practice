#!/usr/bin/env python3


def three_sums(nums):
	"""
	Find a list of non-duplicate order of numbers that add up to zero
	nums:
		list of signed integers
	return:
		three numbers that do not add up to zero
	"""
	if not nums or len(nums) < 3:
		return []

	
	
	# store nums in hash_map
	hash_nums = {}
	for num in nums:
		hash_nums[num] = 0

	three_sums = []

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