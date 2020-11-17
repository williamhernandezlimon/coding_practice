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


def is_symmetric_iterative(root):
	"""
	Returns True if tree is symmetric
	"""
	# empty tree
	if root == None: return True

	# root will be traversed concurrently
	root1 = root
	root2 = root

	stack1 = []
	stack2 = []
	stack1.append(root1)
	stack2.append(root2)
	while stack1 and stack2:
		root1 = stack1.pop()
		root2 = stack2.pop()
		if root1 != None:
			left1 = root1.left
			right1 = root1.right
			root1 = root1.value
		if root2 != None:
			left2 = root2.left
			right2 = root2.right
			root2 = root2.value

		if root1 != root2:
			return False
		
		# Note: appending as mirror image
		stack1.append(left1)
		stack1.append(right1)

		stack2.append(right2)
		stack2.append(left2)
		

	return True


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

