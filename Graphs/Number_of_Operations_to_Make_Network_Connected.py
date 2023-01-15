"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where
connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other
computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected
computers, and place them between any pair of disconnected computers to make them directly connected.
Return the minimum number of times you need to do this in order to make all the computers connected.
If it is not possible, return -1.

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
"""
from typing import List


def makeConnected(self, n: int, connections: List[List[int]]) -> int:
	# Time = Space = O(n)
	"""
	Logic:
	For n nodes, we need at least n-1 edges make it fully connected. So first we will do DFS and find all the
	disconnected components. Now we have the total edges given as input, and if the total edges is greater than
	or equal to the total given nodes - 1, then we know for sure that we can connect all the nodes, so we return
	total disconnected nodes - 1, else -1
	"""
	# Creating a graph, just like adjacency list.
	graph = {}
	for n1, n2 in connections:
		if n1 not in graph:
			graph[n1] = []
		if n2 not in graph:
			graph[n2] = []
		graph[n1].append(n2)
		graph[n2].append(n1)
	# Tracking visited nodes for finding disconnected components
	visited = set()
	disconnectedComp = 0
	# For each node
	for node in range(n):
		# IF its unvisited
		if node not in visited:
			visited.add(node)
			self.dfs(graph, node, visited)
			# After exploring all the connected nodes, we increase the count by 1
			disconnectedComp += 1
	# Now we have found all the disconnected components, so we will check whether we have enough edges.
	# For given n nodes, we need at least n-1 edges
	if len(connections) >= n - 1:
		# We return the minimum edges required  = total disconnected nodes - 1
		return disconnectedComp - 1
	return -1


def dfs(self, graph, node, visited):
	# Simple DFS
	for child in graph.get(node, []):
		if child not in visited:
			visited.add(child)
			self.dfs(graph, child, visited)
