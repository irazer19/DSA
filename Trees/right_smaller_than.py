"""
Write a function that takes in an array of integers and returns an array of the same length, where each element
in the output array corresponds to the number of integers in the input array that are to the right of the relevant
index and that are strictly smaller than the integer at that index.

In other words, the value at output[i] represents the number of integers that are to the right of 1 and that are
strictly smaller than input[i].

Input:
array = [8, 5, 11, -1, 3, 4, 2]

Output:
[5, 4, 4, 0, 1, 1, 0]

"""


def rightSmallerThan(array):
    # Time: O(n*log(n)) and Space: O(n) in average case.
    # Time = Space = O(n^2) in worst case.
    
    """
    Logic:
    We construct a BST tree starting from the end of the array.
    For every node we track the total number of nodes in the left subtree. As we move insert a node,
    If the new node is greater than the current node then we know that the new node is also greater than all
    the left nodes of the current node including the current node.

    And if the new node is less than the current node, then we simply increase number of left node count for the
    current node, and then insert the new node.

    We return the new node after inserting it because it stores the greaterThan value as we traversed, and we
    then store that in the result array.

    """
    # Result array, default value is 0
    result = [0 for _ in array]
    # Initializing the BST class with root = None
    bst = SpecialBST(None)

    # Inserting the array values starting from the end.
    for i in range(len(array) - 1, -1, -1):
        node = bst.insert(array[i])
        # Storing the greaterThan value in the result for the current index
        result[i] = node.greaterThan

    return result


class SpecialBST:
    def __init__(self, root):
        self.root = root

    def insert(self, val):
        # First we create the new node for the given value.
        newNode = BST(val)
        # If the root is empty, then we make the new node as root and return it.
        if not self.root:
            self.root = newNode
            return newNode

        # Else, we start inserting from the root node onwards
        node = self.root
        while True:
            # If the val is less than the current node.
            if val < node.value:
                # First we increase the left subtree count for the node.
                node.leftNodesCount += 1
                # Basic insert for BST.
                if node.left:
                    node = node.left
                else:
                    node.left = newNode
                    break
            else:
                # Else, if the val is greater or equal to the current node, then we know that all the current node's
                # left subtree nodes are smaller than the val, so we anyways increase the greaterThan count for the
                # current new node.
                newNode.greaterThan += node.leftNodesCount
                # Now if the val is strictly greater than the current node, then we also increase the greaterThan count
                # by 1.
                if val > node.value:
                    newNode.greaterThan += 1
                # Basic insert for BST
                if node.right:
                    node = node.right
                else:
                    node.right = newNode
                    break
        # return the new node so that greaterThan can be stored in the result.
        return newNode


class BST:
    # BST node class.
    # leftNodesCount = Counts the number of nodes in the left subtree of this node.
    # greaterThan = Stores the total number of nodes that are smaller than the current node.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.leftNodesCount = 0
        self.greaterThan = 0
