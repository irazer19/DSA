"""
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember
every pair of adjacent elements in nums. You are given a 2D integer array adjacentPairs of size n - 1 where each
adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.
Return the original array nums. If there are multiple solutions, return any of them.

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.

"""


def restoreArray(adjacentPairs):
	# Time = Space: O(n)
	"""
	Logic:
	First lets create a graph using dictionary, where for each number we will store all its adjacent numbers.
	Next, we want to do DFS from the number which has only 1 adjacent element because it will either be the start or
	end of the result. There will exactly be two numbers which have only 1 adjacent element, first and the last
	element of the result.

	In DFS, we will simply add the current number in the result and then loop over the children and explore their
	adjacent numbers from the graph we created.

	"""
	# Stores all the adjacent numbers for each number
	table = {}
	for i, j in adjacentPairs:
		if i not in table:
			table[i] = []
		if j not in table:
			table[j] = []
		table[i].append(j)
		table[j].append(i)
	# For each unique number
	for node in list(table.keys()):
		# To store the result of DFS
		stack = []
		# Tracking the visited nodes
		visited = set()
		# If this element has only 1 adjacent element, meaning its either the first or last element in the result.
		if len(table.get(node, [])) == 1:
			# Doing DFS
			dfs(table, node, stack, visited)
			# Returning the result
			return stack


def dfs(table, node, stack, visited):
	# Mark as visited
	visited.add(node)
	# Adding to result
	stack.append(node)
	# For adjacent numbers to the current number
	for nextNode in table[node]:
		# If we have not visited it
		if nextNode not in visited:
			# DFS again
			dfs(table, nextNode, stack, visited)
