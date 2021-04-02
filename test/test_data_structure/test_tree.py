#!/usr/bin/env python3
from src.data_structure.node import *
from src.data_structure.tree import *
from pytest import mark
from sys import stderr


def array_to_tree(l):
	"""
	left = 2 * i + 1
	right = 2 * i + 2
	"""
	# add root to q
	root = NodeBinary(l[0], None, None)
	q = [root]
	i = 0
	# loop while q
	while q:
		# pop parent
		p = q.pop(0)

		# set parent's left/right and add to q
		li = 2 * i + 1  # left index
		lv = l[li] if li < len(l) else None  # left value
		left = NodeBinary(lv, None, None) if lv==0 or lv else None
		if left:
			q.append(left)

		ri = 2 * i + 2  # right index
		rv = l[ri] if ri < len(l) else None  # right value
		right = NodeBinary(rv, None, None) if rv==0 or rv else None
		if right:
			q.append(right)

		if p:
			p.left = left
			p.right = right
		else:
			print("p has no value")
		# increment i
		i += 1

	return root

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


def find_node(root, value):
	# empty root
	if not root:
		return None

	# node found
	if root.value == value:
		return root

	# search left
	node = find_node(root.left, value)

	# search right
	if not node:
		node = find_node(root.right, value)

	return node


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


@mark.parametrize("test_root, expected_response", [
		([3,1,4,3,None,1,5], 4),
		([3,3,None,4,2], 3),
		([9,None,3,6], 1)
	]
)
def test_good_nodes(test_root, expected_response):
	test_root = array_to_tree(test_root)
	response = good_nodes(test_root)

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


@mark.parametrize("test_root, expected_response", [
		(None, []),
		(create_tree(), [[3],[9,20],[15,7]])
		# TODO: 
		# 	input: [1,2,3,4,null,null,5]
		#	output: [[1],[2,3],[4,5]]
	]
)
def test_level_order_list(test_root, expected_response):
	response = level_order_list(test_root)

	assert response == expected_response


@mark.parametrize("test_root, test_k, expected_response", [
		([3,1,4,None,2], 1, 1)
	]
)
def test_kth_smallest(test_root, test_k, expected_response):
	test_tree = array_to_tree(test_root)
	response = kth_smallest(test_tree, test_k)

	assert response == expected_response


@mark.parametrize("test_root, test_p, test_q, expected_response", [
		([3,5,1,6,2,0,8,None,None,7,4], 5, 1, 3),
		([3,5,1,6,2,0,8,None,None,7,4], 5, 4, 5),
		([3,5,1,6,2,0,8,None,None,7,4], 6, 0, 3)
	]
)
def test_lowest_common_ancestor(test_root, test_p, test_q, expected_response):
	test_root = array_to_tree(test_root)
	test_p = find_node(test_root, test_p)
	test_q = find_node(test_root, test_q)

	assert test_root and test_p and test_q, "Invalid test parameters"
	
	response = lowest_common_ancestor(test_root, test_p, test_q)
	assert response and response.value == expected_response


@mark.parametrize("test_nums, expected_response", [
		([-10,-3,0,5,9], [-10, -3, 0, 5, 9])
	]
)
def test_sorted_array_to_bst(test_nums, expected_response):
	root = sorted_array_to_bst(test_nums)

	# helper traversal
	def post_order_traversal(root, response):
		if not root:
			return None
		post_order_traversal(root.left, response)
		response.append(root.value)
		post_order_traversal(root.right, response)

	response = []
	post_order_traversal(root, response)

	assert response == expected_response


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

