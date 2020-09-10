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