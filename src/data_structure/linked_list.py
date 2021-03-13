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


def delete_node(node):
	"""
	Delete the given node. Assume node is not a tail.
	node:
		a node from a LinkedList
	complexity:
		time: O(N)
		space: O(1)
	"""
	if not node or not node.next:
		return None
	node.data = node.next.data
	node.next = node.next.next


def is_palindrome(head):
	"""
	Check if the linked list is a palindrome
	head:
		head of the LinkedList
	complexity:
		time: O(N)
		space: O(1)
	"""
	if not head:
		return False
	if not head.next:
		return True

	# TODO: Update to find middle and reverse at the same time
	# get mid point
	fast = head
	slow = head
	tail = None
	while fast and fast.next:
		fast = fast.next.next
		tail = slow
		slow = slow.next

	# if odd, omit the middle node
	if fast:
		slow = slow.next

	# detach and create 2 linked lists
	new_head = slow
	tail.next = None

	# reverse first half unitl tail
	prev = None
	curr = head
	while curr:
		# set next
		nxt = curr.next
		# curr.next = prev
		curr.next = prev
		# move prev
		prev = curr
		# move curr
		curr = nxt
	head = prev

	# check first half is the same as second half
	while head and new_head:
		if head.data != new_head.data:
			return False
		
		head = head.next
		new_head = new_head.next

	return not head and not new_head


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

