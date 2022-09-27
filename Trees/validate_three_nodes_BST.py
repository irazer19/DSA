"""
Given nodeOne, nodeTwo, and nodeThree of a BST. return whether nodeTwo lies between nodeOne and nodeThree.

"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Time: O(d) and Space: O(1), d is the depth.
    """
    Logic:
    We have to find whether the nodeTwo lies between nodeOne and nodeThree, it can be between nodeOne and nodeThree or
    nodeThree and nodeOne.
    First we check whether from nodeOne we can reach nodeTwo, if yes then again check whether from nodeTwo we can
    reach nodeThree, if yes return True.
    If the above is False, repeat the same check starting from nodeThree --> nodeTwo, if yes then
    nodeTwo --> nodeOne.

    If none of the above returns True, then we return False.
    """
    # Starting from nodeOne to nodeTwo.
    if isFound(nodeOne, nodeTwo):
        # nodeTwo to nodeThree
        if isFound(nodeTwo, nodeThree):
            return True
    # Starting from nodeThree to nodeTwo
    elif isFound(nodeThree, nodeTwo):
        # nodeTwo to nodeOne
        if isFound(nodeTwo, nodeOne):
            return True
    return False


def isFound(node, target):
    # Since its BST, we can directly use while loop to move to next node.
    # We move until we find the target node, else return False at the end of the function.
    while node:
        if target.value < node.value:
            node = node.left
        elif target.value > node.value:
            node = node.right
        else:
            return True
    return False
