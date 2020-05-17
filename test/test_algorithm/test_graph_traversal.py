#!/usr/bin/env python3
from src.algorithm.graph_traversal import *
from pytest import mark


def create_graph():
	return {
		"a": ["b", "s"],
		"b": ["a"],
		"c": ["d", "e", "f"],
		"d": ["c"],
		"e": ["c", "h"],
		"f": ["c", "g"],
		"g": ["s", "f"],
		"h": ["e", "g"],
		"s": ["c", "g"]
	}

def test_bfs():
	graph = create_graph()
	response = bfs(graph, 'a')
	expected_response = ['a', 'b', 's', 'c', 'g', 'd', 'e', 'f', 'h']

	assert response == expected_response

def test_dfs():
	graph = create_graph()
	iterative_response = dfs_iterative(graph, 'a')
	iterative_efficient_response = dfs_iterative_efficient(graph, 'a')
	recursive_response = dfs_recursive(create_graph(), 'a', [])

	expected_iterative_response = ['a', 's', 'g', 'f', 'c', 'e', 'h', 'd', 'b']
	expected_recursive_response = ['a', 'b', 's', 'c', 'd', 'e', 'h', 'g', 'f']

	assert iterative_response == expected_iterative_response
	assert iterative_efficient_response == expected_iterative_response
	assert recursive_response == expected_recursive_response
