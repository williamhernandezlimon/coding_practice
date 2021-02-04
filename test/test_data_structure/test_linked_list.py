#!/usr/bin/env python3
from src.data_structure.node import *
from src.data_structure.linked_list import *
from pytest import mark


@mark.parametrize("test_list, expected_response", [
		([], None),
		(['A', 'B', 'C', 'D', 'E'], ['E', 'D', 'C', 'B', 'A'])
	]
)
def test_reverse(test_list, expected_response):
	"""
	Tests linked list was properly reversed
	"""
	# TODO: tests empty linked list and single linked list
	ll = create_linked_list(test_list)
	list = to_list(ll)
	reverse(ll)
	list_reverse = to_list(ll)

	front_ptr = 0
	back_ptr = len(list) - 1
	while front_ptr < len(list):
		assert list[front_ptr] == list_reverse[back_ptr]
		front_ptr += 1
		back_ptr -= 1

@mark.parametrize(
		"test_list, expected_response", [
		([], None),
		([1, 2, 3], [1, 2, 3]),
		([1, 2, 3, 1, 1, 1], [1, 2, 3]),
		([1, 2, 3, 1, 1, 1], [1, 2, 3]),
		([1, 1, 2, 2, 3, 3], [1, 2, 3]),
	]
)
def test_remove_duplicates(test_list, expected_response):
	ll1 = create_linked_list(test_list)
	# TODO: data doesn't have to be a linked
	ll2 = create_linked_list(expected_response)
	
	remove_duplicates(ll1)

	# use pointers to check data valid
	p1 = ll1.head if ll1 else None
	p2 = ll2.head if ll2 else None

	while p1 and p2:
		assert p1.data == p2.data
		p1 = p1.next
		p2 = p2.next
	
	assert not p1 and not p2


@mark.parametrize("test_ll_list, test_n, expected_response", [
		([1,2,3,4,5], 2, [1,2,3,5]),
		([1, 2], 1, [1]),
		([1], 1, []),
	]
)
def test_remove_nth_node_from_end(test_ll_list, test_n, expected_response):
	test_head = create_linked_list(test_ll_list).head
	test_head = remove_nth_node_from_end(test_head, test_n)

	i = 0
	while test_head and i < len(expected_response):
		assert test_head.data == expected_response[i]
		i += 1
		test_head = test_head.next

	assert test_head == None and i == len(expected_response)


@mark.parametrize("test_number1, test_number2, expected_response", [
		([2, 4, 3], [5, 6, 4], 807),
		([2], [5, 2], 27),
		([1, 4], [1], 42)
	]
)
def test_add_two_numbers(test_number1, test_number2, expected_response):
	ll1 = create_linked_list(test_number1)
	ll2 = create_linked_list(test_number2)
	response = add_two_numbers(ll1.head, ll2.head)

	assert response == expected_response


### helper functions below ###
def add(ll: LinkedList, node: Node) -> LinkedList:
	current = ll.head
	while current.next != None:
		current = current.next
	current.next = node

def create_linked_list(list: LinkedList) -> LinkedList:
	if not list: 
		return None
	assert len(list) > 0, "The array cannot be empty."
	
	head = LinkedList(Node(list[0]))
	for i in list[1:]:
		add(head, Node(i))
	return head

def to_list(ll: LinkedList) -> list:
	l = []
	current = ll.head if ll and ll.head else None
	while current != None:
		l.append(current.data)
		current = current.next
	
	return l