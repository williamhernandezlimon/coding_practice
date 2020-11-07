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