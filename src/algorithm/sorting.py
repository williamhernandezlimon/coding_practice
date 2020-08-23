#!/usr/bin/env python3

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


def quicksort(list, low, high):
	"""
	Quicksort algorithm
	list:
		list of numbers that will be sorted
	low:
		index of the beginning of the list
	high:
		index of the end of the list
	"""
	if list and low < high:
		pivot_position = _partition(list, low, high)
		quicksort(list, low, pivot_position-1)
		quicksort(list, pivot_position+1, high)


def mergesort(list):
	"""
	Merge sort algorithm
	list:
		list of numbers that will be sorted
	"""
	if len(list) <= 1:
		return list if list else []

	# split left and right
	middle = len(list) // 2
	left = list[:middle]
	right = list[middle:]
	

	# sort left and right
	mergesort(left)
	mergesort(right)


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
