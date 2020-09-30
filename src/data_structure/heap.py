#!/usr/bin/env python3

def heap_max(a):
	"""
	Builds a max heap using the existing list "a"
	Where parent's index is 0 is larger than all children. And left and right are 
	(parent*2 + 1) and (parent*2 + 2) respectively 
	a:
		list of elements to be converted into a max heap
	complexity:
		time: O(nlog(n))
		space: O(1)
	"""
	# last non-leaf node is: len(a)//2 - 1
	for i in range(len(a)//2 -1, -1, -1):
		_heapify_max(a, i)


def heap_min(a):
	"""
	Builds a min heap using the existing list "a"
	Where parent's index is 0 is smaller than all children. And left and right are 
	(parent*2 + 1) and (parent*2 + 2) respectively 
	a:
		list of elements to be converted into a min heap
	complexity:
		time: O(nlog(n))
		space: O(1)
	"""
	for i in range(len(a)//2 -1, -1, -1):
		_heapify_min(a, i)


def _heapify_max(a, parent_pos):
	left = (parent_pos * 2) + 1
	right = (parent_pos * 2) + 2

	max_pos = parent_pos
	# check left leaf
	if left < len(a) and a[max_pos] < a[left]:
		max_pos = left
	# check right leaf
	if right < len(a) and a[max_pos] < a[right]:
		max_pos = right

	# update if parent is not largest and heapify
	if max_pos != parent_pos:
		print(f"swapping a[max_pos]: {a[max_pos]} a[parent_pos]: {a[parent_pos]}")
		a[max_pos], a[parent_pos] = a[parent_pos], a[max_pos]
		_heapify_max(a, max_pos)


def _heapify_min(a, parent_pos):
	left = (2*parent_pos) + 1 if (2*parent_pos) + 1 < len(a) else None
	right = (2*parent_pos) + 2 if (2*parent_pos) + 2 < len(a) else None
	min_pos = parent_pos

	# check left leaf for min
	if left and a[left] < a[parent_pos]:
		min_pos = left
	
	# check right leaf for min
	if right and a[right] < a[min_pos]:
		min_pos = right

	# update parent if not largest and heapify
	if parent_pos != min_pos:
		a[parent_pos], a[min_pos] = a[min_pos], a[parent_pos]
		_heapify_min(a, min_pos)

