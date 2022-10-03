"""
Print the bottom view of a binary tree.

           10
          /  \
         5    20
        / \   / \
       3   8  18  25
          /
         7

"""


def bottomView(root):
    # Time = Space = O(n)
    """
    Logic:
    Using BFS, for every node we try to find its distance from the center of the tree, the left node has a
    negative distance and the right node has a positive distance.
    The root node's distance is 0 from the center. We maintain a hashmap to store the result for each distance,
    {distance: node value}, and as we move down, we overwrite the older value of that distance with this new-found
    node at the same distance because we want the bottom view of the tree.
    Finally, print all the values inside the hashmap.
    """
    node = root
    # Hashmap to store the node value for each distance.
    result = {}

    # Root distance is 0 from the center of the tree.
    q = [(node, 0)]
    # BFS
    while q:
        # Get the node and its distance.
        currNode, dist = q.pop(0)
        # Overwrite the existing value for the same distance.
        result[dist] = currNode.value
        # Appending the children with their distance from the center.
        if currNode.left:
            q.append((currNode.left, dist - 1))
        if currNode.right:
            q.append((currNode.right, dist + 1))

    return list(result.values())


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


tree = BinaryTree(10)
tree.left = BinaryTree(5)
tree.left.left = BinaryTree(3)
tree.left.right = BinaryTree(8)
tree.left.right.left = BinaryTree(7)
tree.right = BinaryTree(20)
tree.right.left = BinaryTree(18)
tree.right.right = BinaryTree(25)

print(bottomView(tree))
