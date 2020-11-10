#!/usr/bin/env python3
import logging 
import math

from src.data_structure import table as table_object
from src.data_structure import node

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


def clone_graph(start):
	"""
	Runs a bfs on graph, starting from Node "start"
	start:
		type Node which is the starting point to clone the graph
	return:
		cloned graph
	"""
	# TODO: create unit tests
	if node is None: return None

	# cloned map
	# the key will be the original node
	# the value will be the cloned node, with neighbors
	cloned = {node: node.NodeGraph(node.data)}
	q = [node]

	while q:
		node = q.pop()

		# for neighbor in node.neighbors:
		for neighbor in node.neighbors:
			
			# if not visited, then add to visited
			if neighbor not in cloned:
				q.append(neighbor)
				cloned[neighbor] = node.NodeGraph(neighbor.data)
			cloned[node].neighbors.append(cloned[neighbor])

	return cloned[node]


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


def word_search(board, word):
	"""
	Given a 2D board and a word, find if the word exists in the grid.

	The word can be constructed from letters of sequentially adjacent cells, 
	where "adjacent" cells are horizontally or vertically neighboring. 
	The same letter cell may not be used more than once.
	board:
		list of lists, 2d array containing word search
	word:
		the word to be found in the board
	complexity:
		time: O(m*n), due to 
		space: O(m*n), due to recurssion
		where m and n are the rows and columns respectfully
	"""
    # loop through all rows
    for i in range(len(board)):
        # loop through all columns
        for j in range(len(board[i])):
            # if first_element == current_word and _dfs_search(i, j, board, word)
            if word[0] == board[i][j] and _dfs_search(i, j, 0, board, word):
                return True

    # no match found
    return False


def _dfs_search(i, j, word_index, board, word):
    # base case 
    if len(word) == word_index:
        return True


    # check within bounds
    if i < 0 or i >= len(board) or \
        j < 0 or j >= len(board[i]) or \
        word[word_index] != board[i][j]: 
        return False

    # save visited
    saved_char =  board[i][j]

    # mark as visited
    board[i][j] = " "

    # check neighbors
    top = _dfs_search(i + 1, j, word_index + 1, board, word)
    bottom = _dfs_search(i - 1, j, word_index + 1, board, word)
    left = _dfs_search(i, j + 1, word_index + 1, board, word)
    right = _dfs_search(i, j - 1, word_index + 1, board, word)
    if top or bottom or left or right:
    	return True

    # reset to unvisited
    board[i][j] = saved_char

    return False


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

