#!/usr/bin/env python3


def create(rows, columns):
	return [[0] * (columns) for _ in range(rows)]

def draw(table):
	row = 0
	while row < len(table):
		print(table[row])
		row += 1
