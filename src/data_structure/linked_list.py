#!/usr/bin/env python3

class LinkedList:
	def __init__(self, node):
		self.head = node

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

