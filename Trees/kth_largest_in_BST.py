"""
Find the kth largest value in the BST.
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Time: O(h + k) and Space: O(h), h = height of tree and k = kth largest value.
    """
    Logic:
    If we do reverse Inorder traversing (right, root, left), then we will visit the values in descending order(largest
    to smallest).

    We maintain a global class to track the total visited nodes. As we do reverse Inorder traversing, we will
    keep updating the visited nodes until visited = k.
    """
    # Result class to store the visited nodes and the resultant node value.
    result = Result(None, 0)
    reverseInorder(tree, result, k)

    return result.nodeValue


def reverseInorder(node, result, k):
    # Base Case.
    if not node:
        return

    # Moving to right
    reverseInorder(node.right, result, k)
    # Once we return from right subtree, if we already have the result value then we return.
    if result.nodeValue:
        return
    # Increase visited by 1
    result.visitedSoFar += 1
    # Now also check whether visited = k, if yes and the result value is also None, then we found our answer and
    # hence we update the result node value and return.
    if result.visitedSoFar == k and result.nodeValue is None:
        result.nodeValue = node.value
        return
    # Else, move to left.
    reverseInorder(node.left, result, k)


class Result:
    def __init__(self, nodeValue, visitedSoFar):
        self.nodeValue = nodeValue
        self.visitedSoFar = visitedSoFar
