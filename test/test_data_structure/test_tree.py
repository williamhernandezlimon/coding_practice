#!/usr/bin/env python3
from src.data_structure.node import *
from src.data_structure.tree import *
from pytest import mark
from sys import stderr

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
	
	right_leaf = NodeBinary(20, left_leaf, right_leaf)
	left_leaf = NodeBinary(9, None, None)
	
	
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



@mark.parametrize(
	"test_tree, test_node, expected_response", [
		({}, 1, 0),
		# ({1: []}, 2, 0),
		({1: []}, 1, 1),
		# ({1: [2]}, 3, 0),
		({1: [2]}, 1, 2),
		({1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, 2, 3),
		({1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, 1, 5)
	]
)
def test_count_nodes(test_tree, test_node, expected_response):
	response = count_nodes(test_tree, test_node)

	assert response == expected_response


@mark.parametrize(
	"test_root, expected_response", [
		(create_tree(), 3),
		(NodeBinary(7, None, None), 1),
		(None, 0)
	]
)
def test_max_depth(test_root, expected_response):
	response = max_depth(test_root)

	assert response == expected_response


@mark.parametrize(
	"test_root, expected_response", [
		(create_tree_symmetric(), True),
		(create_tree_asymmetric(), False),
		(create_tree(), False),
		(NodeBinary(7, None, None), True),
		(None, True)
	]
)
def test_is_symmetric(test_root, expected_response):
	# response = is_symmetric_iterative(test_root)

	# assert response == expected_response

	response = is_symmetric(test_root)
	assert response == expected_response


@mark.parametrize(
	"test_tree, expected_response", [
		(None, ''),
		(create_tree(), "9\n3\n15\n20\n7\n")
	]
)
def test_in_order_traversal(capsys, test_tree, expected_response):
	in_order_traversal(test_tree)
	captured = capsys.readouterr()

	assert captured.out == expected_response


@mark.parametrize(
	"test_tree, expected_response", [
		(None, ''),
		(create_tree(), "9\n15\n7\n20\n3\n")
	]
)
def test_post_order_traversal(capsys, test_tree, expected_response):
	post_order_traversal(test_tree)
	captured = capsys.readouterr()

	assert captured.out == expected_response


@mark.parametrize(
	"test_tree, expected_response", [
		(None, ''),
		(create_tree(), "3\n9\n20\n15\n7\n")
	]
)
def test_pre_order_traversal(capsys, test_tree, expected_response):
	pre_order_traversal(test_tree)
	captured = capsys.readouterr()

	assert captured.out == expected_response


@mark.parametrize(
	"test_tree, expected_response", [
		(None, ''),
		(create_tree(), "3\n9\n20\n15\n7\n")
	]
)
def test_level_order_traversal(capsys, test_tree, expected_response):
	level_order_traversal(test_tree)	
	captured = capsys.readouterr()

	assert captured.out == expected_response


@mark.parametrize("test_tree_map, test_root, expected_response", [
		({}, 1, False),  # empty map
		({1: [2]}, 1, True),
		({1: [2], 3: {}}, 1, False),  # has island
		({1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, 1, True),
		({1: [2, 3], 2: [4, 5], 3: [1], 4: [], 5: []}, 1, False)  # check loop
	]
)
def test_valid_tree(test_tree_map, test_root, expected_response):
	response = valid_tree(test_tree_map, test_root)

	assert response == expected_response

