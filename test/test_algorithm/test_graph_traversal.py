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
TEST_GRAPH_1 = {
	'a': {'b': 1}, 
	'b': {'c': 2, 'b': 5}, 
	'c': {'d': 1}, 
	'd': {}
}
TEST_GRAPH_2 = {
	'a': {'b': 14, 'c': 9, 'd': 7},
	'b': {'a': 14, 'c': 2, 'e': 9},
	'c': {'a': 9, 'b': 2, 'd': 10, 'f': 11},
    'd': {'a': 7, 'c': 10, 'f': 15},
    'e': {'b': 9, 'f': 6},
    'f': {'c': 11, 'd': 15, 'e': 6}
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


TEST_DIJKSTRAS = [
	({}, None, None, None),
	(TEST_GRAPH_1, 'a', {'a': 0, 'c': 3, 'b': 1, 'd': 4}, {'b': 'a', 'c': 'b', 'd': 'c'}),
	(TEST_GRAPH_2, 'a', {'a': 0, 'c': 9, 'b': 11, 'e': 20, 'd': 7, 'f': 20}, {'b': 'c', 'c': 'a', 'd': 'a', 'f': 'c', 'e': 'b'}),
]
@mark.parametrize("test_graph, test_start, expected_response_visited, expected_response_path", TEST_DIJKSTRAS)
def test_dijkstras(test_graph, test_start, expected_response_visited, expected_response_path):
	response_visited, response_path = dijkstras(test_graph, test_start)

	assert response_visited == expected_response_visited
	assert response_path == expected_response_path