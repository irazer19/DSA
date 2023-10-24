"""
Given the root of a binary search tree (BST) and an integer target, split the tree into two subtrees where one subtree has nodes that are all smaller or equal to the target value, while the other subtree has all nodes that are greater than the target value. It Is not necessarily the case that the tree contains a node with the value target.
Additionally, most of the structure of the original tree should remain. Formally, for any child c with parent p in the original tree, if they are both in the same subtree after the split, then node c should still have the parent p.
Return an array of the two roots of the two subtrees.
"""


def split_bst(root, k):
    # Time = Space = O(logn)
    return split(root, k)


def split(node, k):
    """
    We will split the bst in left and right subtree as we traverse towards the node with value k, at each
    call we return the left and right subree.
    """
    # Edge case
    if not node:
        return None, None

    # If the current node is less or equal to k, we will start splitting to the right
    if node.val <= k:
        left, right = split(node.right, k)
        # Now since the right side returns the left_subtree and right_subtree, we know that the current node's
        # value is less than left_subtree, so we should connect them.
        node.right = left
        # Since we connected the left_subtree to the current node, we return
        # node (now current left tree), right (our right subtree result)
        return node, right
    else:
        # Similarly, if the current node value is greater than k, then we will split the left side.
        left, right = split(node.left, k)
        # The returned right_subtree is greater than k because of BST, so we should connect it to the current node's
        # left
        node.left = right
        # return left (as it is), node (updated right sub_tree)
        return left, node


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)


left, right = split_bst(root, 6)
print(left.val, right.val)
