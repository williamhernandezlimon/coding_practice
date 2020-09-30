#!/usr/bin/env python3


def heap_sort(list):
	"""
	Heap sort algorithm
	list:
		the list of numbers to be sorted
		DOES NOT SUPPORT duplicates
	complexity:
		time: O(nlogn)
		space: O(n)
	"""
	# build max heap
	length = len(list)
	i = length // 2  # starting from the middle works more effeciently
	while i >= 0:
		_max_heapify(list, length, i)
		i -= 1

	# extract max element and re-heapify
	i = length - 1
	while i > 0:
		list[0], list[i] = list[i], list[0]
		_max_heapify(list, i, 0)
		i -= 1


def insertion_sort(list):
	"""
	Insertion sort algorithm
	list:
		list of numebers which will be sorted
	complexity:
		time: O(n^2)
		space: O(n)
	"""
	i = 1
	while i < len(list):
		j = i - 1
		current_value = list[i]
		while j >= 0 and list[j] >= current_value:
			# shift values +1 and swap with current value
			list[j+1], list[j] = list[j], current_value
			j -= 1
			
		i += 1


def merge_sort(list):
	"""
	Merge sort algorithm
	list:
		list of numbers that will be sorted
	complexity:
		time average, best, & worst: O(nlogn)
		space:O(n)
	"""
	if len(list) <= 1:
		return list if list else []

	# split left and right
	middle = len(list) // 2
	left = list[:middle]
	right = list[middle:]
	

	# sort left and right
	merge_sort(left)
	merge_sort(right)


	# merge left and right
	i = j = k = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			list[k] = left[i]
			i += 1
		else:
			list[k] = right[j]
			j += 1
		k += 1

	# merge unvisted elements
	while i < len(left):
		list[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		list[k] = right[j]
		j += 1
		k += 1


def quick_sort(list, low, high):
	"""
	Quicksort algorithm
	list:
		list of numbers that will be sorted
	low:
		index of the beginning of the list
	high:
		index of the end of the list
	complexity:
		time average & best: O(nlogn)
		time worse: O(n^2)
		space: O(n)
	"""
	if list and low < high:
		pivot_position = _partition(list, low, high)
		quick_sort(list, low, pivot_position-1)
		quick_sort(list, pivot_position+1, high)


def selection_sort(list):
	"""
	Selection sort algorithm
	list:
		list of numbers that will be sorted
	complexity:
		best, average, & worst: O(n^2)
	"""
	for i in range(len(list)):
		minimum_index = i
		for j in range(i+1, len(list)):
			if list[minimum_index] > list[j]:
				minimum_index = j
		
		list[i], list[minimum_index] = list[minimum_index], list[i]


def _max_heapify(list, length, parent_pos):
	"""
	Max heapify sets parent_pos to be the largest item 
		if parent_pos is not originally the largest, 
		then a swap is performed and is re-heapified
	Once parent_pos is the largest item, heap_sort can extract it later
	"""
	# set left and right
	left_pos = 2*parent_pos + 1
	right_pos = 2*parent_pos + 2

	max_position = parent_pos
	# if left child exists and is bigger
	if left_pos < length and list[parent_pos] < list[left_pos]:
		max_position = left_pos

	# if right child exists and is bigger
	if right_pos < length and list[max_position] < list[right_pos]:
		max_position = right_pos

	# if root is not max, swap and re-heapify
	if max_position != parent_pos:
		list[parent_pos], list[max_position] = list[max_position], list[parent_pos]
		_max_heapify(list, length, max_position)
		

def _partition(list, low, high):
	"""
	Only used in quicksort.
	Selects pivot to be the last element
	Places smaller and larger numbers, to the pivot, on the left and right respectively
	list:
		list of numbers that will be re-placed
	low:
		index of the beginning of the list
	high:
		index of the end of the list
	return:
		Postition of the pivot
	"""
	# use the last element as the pivot
	pivot = list[high]
	
	# i must be at least 1 position behind j
	i = low -  1 

	for j in range(low, high):
		# swap
		if list[j] <= pivot:
			i += 1

			# swap i & j
			list[j], list[i] = list[i], list[j]

	# move pivot to the middle
	list[i+1], list[high] = list[high], list[i+1]


	return i+1