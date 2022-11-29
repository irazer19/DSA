"""
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others
are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum
node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the
new tree. Return the merged tree.
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
"""


def mergeTrees(root1, root2):
	# Time: O(m + n) and Space: O(d), m, n is the number of nodes in root1 and root2, and d is the depth.
	"""
	Logic:
	We start merging from the root of the trees, we use preorder traversal.
	At each call, we compute the total value for the new node, create the new node and then call the left and right
	branches.
	"""
	# Base base, if both the nodes do not exist, then return None
	if not root1 and not root2:
		return None

	# Computing the total sum for the new node.
	val1 = root1.val if root1 else 0
	val2 = root2.val if root2 else 0
	# Creating a new node.
	node = TreeNode(val1 + val2)
	# Moving to th left by passing the root1 and root2 appropriately
	node.left = mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
	node.right = mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

	return node


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
