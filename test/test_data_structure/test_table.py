#!/usr/bin/env python3
from src.data_structure import table
from pytest import mark


@mark.parametrize(
	"test_matrix, expected_response", [
		([], []),
		([[1]], [[1]]),
		([[0]], [[0]]),
		([[1,1,1], [1,0,1], [1,1,1]], [[1,0,1], [0,0,0], [1,0,1]]),
		([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]])
	]
)
def test_set_zeros(test_matrix, expected_response):
	table.set_zeros(test_matrix)

	assert test_matrix == expected_response


@mark.parametrize("test_matrix, expected_response", [
		([[2,5],[8,4],[0,-1]], [2,5,4,-1,0,8]),
		([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
		([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
		([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10])
	]
)
def test_sprial_order(test_matrix, expected_response):
	response = table.spiral_order(test_matrix)

	assert response == expected_response


@mark.parametrize("test_matrx, test_c1, test_c2, expected_response", [
		(
			[
				[1,2,3],
				[4,5,6],
				[7,8,9]
			], (0,0), (2,2), 45
		),
		(
			[
				[1,2,3],
				[4,5,6],
				[7,8,9]
			], (0,0), (0,0), 1
		),
		(
			[
				[1,2,3],
				[4,5,6],
				[7,8,9]
			], (1,1), (2,2), 28
		),
		(
			[[]], (1,1), (5,5), -1
		),
		(
			[[]], (0,0), (0,0), 0
		),
		(
			[
				[1,2,3,4,5],
				[1,1,2,3,2],
				[1,3,4,2,0],
				[2,1,1,3,4]
			], (1,2), (3,3), 14
		)
	]
)
def test_submatrix_sum(test_matrx, test_c1, test_c2, expected_response):
	response = table.submatrix_sum(test_matrx, test_c1, test_c2)

	assert response == expected_response

