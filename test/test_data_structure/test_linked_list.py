#!/usr/bin/env python3
from src.data_structure.node import *
from src.data_structure.linked_list import LL

def create_linked_list():
	n1 = Node('A')
	n2 = Node('B')
	n3 = Node('C')
	n4 = Node('D')
	n5 = Node('E')

	ll = LL(n1)

	ll.add(n2)
	ll.add(n3)
	ll.add(n4)
	ll.add(n5)

	return ll	

def test_reverse():
	"""
	Tests linked list was properly reversed
	"""
	ll = create_linked_list()
	array = ll.to_array()
	ll.reverse()
	array_reverse = ll.to_array()


	front_ptr = 0
	back_ptr = len(array) - 1
	while front_ptr < len(array):
		assert array[front_ptr] == array_reverse[back_ptr]
		front_ptr += 1
		back_ptr -= 1

	# TODO: tests empty linked list and single linked list
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
