#!/usr/bin/env python3

class LinkedList:
	def __init__(self, node):
		self.head = node

def add_two_numbers(l1: LinkedList, l2: LinkedList) -> int:
	"""
	Given 2 non-empty linked lists with
	2 non-negative numbers, together is stored a
	reverse orfer number. Add the 2 numbers
	Assume no zeros.

	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8
	Explanation: 342 + 465 = 807

	Time: O(max(l1, l2))
	Space: O(max(l1, l2))
	"""
	n1 = 0
	n2 = 0
	i = 0
	while l1 or l2:
		offset = 10**i if i > 0 else 1
		if l1:
			n1 = (l1.data * offset) + n1
			l1 = l1.next
		if l2:
			n2 = (l2.data * offset) + n2
			l2 = l2.next
		i += 1

	return n1 + n2

def reverse(ll: LinkedList) -> LinkedList:
	"""
	Given a linked list, reverse the entire linked list
	"""
	if not ll:
		return None

	previous = None
	current = ll.head
	nnext = current.next

	while nnext != None:
		current.next = previous
		previous = current
		current = nnext
		nnext = nnext.next
	current.next = previous
	ll.head = current

