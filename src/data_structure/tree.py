#!/usr/bin/env python3
import logging 

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def count_nodes(tree_map, start_node):
	"""
	Count the number of nodes, from the starting_node inclusive

	tree_map:
		map of nodes that make a tree
	start_node:
		starting node to count nodes from
	complexity:
		time: O(n)
	"""	
	if not tree_map: return 0

	total = 1
	for node in tree_map.get(start_node, []):
		total += count_nodes(tree_map, node)

	return total


def max_depth(root):
	"""
	Returns the max depth of a binary tree
	"""
	if not root: return 0

	left_depth = 1 + max_depth(root.left)
	right_depth = 1 + max_depth(root.right)

	return max(left_depth, right_depth)


def is_symmetric(root):
	"""
	Returns True if tree is symmetric
	
	[1,2,2,3,4,4,3]



	left_order = 1 2 3 4 2 4 3
	right_order = 1 2 3 4 2 4 3

	"""
	# empty tree
	if not root:
		return True

	# get left order
	left_order = []
	_get_left_order(root, left_order)

	# get right order
	right_order = []
	_get_right_order(root, right_order)
	
	# compare left and right order lists are the same
	print(f"left_order: {left_order} right_order: {right_order}")
	if len(left_order) == len(right_order):
		for i in range(len(left_order)):
			if left_order[i] != right_order[i]:
				return False
		return True

	return False
	

def _get_left_order(node, order):
	if not node:
		order.append(None)
		return None

	order.append(node.value)
	_get_left_order(node.left, order)
	_get_left_order(node.right, order)


def _get_right_order(node, order):
	if not node:
		order.append(None)
		return None

	order.append(node.value)
	_get_right_order(node.right, order)
	_get_right_order(node.left, order)


def in_order_traversal(root):
	if root:
		in_order_traversal(root.left)
		print(root.value)
		in_order_traversal(root.right)


def post_order_traversal(root):
	if root:
		post_order_traversal(root.left)
		post_order_traversal(root.right)
		print(root.value)


def pre_order_traversal(root):
	if root:
		print(root.value)
		pre_order_traversal(root.left)
		pre_order_traversal(root.right)


def level_order_traversal(root):
	queue = [root] if root else []
	while queue:
		leaf = queue.pop(0)
		print(leaf.value)
		
		if leaf.left:
			queue.append(leaf.left)
		if leaf.right:
			queue.append(leaf.right)


def valid_tree(tree_map, root):
	"""
	Check to see the tree is valid; no loops

	tree_map:
		map of nodes that make a tree
	start_node:
		starting node to count nodes from
	visited:
		set(), for constant lookups, used for detecting loops
	complexity:
		time: O(n)
	"""
	if root not in tree_map: return False
	
	visited = set()
	has_no_loops = not(_has_loops(tree_map, root, visited))
	has_no_islands = not(_has_islands(tree_map, root, visited))

	return has_no_loops and has_no_islands


def _has_loops(tree_map, root, visited):
	"""
	tree_map:
		map of nodes that make a tree
	start_node:
		starting node to count nodes from
	visited:
		set(), for constant lookups, used for detecting loops
	"""
	if root not in tree_map: return False
	visited.add(root)
	loop = False
	for child in tree_map[root]:
		if child in visited:
			return True
		loop = _has_loops(tree_map, child, visited)

	return loop


def _has_islands(tree_map, root, visited):
	"""
	tree_map:
		map of nodes that make a tree
	start_node:
		starting node to count nodes from
	visited:
		set(), for constant lookups, used to detect islands
	"""
	for node in tree_map:
		if node not in visited:
			return True

	return False

