"""
Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list
and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
"""


def flattenInPreorderTraversalForm(root) -> None:
	# Time: O(n) and Space: O(d)
	"""
	Do not return anything, modify root in-place instead.
	Logic:
	Since we have to create a linked list in the preorder traversal format, we will do iterative preorder traversal.
	To mutate the root, we will create a prev variable which will hold the last node in our result linked list.
	As we pop nodes, we will connect the new node with the prev node.
	"""
	# Edge case
	if not root:
		return root
	# Edge case
	if not root.left and not root.right:
		return root

	# Variable to store the last node in the resultant list
	prev = None
	# Iterative preorder traversal
	stack = [root]
	while stack:
		# Current node from the stack.
		currNode = stack.pop()
		# Storing the right, left nodes according to their visit time of preorder traversal.
		if currNode.right:
			stack.append(currNode.right)
		if currNode.left:
			stack.append(currNode.left)
		# If this is the root node, then we initialize prev with it.
		if not prev:
			prev = currNode
		else:
			# Else, we will convert to a linked list, left becomes null and prev.right points to the current node.
			prev.left = None
			prev.right = currNode
			prev = prev.right
