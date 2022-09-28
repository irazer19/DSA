"""
Invert a given binary tree.

"""


def invertBinaryTree(tree):
    # Time: O(n) and Space: O(d), d is the depth of the tree.
    """
    Logic:
    Using DFS, explore left, then explore right, and then interchange the result of left and right for the
    current node and return the node.
    """
    # If node is None
    if not tree:
        return None

    # Exploring left
    leftSubTree = invertBinaryTree(tree.left)
    # Exploring right
    rightSubTree = invertBinaryTree(tree.right)
    # Interchange the result of left and right for the current node.
    tree.left = rightSubTree
    tree.right = leftSubTree

    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
