"""
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique
values from 1 to n. Return the answer in any order.
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

You have to return list tree node objects.
"""


def generateTrees(n: int):
	# Time: O(Catalan number)
	"""
	Logic:
	We will take n, and create an array of all the numbers from 1 to n.
	Next, we will loop over the array, and treat every element as the root node, and then call left and right
	function with the given start and end index range. The function call will return a list of all the possible
	trees which we will combine using for-loop where the current index is the root node. We will add this tree
	to the result list and return it recursively.
	"""
	# Representing all the nodes of the tree starting from 1 to n
	nums = [i for i in range(1, n + 1)]
	# Also passing the start and end range
	return getTrees(nums, 0, len(nums) - 1)


def getTrees(nums, start, end):
	# Base case,
	if start > end:
		# We return a list
		return [None]
	# To store all the newly created trees
	totalTrees = []
	# For each item in the given range
	for i in range(start, end + 1):
		# Getting the left and the right trees
		leftTrees = getTrees(nums, start, i - 1)
		rightTrees = getTrees(nums, i + 1, end)
		# Since the result from above is a list, we will loop over to get all the configurations.
		for l in leftTrees:
			for r in rightTrees:
				# Creating a tree where the current ith element is the root node.
				root = TreeNode(nums[i])
				root.left = l
				root.right = r
				# Appending this tree to the result.
				totalTrees.append(root)
	# Returning the list
	return totalTrees


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
