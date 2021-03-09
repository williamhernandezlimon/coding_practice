#!/usr/bin/env python3
import logging 
from src.data_structure.node import *


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
	"""
	# empty tree
	if not root:
		return True

	# helper method
	def _is_mirror(node1, node2):
		# empty case
		if not node1 or not node2:
			return node1 == node2

		if node1.value != node2.value:
			return False

		return _is_mirror(node1.left, node2.right) and \
			_is_mirror(node1.right, node2.left)

	return _is_mirror(root.left, root.right) and \
		 _is_mirror(root.right, root.left)


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


def level_order_list(root):
	"""
	    3
	   / \
	  9  20
	/   /  \
   3   15   7
	"""
	# base case: empty root
	if not root:
		return []

	# track of q
	q = [root]
	# track of levels
	levels = [[root.value]]

	# loop while q not empty
	while q:
		# get level and size of q
		level = []
		parent_count = len(q)

		# traverse to get children for all parents
		for i in range(parent_count):
			# get parent
			parent = q.pop(0)

			# add children to q and level
			left = parent.left if parent and parent.left else None
			if left:
				q.append(left)
				level.append(left.value)

			right = parent.right if parent and parent.right else None
			if right:
				q.append(right)
				level.append(right.value)

		# add level to levels, only non-empty level
		if level:
			levels.append(level)

	# return levels
	return levels


def kth_smallest(root, k):
	"""

	"""
	# traverse to the very left before decrementing
	# keep track of decrementing k
	# keep track of current node
	values = []
	def traverse(root, values):
		# base case
		if not root:
			return None
		# go left
		if root.left:
			traverse(root.left, values)
		
		# track values
		values.append(root.value)

		# go right
		if root.right:
			traverse(root.right, values)

	traverse(root, values)
	kth = values[k-1] if k >= 0 else None
	
	return kth
def sorted_array_to_bst(nums):
	"""
	Convert array to BST
	Complexity:
		time: O(n)
		space: O(n)
	"""
	if not nums:
		return None

	mid = len(nums) // 2
	left = sorted_array_to_bst(nums[0:mid])
	right = sorted_array_to_bst(nums[mid+1:])

	return NodeBinary(nums[mid], left, right)
	 	

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

