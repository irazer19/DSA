"""
Given a sorted list, create a BST with minimum height.
Return the root node of the BST.

"""


def minHeightBst(array):
    # Time = Space = O(n)
    """
    Logic:
    To minimize the height of a BST, we select the middle element of the array as the root node, and then
    all the left elements make the left subtree and all the right elements make the right subtree.
    We do this recursively until the start index > end index.

    """
    # Passing the array, start index, and end index.
    return createTree(array, 0, len(array) - 1)


def createTree(array, start, end):
    # If the start index has crossed the end index, then we dont have any elements, we return None value for the node.
    if start > end:
        return None

    # Getting the mid
    mid = (start + end) // 2
    # Creating a new node with the middle element.
    node = BST(array[mid])
    # Recursively filling the left and right subtree.
    node.left = createTree(array, start, mid - 1)
    node.right = createTree(array, mid + 1, end)
    
    return node


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
