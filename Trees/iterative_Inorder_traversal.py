"""
Print all the nodes in Inorder traversal using iteration.
"""


def iterativeInOrderTraversal(tree, callback):
    # Time = Space = (n)
    """
    Logic:
    While loop until both stack and node is empty/None.
    If node exists, we store in the stack and move to left,
    If node is None, we pop, print and move to right.
    """
    # Stores the "in path" nodes as we move down the tree.
    stack = []
    node = tree
    # Stores the inorder traversal result
    result = []
    # Both, stack and node have to be empty/None for break
    while stack or node:
        # If current node is None
        if not node:
            # Pop from stack
            node = stack.pop()
            # Print
            result.append(node)
            # Go right
            node = node.right
        else:
            # Else, if the current node exists, store in stack and just move left.
            stack.append(node)
            node = node.left
