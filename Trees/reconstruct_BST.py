"""
Given a preOrderTraversalValues, reconstruct the BST from it.
Preorder traversal: Root, Left, Right.

preOrderTraversalValues = [10, 4, 2, 1, 3, 17, 19, 18]

"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Counter:
    def __init__(self, idx):
        self.idx = idx


def reconstructBst(preOrderTraversalValues):
    # Time = Space = O(n)
    """
    Logic:
    We are given preorder traversal values, so our first element is always the root.
    We will maintain a global class for tracking the current index of the preOrderTraversalValues array.

    Now we will start by creating a node at the current index, and then increase the index counter by 1,
    then we will move to left and then right of the node.
    Base case: If the idx is out of bounds, then we return None, or if the current node value is out of bounds from its
    given range, we return None.

    A node can be placed in the BST if it is within the given range of values.

    """
    # Object to track the current index
    counter = Counter(0)

    return createBST(preOrderTraversalValues, counter, float('-inf'), float('inf'))


def createBST(array, counter, lower, upper):
    # If the current index is out of bounds, return None
    if counter.idx == len(array):
        return None
    # If the current node value is out of bounds, return None
    currVal = array[counter.idx]
    if currVal < lower or currVal > upper:
        return None

    # Create a new node.
    node = BST(currVal)
    # Move to index by 1
    counter.idx += 1
    # Fill the left and the right subtree recursively by passing the correct lower and upper range of values.
    node.left = createBST(array, counter, lower, currVal - 1)
    node.right = createBST(array, counter, currVal, upper)

    return node
