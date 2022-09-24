"""
Validate the given Binary Search Tree.
Return a boolean.

"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Time: O(n) and Space: O(d), where d = tree depth.
    """
    Logic:
    We perform DFS, at every node, we check whether the node value lies within the given range(start, end) to
    satisfy the BST property.
    If a node's value is not within the given range, then we return False, otherwise we check the result from
    its left subtree and the right subtree, if both the results return True, only then we return True.

    NOTE: For BST: Left Child < Parent and Right Child >= Parent.

    """
    # For the first root node, the range is -infinity to +infinity.
    return solve(tree, float('-inf'), float('inf'))


def solve(node, startVal, endVal):
    # If node is None, return True as base case.
    if not node:
        return True
    # If the node's value is not within the given range, return False'
    if node.value < startVal or node.value > endVal:
        return False

    # Else, we check the left subtree and the right subtree.
    leftResult = solve(node.left, startVal, node.value - 1)
    rightResult = solve(node.right, node.value, endVal)

    # Only if both the left and right subtree's are valid, we return True.
    return leftResult and rightResult
