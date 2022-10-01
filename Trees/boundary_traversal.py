"""
Print all the nodes which are at the boundary of a tree.

"""


def boundaryTraversal(root):
    # Time = Space = O(n)
    """
    Logic:
    First we traverse all the left most nodes, then all the leaf nodes, then all the right most nodes.
    The right most nodes have to be in reverse order because we want to boundary values to be in anti-clockwise order.

    Now from all the three traversed results, merge them so that its in anti-clockwise order.

    """
    # Stores the order of nodes for each type of traversal.
    preorder = []
    postorder = []
    leaforder = []

    # Traversing.
    preOrder(root, preorder)
    getLeafs(root, leaforder)
    postOrder(root, postorder)

    # The preorder of left nodes result is already in its correct order so we start from leaf nodes.
    result = preorder
    # Adding all the leaf nodes starting from 1 because that node was already added in the preorder.
    for i in range(1, len(leaforder)):
        result.append(leaforder[i])

    # Adding the right most nodes, in this we skip the first and the last nodes because we have already added
    # during the preorder and leaf result addition.
    # Also we do reverse of the result for right nodes, because we are moving anti-clockwise.
    for i in reversed(range(1, len(postorder) - 1)):
        result.append(postorder[i])

    return result


def preOrder(node, result):
    # The moment we hit a leaf node, we return -1 to signal that we want to get out now.
    # We do preorder because we want the anti-clockwise order of the left nodes.
    if not node:
        return
    result.append(node.value)
    if not node.left and not node.right:
        return -1
    if preOrder(node.left, result) == -1:
        return -1
    preOrder(node.right, result)


def postOrder(node, result):
    # This is not really a postOrder because we capture the node first and then move to right and then left of the
    # tree. And if we hit a leaf node, we stop and return -1 and get out.
    if not node:
        return
    result.append(node.value)
    if not node.left and not node.right:
        return -1
    if postOrder(node.right, result) == -1:
        return -1
    postOrder(node.left, result)


def getLeafs(node, result):
    # Inorder traversal where we only add leaf nodes.
    if not node:
        return
    getLeafs(node.left, result)
    if not node.left and not node.right:
        result.append(node.value)
    getLeafs(node.right, result)


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

boundaryTraversal(tree)
