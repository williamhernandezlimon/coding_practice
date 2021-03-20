#!/usr/bin/env python3


def divide(dividend, divisor):
	"""
	Divide without using multiplication, division, or mod
	TODO: update using bit-shifting
	dividend:
		integer numerator
	divsor:
		integer denominator
	complexity:
		time: O(N)
		space: O(1)
	"""
	n, i = divisor, 0

	if dividend > 0:
		if divisor > 0:
			while n <= dividend:
				n += divisor
				i += 1
		elif divisor < 0:
			# make divisor positive
			divisor = abs(divisor)
			n = divisor
			while n <= dividend:
				n += divisor
				i -= 1
		else:
			return None
	elif dividend < 0:
		# make divisor negative
		j = 0
		while j < 2:  
			n -= divisor
			j += 1

		if divisor > 0:
			while n >= dividend:
				n -= divisor
				i -= 1
		elif divisor < 0:
			divisor = abs(divisor)
			dividend = abs(dividend)
			while n <= dividend:
				n += divisor	
				i += 1
		else:
			return None
	else:
		return 0

	return i


def target_sum(l, target):
	"""
		l: the list containing unsigned
		target_number: two values from list should add to target_number

		return True if 2 numbers add up to target_number

		run time: O(n^2)
		# Todo: use dynamic programming to acheive O(nxm) where m is the enumeration(target)
	"""
	# store all value in hash-map for constant lookups
	d = {}
	for n in l:
		# check for duplicates
		if n in d:
			d[n] = d[n] + 1
		else:
			d[n] = 1 

	for n in l:
		new_target = target - n
		if new_target in d: 
			return [n, new_target]

	return None
