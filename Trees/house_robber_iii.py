"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.
Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses
in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken
into on the same night.
Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
"""


def rob(root):
	# Time: O(n) and Space: O(d), d = depth
	"""
	Logic:
	At every node, we find the max value by including the current node and excluding the current node.
	And we do this by exploring left and right subtree.
	We return a pair from the function [value by including curr node, value by excluding curr node]
	"""
	return max(solve(root))


def solve(node):
	# Base case
	if not node:
		return 0, 0
	# We explore the left and the right subtree
	# i = root included, x = root excluded
	iLeft, xLeft = solve(node.left)
	iRight, xRight = solve(node.right)

	# Now we compute the sum by including the current node
	withCurrNode = node.val + xLeft + xRight
	# Computing the sum by excluding the current node
	withoutCurrNode = max(iLeft, xLeft) + max(iRight, xRight)
	# Returning both the pairs.
	return withCurrNode, withoutCurrNode
