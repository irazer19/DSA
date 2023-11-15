"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest. You may return the result in any order.


Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
"""


def del_nodes(self, root, to_delete):
    # Time = Space = O(n)
    """
    If we find a node which has to be deleted, then the left and right recursion will also pass a parameter
    called is_root which suggests that its children are about to become a root as the parent will get deleted.
    This way we track the nodes which are supposed to be part of the result
    And if the node was to be deleted, then we will return None from that recursion.
    """

    # Saving the result
    result = []
    self.dfs(result, root, set(to_delete), True)

    return result


def dfs(self, result, node, to_delete, is_root):
    # Edge case
    if not node:
        return None
    # Checking whether the current node is supposed to be deleted.
    node_to_delete = node.val in to_delete
    # If the current node is considered as root, and its not supposed to be deleted then we know its a resultant node.
    if is_root and not node_to_delete:
        result.append(node)
    # node_to_delete if YES, then its children will get passed is_root=True in the recursion
    # Going to the left
    node.left = self.dfs(result, node.left, to_delete, node_to_delete)
    # To the right
    node.right = self.dfs(result, node.right, to_delete, node_to_delete)
    # We return None if the current node was to be deleted, else the usual node.
    return None if node_to_delete else node
