"""
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one
with headID.
Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th
employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his
direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i]
minutes, all his direct subordinates can start spreading the news).
Return the number of minutes needed to inform all the employees about the urgent news.

Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
Output: 1
Explanation: The head of the company with id = 2 is the direct manager of all the employees in the company and needs
1 minute to inform them all. The tree structure of the employees in the company is shown.
"""
from typing import List


def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
	# Time: O(d), depth of the tree structure and Space: O(n)
	"""
	Logic:
	Since a manager informs all the employees all at once so the time taken is the max of the time taken to inform
	all the direct employees.
	We will do DFS, where we will reach the leaf node and the update the result using max function, if the top
	manager has k children then we will have k leaf nodes, and so the result will be the max of the k chains.
	"""
	# Creating the graph to get all the employees for a manager
	graph = {}
	for i in range(len(manager)):
		m = manager[i]
		if m not in graph:
			graph[m] = []
		graph[m].append(i)
	# Result
	result = Result(0)
	# DFS
	self.dfs(graph, headID, informTime, 0, result)

	return result.time


def dfs(self, graph, currNode, informTime, currTime, result):
	# If we hit a leaf node, where the current node has not children
	if currNode not in graph:
		# We will update the result and return
		result.time = max(result.time, currTime)
		return
	# Else, we will loop over all the child and do DFS
	for child in graph.get(currNode, []):
		# We will pass the total time to reach this child node which is equal to:
		# Time to inform current node + time to inform the current child from the current node.
		self.dfs(graph, child, informTime, currTime + informTime[currNode], result)


class Result:
	def __init__(self, time):
		self.time = time
