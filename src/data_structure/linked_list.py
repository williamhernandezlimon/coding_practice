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


def remove_duplicates(ll: LinkedList) -> LinkedList:
	"""
	Remove duplicates in linked list using a set
	ll:
		linked list of nodes
	complexity:
		time: O(n)
		space: O(n)
	"""
	# empty case
	if not ll or not ll.head: return None

	current = ll.head
	s = {current.data}
	prev = current
	current = current.next
	while current:
		# remove duplicate
		if current.data in s:
			prev.next = current.next
			current = current.next 	
		else:
			# add data set
			s.add(current.data)

			# continue traversing
			prev = prev.next
			current = current.next


def remove_nth_node_from_end(head, n):
	"""
	Remove the nth node from the end of linked list
	head:
		head of linked list, containing first node
	return:
		head to the modified linked list
	complexity:
		time: O(n)
		space: O(1)
	"""
	# walk n steps
	i = 0
	tail = head
	while i < n and tail:
		tail = tail.next
		i += 1

	# n is larger than LL len
	if not tail:
		return head.next

	# walk until end is reached
	prev = head
	while tail.next:
		tail = tail.next
		prev = prev.next

	# remove nth node
	prev.next = prev.next.next


	return head


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

