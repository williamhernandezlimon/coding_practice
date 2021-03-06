#!/usr/bin/env python3

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class NodeBinary:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right

class NodeGraph:
	def __init__(self, data=0, neighbors=None):
		self.data = data
		self.neighbors = neighbors

		