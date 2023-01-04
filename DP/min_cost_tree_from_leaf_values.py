"""
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.
It is guaranteed this sum fits into a 32-bit integer.

Input: arr = [6,2,4]
Output: 32
Explanation: There are two possible trees shown.
The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.

"""


def mctFromLeafValues(arr) -> int:
	# Time: O(2^n) and Space: O(n)
	"""
	Logic:
	We use dp, from each index we divide in the left and right subtree.
	If there is just one leaf/element left, then we return [leaf value, result]
	Now once we get the return from left and right subtree, we will compute the max leaf value for returning it to
	the next and we will also compute the current cost = left cost + right cost + (left_leaf * right_leaf) and
	we will try to minimize the cost.
	Finally we will return the pair [max leaf value, cost]

	"""
	# We cache the result for the range [start index, end index]
	cache = {}
	result = dfs(arr, 0, len(arr) - 1, cache)
	return result[1]


def dfs(arr, start, end, cache):
	# If the result is already computed
	if (start, end) in cache:
		return cache[(start, end)]
	# Edge case
	if start > end:
		return [1, 0]
	# If its a leaf node
	if start == end:
		return [arr[start], 0]

	# Now we will compute the maxLeaf and cost for the range [start, end]
	maxLeaf, cost = -1, float('inf')
	for i in range(start, end):
		# Left subtreee result
		maxLeafLeft, costLeft = dfs(arr, start, i, cache)
		# Right subtree result
		maxLeafRight, costRight = dfs(arr, i + 1, end, cache)
		# Computing the max leaf value
		maxLeaf = max(maxLeafLeft, maxLeafRight)
		# Computing the current total cost, we also add the cost from the left and right subtree
		currCost = costLeft + costRight + maxLeafLeft * maxLeafRight
		# Minimizing the cost
		cost = min(cost, currCost)
	# Caching the result
	cache[(start, end)] = [maxLeaf, cost]
	return [maxLeaf, cost]
