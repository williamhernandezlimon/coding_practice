#!/usr/bin/env python3
import logging 
import math

from src.data_structure import table as table_object


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def bfs(graph, start):
	"""
	Graph
	breadth first search
	"""
	explored = []
	queue = [start]

	while queue:
		node = queue.pop(0)
		neighbors = graph[node] if node and node in graph else []

		if node not in explored:
			neighbors = graph[node]
			for neighbor in neighbors:
				queue.append(neighbor)
			explored.append(node)

	return explored


def dfs_iterative(graph, start):
	"""
	Graph
	Depth first search iterative
	"""
	visited = []
	stack = [start]
	while stack:
		parent = stack.pop()
	

		if parent in visited:
			continue
		visited.append(parent)
		neighbors = graph[parent] if parent and parent in graph else []
		for neighbor in neighbors:
			stack.append(neighbor)

	return visited


def dfs_iterative_efficient(graph, start):
	"""
	Graph
	Depth first search iterative
	Removes the inner loop by assigning all neighbors to stack in O(1) time
	"""
	visited = []
	stack = [start]
	while stack:
	    node = stack.pop()
	    if node not in visited:
	        visited += [node]

	        # instead of looping, we append all neighbors
	        stack += graph[node]
	return visited


def dfs_recursive(graph, start, visited):
	"""
	Graph
	Depth first search recursively
	"""
	neighbors = graph[start] if start and start in graph else []
	visited.append(start)

	for neighbor in neighbors:
		if neighbor not in visited:
			dfs_recursive(graph, neighbor, visited)

	return visited
