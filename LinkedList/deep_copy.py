"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any
node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should
point to new nodes in the copied list such that the pointers in the original list and copied list represent the same
list state. None of the pointers in the new list should point to nodes in the original list.

"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    # Time: O(n) and Space: O(n)
    """
    Logic:
    We can easily create a new linked list from the given list, but the challenge is to also handle the random
    pointers of each node because it can point to any nodes.
    Step 1: We create a new list where the original list's next points to the current new replicated node.
    And the current replicated node's random points to the original node.

    Once we have the above list ready, then we know that the new lists next pointer is correct, and so to make the
    random pointer also point to the correct node, we traverse the new list, and at every node get access to its
    original node and connect it to the correct random node.
    """
    # The getCopy function returns a replicated copy of the list where the next pointer of every node points
    # correctly, but the random pointer does not.
    modifiedNode = getCopy(head)
    node = modifiedNode
    # Traversing the new list
    while node:
        # Getting the random node from the original list.
        randomNode = node.random.random
        # If the random exists, then we know that it points to its replicated node so we adjust the pointer.
        if randomNode:
            node.random = randomNode.next
        else:
            # Else, we point the random node to None.
            node.random = None
        node = node.next

    return modifiedNode


def getCopy(head):
    # We create a brand new list here.
    node = head
    newHead = Node(x=-1)
    currNode = newHead

    # Traversing until None.
    while node:
        # Capturing the next node.
        nextNode = node.next
        # Creating a new node.
        newNode = Node(x=node.val)
        # Connecting the current replicated node to the next replicated node.
        currNode.next = newNode
        # Moving forward the current replicated node
        currNode = currNode.next
        # Making the original node's next point to the current replicated node.
        node.next = currNode
        # Making the current replicated node's random point to the original node.
        currNode.random = node
        # Moving to the next node in the original list.
        node = nextNode
    return newHead.next
