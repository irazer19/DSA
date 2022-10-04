"""
Given a head of a singly linked list, remove all the duplicate nodes, and return the modified linked list.

Input:
1--1--2--2--3--4--4--4--5
Output:
1--2--3--4--5
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    Starting from the head, if the next node is duplicate then use a while loop until the next node is duplicate,
    and once out then connect it to the next node and move to the next node.
    And if the next node is not duplicate then just move to the next node.
    """
    # We will use node variable for traversing.
    node = linkedList

    # Exploring all the nodes until None
    while node:
        # If the current node ==  next node
        if node.next and node.value == node.next.value:
            # Take a reference to the current node.
            currNode = node
            # Until the next node is duplicate, keep moving to the next node.
            while currNode and currNode.next and currNode.value == currNode.next.value:
                currNode = currNode.next
            # Once out, connect the original node to this current node.
            node.next = currNode.next
        # Move to the next node
        node = node.next

    return linkedList
