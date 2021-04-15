#!/usr/bin/env python3


def create(rows, columns):
	return [[0] * (columns) for _ in range(rows)]


def draw(table):
	row = 0
	while row < len(table):
		print(table[row])
		row += 1


def set_zeros(matrix):
	"""
	Set correponding row and column to 0, when a given cell is 0
	matrix:
		contains the rows and column, that will be modified
	Complexity:
		Time: O(mxn)
		Space: O(mxn)
	"""
	rows_to_zero = set()
	columns_to_zero = set()

	# store columns and rows that must be modified in a set
	for row in range(len(matrix)):
		for column in range(len(matrix[row])):
			if matrix[row][column] == 0:
				rows_to_zero.add(row)
				columns_to_zero.add(column)

	# use the set to modify corresponding cell
	for row in range(len(matrix)):
		for column in range(len(matrix[row])):
			if row in rows_to_zero or column in columns_to_zero:
				matrix[row][column] = 0


def spiral_order(matrix):
	"""
	Given m x n matrix, return all elements of the matrix 
	in spiral order
	matrix:
		list of list of integers
	return:
		list of integers in spiral order
	complexity:
		time: O(N+M)
		space: O(N+M)
	"""
	order = []
	t, b, l, r = 0, len(matrix)-1, 0, len(matrix[0])-1
	while t <= b and l <= r:
		print(f"t: {t} b: {b} l: {l} r: {r}")
		# go right
		for i in range(t, r+1):
			if matrix[t][i] != None:
				order.append(matrix[t][i])
				matrix[t][i] = None
		# update top
		t += 1

		# go down
		for i in range(t, b+1):
			if matrix[i][r] != None:
				order.append(matrix[i][r])
				matrix[i][r] = None
		# update right
		r -= 1

		# go left
		print(f"going left r: {r} l: {l} b: {b}")
		for i in range(r, l-1, -1):
			if matrix[b][i] != None:
				order.append(matrix[b][i])
				matrix[b][i] = None
		# update bottom
		b -= 1

		# go up
		for i in range(b, t-1, -1):
			if matrix[i][l] != None:
				order.append(matrix[i][l])
				matrix[i][l] = None
		# update left
		l += 1

	return order


def submatrix_sum(matrix, c1, c2):
	"""
	matrix:
		list of list of numbers
	c1:
		tuple representing x,y starting coordinate
	c2:
		tuple representing x,y ending coordinate
	return:
		sum of all values from c1 to c2
	complexity:
		time: O(N^2)
		space: O(1)
	"""
	# check valid y, x are valid
	invalid_coords = c2[0] < 0 or len(matrix) < c2[1] or \
		c1[0] < 0 or len(matrix[0]) < c1[1] or \
		c1[0] > c2[0] or c1[1] > c2[1]

	if invalid_coords:
		return -1		
	if not matrix or not matrix[0]:
		return 0

	# track sub_sum
	sub_sum = 0

	# loop from c1[1] to c2[1] y-axis
	for y in range(c1[1], c2[1]+1):

		# loop from c1[0] to c2[0] x-axis
		for x in range(c1[0], c2[0]+1):
			# add cell value to sum
			print(f"matrix[{y}][{x}]: {matrix[y][x]}")
			sub_sum += matrix[y][x]


	# return sub_sum
	return sub_sum

