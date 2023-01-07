"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed
2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from
node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from
that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
"""


def eventualSafeNodes(graph):
	# Time: O(n + nlogn) and Space: O(n)
	"""
	Logic:
	We will do DFS for 0th node. After completing all the child dfs for the current node, we will save the
	result of the current node in dp array.
	DFS call will return a boolean whether the current node is a safe node.

	"""
	# seen array to track cycle in the graph
	seen = [False for _ in range(len(graph))]
	# dp to store the computed result for the nodes
	dp = [None for _ in range(len(graph))]
	# Final result
	result = []
	# For each node
	for node in range(len(graph)):
		# If we dont have the computed result for this only, only then we do DFS
		if dp[node] == None:
			dfs(node, result, dp, seen, graph)

	return sorted(result)


def dfs(node, result, dp, seen, graph):
	# Assuming the current node is a safe node
	safe = True
	# Adding the current node in the recursive path
	seen[node] = True
	for child in graph[node]:
		# If the precomputed result for this child node is False or we have already seen this child before(Cycle)
		# then we break and update the state to False
		if dp[child] == False or seen[child]:
			safe = False
			break
		# If we have already computed the result for this child and its True, then check for the next child
		if dp[child]:
			continue
		# Else, we visit this new child, and if it returns False, then break
		if not dfs(child, result, dp, seen, graph):
			safe = False
			break
	# Storing the computed result for the current node
	dp[node] = safe
	# Removing seen, as its no more in the recursive path
	seen[node] = False
	# If the state of the current node was still True, then we add this node to the result
	if safe:
		result.append(node)
	# Returning the state
	return safe
