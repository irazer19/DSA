"""
Write a function that takes in a Binary Tree, flattens it, and returns its leftmost node.
A flattened Binary Tree is a structure that's nearly identical to a Doubly Linked List (except that nodes have left
and right pointers instead of prev and next pointers), where nodes follow the original tree's left-to-right order.
Note that if the input Binary Tree happens to be a valid Binary Search Tree, the nodes in the flattened tree will be
sorted.
The flattening should be done in place, meaning that the original data structure should be mutated
(no new structure should be created).

Basically, the output is like a doubly linked list on the inorder traversal output.
"""


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    # Time: O(n) and Space: O(d), d is the depth of the tree.
    """
    Logic:
    We maintain a global root reference of the new tree.
    As we do inorder traversing of the tree, for each node, instead of printing we update the pointers of the
    root reference with respect to the current node.
    Finally, we return the root reference as the result.
    """
    # New tree object which holds the root reference
    newTree = NewTree(None)
    inorder(root, newTree)
    return newTree.root


def inorder(node, newTree):
    # Basic inorder traversing of the tree
    if not node:
        return

    inorder(node.left, newTree)
    # If root is None, then we update it.
    if not newTree.root:
        newTree.root = node
        newTree.node = node
    else:
        # Else, we update the pointers.
        # Here, left pointer = prev of doubly linked list, and right pointer = next of doubly linked list
        node.left = newTree.node
        newTree.node.right = node
        # Keeping the root reference node to the latest next node.
        newTree.node = newTree.node.right

    inorder(node.right, newTree)


class NewTree:
    def __init__(self, node):
        # root is the main reference which we return
        self.root = node
        # node is the object which we use for traversing.
        self.node = node
