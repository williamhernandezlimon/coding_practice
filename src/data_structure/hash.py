#!/usr/bin/env python3

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
