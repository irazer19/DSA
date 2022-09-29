"""
You're given the root node of a binary tree, a target value of a node that's contained in the tree, and a positive
integer k. Write a function that returns the values of all the nodes that are exactly distance k from the node with
target value.

"""


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findNodesDistanceK(tree, target, k):
    # Time = Space = O(n)
    """
    Logic:
    Since we have to find all the nodes at distance k from the target node, we use BFS to traverse layer by layer.
    We start with the target node in the queue, pop it, and then add all the unvisited neighbors(left, right, parent)
    in the queue. After we have popped all the nodes in a layer, we decrease k by 1.
    We keep repeating until k is 0 or q is empty.
    Finally, we return all the nodes left in the queue when k became 0.

    """
    queue = []
    # Dictionary to store parent node for all the nodes.
    parentDict = {}
    # Tracking the visited nodes
    visited = set()
    # Getting the target node.
    getTargetNode(tree, target, queue)
    # Getting all the parents
    getParents(tree, parentDict, None)
    # BFS
    while queue:
        # Looping first layer.
        for i in range(len(queue)):
            currNode = queue.pop(0)
            # Marking as visited
            visited.add(currNode)
            # Getting the parent of this node
            parentNode = parentDict.get(currNode, None)
            # Exploring the left, right and parent nodes if its unvisited.
            if currNode.left and currNode.left not in visited:
                queue.append(currNode.left)
            if currNode.right and currNode.right not in visited:
                queue.append(currNode.right)
            if parentNode and parentNode not in visited:
                queue.append(parentNode)
        # Decreasing k after completing a layer.
        k -= 1
        # If k is 0, then we stop.
        if k == 0:
            break
    # Return all the left over queue elements.
    return [obj.value for obj in queue]


def getTargetNode(node, target, queue):
    # Fetching the target node from the tree
    if not node:
        return
    getTargetNode(node.left, target, queue)
    if node.value == target:
        queue.append(node)
        return
    if not queue:
        getTargetNode(node.right, target, queue)


def getParents(node, parentDict, parent):
    # Getting parents of all the nodes.
    if not node:
        return

    getParents(node.left, parentDict, node)
    parentDict[node] = parent
    getParents(node.right, parentDict, node)
