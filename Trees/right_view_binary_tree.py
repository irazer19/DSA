"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes
you can see ordered from top to bottom.

"""


def rightSideView(root):
    # Time: O(n) and Space: O(h), h is the height of the tree.
    """
    Logic:
    Using BFS, just add the last element of the layer in the result and move to the next layer.
    The right view of the tree is all the right most elements in every layer.
    """
    # BFS
    q = [root]
    result = []

    while q:
        # Initializing to store the next layer elements
        nextLayer = []
        # Last element of the current layer
        node = q[-1]
        # Adding the last element to the result
        result.append(node.value)
        # Now appending all the children from left to right into the next layer
        for i in range(len(q)):
            currNode = q[i]
            if currNode.left:
                nextLayer.append(currNode.left)
            if currNode.right:
                nextLayer.append(currNode.right)
        # Assigning the next layer to the current layer.
        q = nextLayer
    return result
