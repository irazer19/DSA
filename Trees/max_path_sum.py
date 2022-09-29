"""
Write a function that takes in a binary tree and returns its max path sum.
A path is a collection of connected nodes in a tree, where no node is connected to more than two other nodes; a path
sum is the sum of the values of the nodes in a particular path.

"""


def maxPathSum(tree):
    # Time: O(n) and Space: O(h)
    """
    Logic:
    For a node, we explore its left subtree and the right subtree, the output is the max path sum from each.
    Next, we update the result like this:
    max of:
    1. Current result.
    2. Current node value + result from left subtree
    3. Current node value + result from right subtree
    4. Current node value + result from left subtree + result from right subtree
    We do the above in case there is a -ve value.

    After updating the result, we return the max path sum.
    max path sum = max (current node value + max(left, right))
    """
    # result object
    result = Result(float('-inf'))
    getSum(tree, result)

    return result.maxSum


def getSum(node, result):
    # For None, max sum is 0
    if not node:
        return 0

    # Exploring left and right subtree to get the max path sum from each.
    leftResult = getSum(node.left, result)
    rightResult = getSum(node.right, result)
    # Updating the result
    result.maxSum = max(result.maxSum, max(leftResult + node.value,
                                           rightResult + node.value,
                                           leftResult + rightResult + node.value))
    # returning then max path value till the current node.
    return max(leftResult + node.value, rightResult + node.value)


class Result:
    def __init__(self, maxSum):
        self.maxSum = maxSum
