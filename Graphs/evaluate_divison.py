"""
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi]
and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer
for Cj / Dj = ?.
Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

"""


def calcEquation(equations, values, queries):
	# Time: O(q * n) and Space: O(n)
	"""
	Logic:
	We can observe that we may have to travel from one letter to another in order to reach the target letter.
	Our source letter will be the numerator and the destination letter will be the denominator.
	Ex: Given [a, b] and [b, c], and we want to compute [a, c], then we must start from a --> b --> c, once we
	have the correct sequence of the letters, we compute the total value.
	"""
	# We create the graph using the letters, where the key is the numerator and values will be the denominator
	graph = {}
	# For each numerator and denominator
	for n, d in equations:
		if n not in graph:
			graph[n] = []
		if d not in graph:
			graph[d] = []
		graph[n].append(d)
		graph[d].append(n)

	# Now we store all the equations to the hashtable for quick lookup
	eqTable = {tuple(equations[i]): values[i] for i in range(len(equations))}
	# Final result
	result = []
	# For each query
	for currNode, dst in queries:
		# We will insert the starting node to the stack
		stack = [currNode]
		# Track the visited nodes
		visited = set()
		# Add the starting node to the visited node
		visited.add(currNode)
		# Storing the result from the dfs
		result.append(dfs(graph, eqTable, currNode, dst, stack, visited))

	return result


def dfs(graph, eqTable, currNode, dst, stack, visited):
	# Edge case: if both the letters are same in the equation, then we return 1 provided the letters are present
	# in out original equation
	if currNode == dst and currNode in graph:
		return 1
	# Exploring all the children node of the given curr node
	for child in graph.get(currNode, []):
		# If the child is not visited
		if child not in visited:
			# We append the child to the path
			stack.append(child)
			# Mark as visited
			visited.add(child)
			# Now if the child is the destination node, then we compute the total and return
			if child == dst:
				# compute result
				return computeTotal(eqTable, stack)
			# Else we make a function call where the child is the current node
			total = dfs(graph, eqTable, child, dst, stack, visited)
			# If the total is not -1, that means we found a valid result, so we return it
			if total != -1:
				return total
			# Else, if we get -1, then we will pop the current child from the stack and move to the next child
			stack.pop()
	# default return
	return -1


def computeTotal(eqTable, stack):
	total = 1
	# For each index
	for i in range(len(stack) - 1):
		# We will get the numerator and denominator from ith and i + 1 index of the stack.
		# we will loopup the value of the equation in the hashtable
		val = eqTable.get((stack[i], stack[i + 1]), None)
		# If we dont find the value, then we can try reversing the equation and check whether its present in the
		# hashtable
		if not val:
			val = 1 / eqTable.get((stack[i + 1], stack[i]), None)
		# Finally, we multiple the current value with the existing value of total
		total *= val
	return total
