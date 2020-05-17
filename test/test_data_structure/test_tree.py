#!/usr/bin/env python3
from src.data_structure.node import *
from src.data_structure.tree import *
from pytest import mark


def create_tree():
	"""
	    3
	   / \
	  9  20
	    /  \
	   15   7

	"""
	left_leaf = NodeBinary(15, None, None)
	right_leaf = NodeBinary(7, None, None)
	left_leaf = NodeBinary(9, None, None)
	right_leaf = NodeBinary(20, left_leaf, right_leaf)
	
	root = NodeBinary(3, left_leaf, right_leaf)
	return root

def create_tree_symmetric():
	"""
	    1
	   / \
	  2   2
	 / \\ / \
	3  4 4  3
	"""
	right_leaf_2 = NodeBinary(3, None, None)  # level 2
	left_leaf_2 = NodeBinary(4, None, None)
	left_leaf_1 = NodeBinary(2, left_leaf_2, right_leaf_2)  # level 1

	right_leaf_2 = NodeBinary(4, None, None)
	left_leaf_2 = NodeBinary(3, None, None)
	right_leaf_1 = NodeBinary(2, left_leaf_2, right_leaf_2)
	
	root = NodeBinary(1, left_leaf_1, right_leaf_1)	
	return root

def create_tree_asymmetric():
	"""
	    1
	   / \
	  2   2
	   \\  \
	   3    3
	"""
	right_leaf = NodeBinary(3, None, None)
	left_leaf = NodeBinary(2, None, right_leaf)
	right_leaf = NodeBinary(2, None, right_leaf)
	
	root = NodeBinary(1, left_leaf, right_leaf)	
	return root


TEST_MAX_DEPTH = [
	(create_tree(), 3),
	(NodeBinary(7, None, None), 1),
	(None, 0)
]
@mark.parametrize("test_root, expected_response", TEST_MAX_DEPTH)
def test_max_depth(test_root, expected_response):
	response = max_depth(test_root)

	assert response == expected_response


# TEST_IS_SYMMETRIC = [
# 	(create_tree_symmetric(), True),
# 	(create_tree_asymmetric(), False),
# 	(create_tree(), False),
# 	(NodeBinary(7, None, None), True),
# 	(None, True)
# ]
# @mark.parametrize("test_root, expected_response", TEST_IS_SYMMETRIC)
# def test_is_symmetric(test_root, expected_response):
# 	response = is_symmetric_iterative(test_root)

# 	assert response == expected_response



