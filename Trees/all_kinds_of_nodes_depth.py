"""
The distance between a node in a binary tree and the tree's root is called the node's depth.
Write a function that takes in binary tree and returns the sum of all of its subtree's nodes depths.

"""


def allKindsOfNodeDepths(root):
    # Time: O(n) and Space: O(h)
    """
    Logic:
    Here we find the distance of a node from all its parent nodes, which means that for a given node at depth d,
    we find the sum of natural numbers till depth d.
    Now explore left subtree and right subtree, the return from them is the sum of all the node's distance from their
    parent nodes.
    So we return:
    (Sum of all left subtree nodes from all parents +
    Sum of all right subtree nodes from all parents +
    Sum of current nodes distance from all its parents)
    """
    # Using DFS
    return dfs(root, 0)


def dfs(node, depth):
    # If node is None, return 0
    if not node:
        return 0
    # Explore left and right subtree by passing the updated the depth.
    leftResult = dfs(node.left, depth + 1)
    rightResult = dfs(node.right, depth + 1)
    # Using the sum of natural number formula to calculate the current nodes distance from all its parents.
    currSum = (depth * (depth + 1)) // 2

    # Returning the aggregated result from the current node.
    return currSum + leftResult + rightResult


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
