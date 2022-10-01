"""
Write a function that takes in the root nodes of two binary tree and returns a boolean representing whether theie
leaf traversals are the same.

The leaf traversal of a binary tree traverses only its leaf nodes from left to right. A leaf node is any node that has
no left or right children.

"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def compareLeafTraversal(tree1, tree2):
    # Time: O(n + m) and Space: O(h1 + h2), h1 and h2 are the height of the tree1 and tree2.
    """
    Logic:
    We will do Preorder traversal iteratively of both the trees.
    First, we will have a while loop which will get the next leaf node of both the trees, then we compare the
    leaf values, if they don't match then we return False, else we continue with the next leaf nodes.
    Finally, if we exhaust all the leaf nodes, then we return True as a default from the function.

    We find the next leaf node using the Preorder traversal.

    """

    # Initial stack value for preorder traversal.
    stack1 = [tree1]
    stack2 = [tree2]

    # Until we have nodes in both the stack, we will continue to find the next leaf node.
    while stack1 and stack2:
        # Finding the next leaf node using the preorder traversal.
        leaf1 = findNextLeaf(stack1)
        leaf2 = findNextLeaf(stack2)
        # Comparing the leaf values
        if leaf1 != leaf2:
            return False

    # Default response if all leaf nodes had a match,
    return True


def findNextLeaf(stack):
    # Preorder traversal.
    """
    Idea: Since in preorder traversal we move: Root, Left, Right.
    So we first pop the node from the stack(root), now since we visit left first and then right, that's why we
    store the right node first in the stack and then the left node so that we can pop accordingly.
    """

    while stack:
        # Visiting the root node first
        node = stack.pop()
        # If its a leaf node, return it.
        if not node.left and not node.right:
            return node.value
        # Storing the right node first because we will visit this last
        if node.right:
            stack.append(node.right)
        # Storing the left node next because we will pop it next time.
        if node.left:
            stack.append(node.left)
