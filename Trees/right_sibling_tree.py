"""
Write a function that takes in a Binary Tree, transforms it into a Right Sibling Tree, and returns its root,
A Right Sibling Tree is obtained by making every node in a Binary Tree have its right property point to its right
sibling instead of its right child. A node's right sibling is the node immediately to its right on the same level
or None / null if there is no node immediately to its right.

Note that once the transformation is complete, some nodes might no longer have a node pointing to them. For example,
in the sample output below, the node with value 10 no longer has any inbound pointers and is effectively unreachable.
The transformation should be done in place, meaning that the original data structure should be mutated (no new
structure should be created).

"""


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def rightSiblingTree(root):
    # Time: O(n) and Space: O(d)
    """
    Logic:
    We use BFS.
    We maintain two lists:
    currLayer = Stores the nodes in the current layer
    children = Stores all the children of the current layer.

    For a current layer, we first collect all the children including "None".
    Then we loop through the nodes in the current layer, and update to its right sibling.
    Once done, we make the children as the current layer, and reinitialize children = [].

    """
    # Initializing the lists.
    node = root
    currLayer = [node]
    children = []

    # BFS, until we have nodes in the current layer.
    while currLayer:
        # Collect all the children of the current layer.
        for currNode in currLayer:
            if currNode:
                children.append(currNode.left)
                children.append(currNode.right)

        # Now, for each node in the current layer, point its right pointer to the next node of the current layer.
        for i in range(len(currLayer)):
            # Only if node exists.
            if currLayer[i]:
                # If its the last node, then point it to None.
                if i == len(currLayer) - 1:
                    currLayer[i].right = None
                else:
                    # Else, point it to the next node.
                    currLayer[i].right = currLayer[i + 1]
        # Update the current layer and reinitialize the children array.
        currLayer = children
        children = []

    return root
