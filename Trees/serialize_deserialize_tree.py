"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to
a string and this string can be deserialized to the original tree structure.

"""

import json


class Codec:
    # Time = Space = O(n)
    """
    Logic:
    Serialization: To convert a binary tree into a storable object. We do preorder traversal of the tree and then
    save the array in a file.

    Deserialization: To restore a binary tree from a given preorder traversal from a file.
    We read the preorder traversal array from a file, and then construct the tree in the same order.
    """

    def __init__(self):
        # Used to track the idx of the preorder traversal array for constructing the tree.
        self.preOrderIdx = 0

    def serialize(self, root):
        # Creating a preorder traversal array and storing in result
        result = []
        self.preOrderTraversal(root, result)
        # Converting to string and Saving it in a file.
        out = json.dumps(result)
        return out

    def preOrderTraversal(self, node, result):
        # Basic Pre order traversal.
        if not node:
            # If node is None, then we store -inf to indicate that we have a None value here.
            result.append(float('-inf'))
            return
        result.append(node.val)
        self.preOrderTraversal(node.left, result)
        self.preOrderTraversal(node.right, result)

    def deserialize(self, data):
        # Constructing the tree from preorder traversal after reading from a file.
        pre = json.loads(data)
        return self.constructTreeFromPreOrder(pre)

    def constructTreeFromPreOrder(self, pre):
        # If the preorder array idx is out of bounds, or we have -inf as the value, then return None.
        if self.preOrderIdx >= len(pre) or pre[self.preOrderIdx] == float('-inf'):
            return None
        # Creating a new node with the current idx value
        node = TreeNode(pre[self.preOrderIdx])
        # Moving to the next idx for adding left subtree
        self.preOrderIdx += 1
        node.left = self.constructTreeFromPreOrder(pre)
        # Moving to the next idx for adding right subtree
        self.preOrderIdx += 1
        node.right = self.constructTreeFromPreOrder(pre)
        return node


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
