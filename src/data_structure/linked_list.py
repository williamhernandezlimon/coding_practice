#!/usr/bin/env python3

class LL:
	def __init__(self, node):
		self.head = node

	def add(self, node):
		current = self.head
		while current.next != None:
			current = current.next
		current.next = node

	def to_array(self):
		array = []
		current = self.head
		while current != None:
			array.append(current.data)
			current = current.next
		
		return array

	def reverse(self):
		previous = None
		current = self.head
		nnext = current.next

		while nnext != None:
			current.next = previous
			previous = current
			current = nnext
			nnext = nnext.next
		current.next = previous
		self.head = current