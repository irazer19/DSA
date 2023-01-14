"""
Find whether the given tree is symmetrical or not.

       1
     /   \
    2     2
   / \   / \
  3  4   4  3

"""


def symmetricalTree(tree):
	# Time = O(n) and Space: O(h)
	"""
	Logic:
	To check symmetrical trees, we will have to compare the first and the last values of the children, so
	we will compare the leftmost with the rightmost, and left.right with the right.left recursively.
	"""
	# Since the root is always symmetrical, we will send the left and right for comparison
	return dfs(tree.left, tree.right)


def dfs(left, right):
	# If left and right values are same, then we will check:
	# leftmost, rightmost and left.right == right.left
	if left and right and left.value == right.value:
		return dfs(left.left, right.right) and dfs(left.right, right.left)
	# Case where if left and right both are None then we return True else False
	return left == right
