#!/usr/bin/env python3

def get_minimum_number(*numbers):
	minimum = None
	for number in numbers:
		minimum = number if (minimum == None) or number < minimum else minimum
	return minimum