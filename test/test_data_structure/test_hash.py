#!/usr/bin/env python3
from src.data_structure.hash import *
from pytest import mark


@mark.parametrize(
	"test_l, test_target, expected_response", [
		([], 7, None),
		([1], 7, None),
		([2,3], 1, None),
		([2,3], 0, None),
		([2,2], 4, [2,2]),
		([1,1,1,1,1], 7, None),
		([1,2,3,4,5], 7, [2, 5])
	]
)
def test_target_sum(test_l, test_target, expected_response):
	response = target_sum(test_l, test_target)

	assert response == expected_response