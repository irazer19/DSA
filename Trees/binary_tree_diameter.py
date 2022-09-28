"""
Write a function that takes in a binary tree and returns its diameter. The diameter of a binary tree is defined
as the length of its longest path, even if that path doesn't pass through the root of the tree.

"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Time: O(n) and Space: O(h), h is the height of the tree.
    """
    Logic:
    Note: Number of edges make up the size of the diameter.
    For a node, we traverse the left subtree, then the right subtree, and then the current diameter
    is equal to left + right, we update the result.
    Next, for returning, we return the max of total number of edges either from left subtree or right subtree + 1.
    We add + 1 because when we return, the current node also forms an edge with the parent node.

    """
    # Result object to store the max diameter.
    result = Result(float('-inf'))
    getDiameter(tree, result)

    return result.diameter


def getDiameter(node, result):
    # If node is None then return 0
    if not node:
        return 0
    # Exploring the left and the right subtrees to get the max path for each.
    leftPath = getDiameter(node.left, result)
    rightPath = getDiameter(node.right, result)

    # Calculating the diameter, current diameter = longest path from left + longest path from right
    result.diameter = max(result.diameter, leftPath + rightPath)
    # Calculating the max path for returning to the previous node.
    # Either left subtree or right subtree has the max path + 1(current node's edge with the parent node)
    maxPath = max(leftPath, rightPath) + 1

    return maxPath


class Result:
    def __init__(self, diameter):
        self.diameter = diameter
