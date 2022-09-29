"""
You're given the root node of a binary tree. Write a function that returns true if this Binary Tree is height
balanced and false if it isn't.
A binary tree is height balanced if for each node in the tree, the difference between the height of its left subtree
and the height of its right subtree is at most 1.

"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    # Time: O(n) and Space: O(h), h is the height of the tree.
    """
    Logic:
    Let's do simply Inorder traversal, at every node, we get the height of the left subtree and the right subtree,
    and then we check whether the absolute difference between them is greater than 1, if yes then we return False.
    Else, we return the max height of (left, right) subtree + 1, and also pass "True".
    We add + 1 because when we return to the parent node, we have to also consider current node's edge.
    Basically, we return a tuple like this (max height so far, result)
    """

    result = isBalanced(tree)

    # The index 1 will have the boolean result.
    return result[1]


def isBalanced(node):
    # If None, then return max height as 0, and result as True.
    if not node:
        return 0, True

    # Get the result from left and right subtree.
    leftResult = isBalanced(node.left)
    rightResult = isBalanced(node.right)
    # If the result from above already contains False, then the tree is not balanced, so we directly return False.
    if leftResult[1] is False or rightResult[1] is False:
        return -1, False
    # If the absolute difference between the left subtree and the right subtree is greater than 1, then return False.
    if abs(leftResult[0] - rightResult[0]) > 1:
        return -1, False
    # Else, the current node is balanced, so we return its max height, True
    return max(leftResult[0], rightResult[0]) + 1, True
