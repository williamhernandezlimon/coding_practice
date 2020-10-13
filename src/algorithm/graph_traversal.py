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
	visited = []
	q = [start]
	
	while q:
		# take the front
		parent = q.pop(0)
		if parent in visited:
			continue

		# add to visited
		visited.append(parent)

		# add neighbors to queue
		neighbors = graph[parent] if graph[parent] else []
		q.extend(neighbors)

	return visited


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


def dijkstras(graph, start):
	"""
	graph:
		map where key is the vertex and value is the neighboring vertecies
	start:
		starting vertex of the graph
	return:
		map of distances with shortest distance from the start and
		map of paths of the parents with the shortest distance from the start
	"""
	if len(graph) == 0 or not start: return None, None

	path = {}  # maps the vertecies and their predecessors
	q = {start: 0}  # similar to distances, but only tracks smallest distance
	distances = {start: 0}  # vertices and thier distances

	unvisited = set(graph.keys())
	while unvisited:
		# get the vertex with the smallest value
		vertex, distance = _pop_min_map_value(q)

		# set the distances to that vertex
		distances[vertex] = distance

		# remove vertex from unvisited
		unvisited.remove(vertex)

		for neighbor in graph[vertex]:

			# if neighbor is unvisited, relax
			if neighbor in unvisited:
				alt_distance = distances[vertex] + graph[vertex][neighbor]

				if alt_distance < q.get(neighbor, float("inf")):
					# set min in q and path
					q[neighbor] = alt_distance
					path[neighbor] = vertex

	return distances, path


def _pop_min_map_value(q):
	"""
	Given a map of key,values return the key,value
	with the smallest value
	q:
		map of key, values
	return:
		return smallest map key, value
	"""
	min_vertex = None
	min_distance = float("inf")
	for vertex in q:
		if q[vertex] < min_distance:
			min_vertex = vertex
			min_distance = q[vertex]

	if min_vertex in q:
		del q[min_vertex]

	return min_vertex, min_distance

