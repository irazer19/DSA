"""
Construct a binary tree from the given array of inorder and postorder traversals.
Return the binary tree.

"""


def fromInorderPostorder(inorder, postorder):
    # Time = Space = O(n)
    """
    Logic:
    We get the root index from the end of the postorder array, so we need to move from the end of the postorder array
    to get the next root index to construct the binary tree.
    Once we get the root index value, then we try to find that value's index in the inorder array to decide the
    start and end index of inorder for making the recursive call to right and left.
    If the start >  end for the function call, then we return None.
    The start and end index show the current set of values in the inorder array.

    Also, to reduce the time complexity, we create a hashmap of the inorder array to access the index of a particular
    value.

    """
    # Making the root index a global class because we move strictly from end to start in the postorder array.
    rootIdx = RootIdx(len(postorder) - 1)
    # Hashmap to store all the index of values in inorder array for quick access.
    inorderIndices = {inorder[i]: i for i in range(len(inorder))}
    # Making the call, initially the start and end index is the entire range of the inorder array.
    root = getTree(inorder, postorder, rootIdx, inorderIndices, 0, len(inorder) - 1)
    return root


def getTree(inorder, postorder, rootIdx, inorderIndices, startIdx, endIdx):
    # Base case
    if startIdx > endIdx:
        return None

    # Creating the node object
    node = Node(postorder[rootIdx.idx])
    # Getting the index of the above node value from the inorder array.
    rootIdxInorder = inorderIndices[postorder[rootIdx.idx]]
    # Moving to the next root index
    rootIdx.idx -= 1
    # Going to the right, where we pass the correct range of start and end indices for the inorder array
    # depending on whether we are going to right of left.
    node.right = getTree(inorder, postorder, rootIdx, inorderIndices, rootIdxInorder + 1, endIdx)
    node.left = getTree(inorder, postorder, rootIdx, inorderIndices, startIdx, rootIdxInorder - 1)

    # Returning the node.
    return node


class RootIdx:
    # To track the next root index as we construct the tree.
    def __init__(self, idx):
        self.idx = idx


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


fromInorderPostorder([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
