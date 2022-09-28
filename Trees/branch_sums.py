"""
Write a function that takes in a Binary Tree and returns a list of its branch sums ordered from leftmost branch sum
to the rightmost branch sum.

"""


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Time = Space = O(n)
    """
    Logic:
    We start from the root node, and keep computing the current sum as we move down the tree.
    First we check the left branch and then the right branch, if we find a leaf node, then we add the current sum
    to the result array.
    """
    # Storing the result
    result = []
    # Initially the current sum is 0.
    exploreTree(root, 0, result)

    return result


def exploreTree(node, currSum, result):
    # Checking for leaf node.
    if node.left is None and node.right is None:
        # We add the leaf nodes value to the current sum and then add it to the result array, and return.
        currSum += node.value
        result.append(currSum)
        return

    # If left nodes exist only then we explore it.
    if node.left:
        # Here we pass the updated current sum by adding the node's value.
        exploreTree(node.left, currSum + node.value, result)
    # If right nodes exist only then we explore it.
    if node.right:
        # Here we pass the updated current sum by adding the node's value.
        exploreTree(node.right, currSum + node.value, result)

    return
