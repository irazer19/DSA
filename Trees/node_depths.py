"""
The distance between a node in a Binary tree and the tree's root is called the node's depth.
Write a function that takes in a Binary tree and returns the sum of its nodes depths.

Input:
     1
    / \
   2   3
  /
 4

Output:
11

"""


def nodeDepths(root):
    # Time: O(n) and Space: O(h), h is the height of the tree.
    """
    Logic:
    We use BFS starting from the root node, and in the queue we store (node, distance from root).
    As we pop out the nodes, we add the nodes distance to the result.
    Then we check the left and right child of the node, and if it exists then we add them in the queue with
    current distance + 1
    """
    # Result to store sum of all the node depths
    result = 0
    # Queue, where the root node with itself has a depth of 0.
    q = [(root, 0)]

    while q:
        # Getting the current node and its distance from the root node.
        node, dist = q.pop(0)
        # Adding the dist to the result
        result += dist
        # Checking for left and right children.
        # Appending the children to the queue with +1 increase in current distance from the root node.
        if node.left:
            q.append((node.left, dist + 1))
        if node.right:
            q.append((node.right, dist + 1))

    return result


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
