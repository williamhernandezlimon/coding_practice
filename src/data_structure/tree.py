#!/usr/bin/env python3
import logging 

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def max_depth(root):
	"""
	Returns the max depth of a binary tree
	"""
	if root == None: return 0
	else:
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

		# print(f"root1.value: {root1.value} root2.value: {root2.value}")
		if root1 != root2:
			return False
		
		# Note: appending as mirror image
		stack1.append(left1)
		stack1.append(right1)

		stack2.append(right2)
		stack2.append(left2)
		

	return True