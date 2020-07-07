#!/usr/bin/env python3
from src.data_structure.node import *
from src.data_structure.linked_list import *
from pytest import mark


TEST_REVERSE = [
	([], None),
	(['A', 'B', 'C', 'D', 'E'], ['E', 'D', 'C', 'B', 'A'])
]
@mark.parametrize("test_list, expected_response", TEST_REVERSE)
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


TEST_NUMBERS = [
	([2, 4, 3], [5, 6, 4], 807),
	([2], [5, 2], 27),
	([1, 4], [1], 42)
]
@mark.parametrize("test_number1, test_number2, expected_response", TEST_NUMBERS)
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
	
	ll = LinkedList(Node(list[0]))
	for i in list[1:]:
		add(ll, Node(i))
	return ll

def to_list(ll: LinkedList) -> list:
	l = []
	current = ll.head if ll and ll.head else None
	while current != None:
		l.append(current.data)
		current = current.next
	
	return l