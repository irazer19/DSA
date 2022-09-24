"""
Write a function that takes in a BST and a target integer value and returns the closest value to that target value
contained in the BST.

Input:
      10
     /  \
    5    15
        /  \
       13   22

target: 12

Output: 13, because node 13 is the closest value to the target value.

"""


def findClosestValueInBst(tree, target):
    # Time: O(log(n)) and Space: O(1)
    """
    Logic:
    Start from the root node, and for every node check its absolute difference with the target.
    We want to minimize the absolute difference between the node value and the target.
    Now, move to the next node using the rules of BST until the node becomes "None".
    """
    # Storing the current absolute difference
    currDist = float('inf')
    # Resultant node value
    result = None
    # Starting from the root.
    node = tree

    # Until the node is not None, we keep checking the absolute difference,
    while node:
        # If the current node's absolute difference is less than the existing, then we update.
        if currDist > abs(node.value - target):
            currDist = abs(node.value - target)
            result = node.value
        # Moving the node by the rules of BST.
        if target < node.value:
            node = node.left
        elif target > node.value:
            node = node.right
        else:
            # If we find a node which has the same value as the target, then we simply return this node because
            # 0 is the minimum distance we can get.
            return node.value
    return result


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
