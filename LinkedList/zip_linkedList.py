"""
You're given the head of a singly LinkedList of arbitrary length k. Write a function that zips the linked list in
place and returns its head.

A zipped list has the following structure:
1st node --> kth node --> 2nd node --> k-1 node --> 3rd node...etc

Input: 1 --> 2 --> 3 --> 4 --> 5 --> 6
Output: 1 --> 6 --> 2 --> 5 --> 3 --> 4
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We reach the middle of a linked list, then reverse the second half of the linked.
    Now as we traverse both the first and second half together, we will manipulate the pointers and return the
    head of the first half of the linked list.

    """
    # Initializing the pointers.
    first = linkedList
    second = linkedList
    # Moving the first ptr until the second pointer becomes None.
    while second:
        prev = first
        first = first.next
        second = second.next
        # Taking another step only if the second ptr still exists.
        if second:
            second = second.next

    # Reversing the second half of the list.
    headTwo = reverseList(first)
    headOne = linkedList

    # This node will store the current reference of the nodes for which we will manipulate the pointers as we move.
    node = None
    # Until both are not null.
    while headOne and headTwo:
        # Storing the next node of both the first and the second linked lists.
        nextNodeOne = headOne.next
        nextNodeTwo = headTwo.next
        # If the node reference is not initialized.
        if not node:
            # We make the start node as the head of the first linked list, and make it point to the second node.
            node = headOne
            node.next = headTwo
        else:
            # Else, we point the current node's reference to the headOne's node
            node.next = headOne
            # Move to that node
            node = node.next
            # Again make it point to the headTwo's node
            node.next = headTwo
        # Move to the latest node reference.
        node = node.next
        # Updating the headOne and headTwo to the next nodes.
        headOne = nextNodeOne
        headTwo = nextNodeTwo
    # When we reach the middle of the linked list, either both halves will be equal or the first half will be greater
    # one node. So we take care of that case.
    if headOne and node:
        # Pointing to the next node of the headOne
        node.next = headOne
        # Then immediately making the next pointer of headOne to None in order to stop going to the second half.
        headOne.next = None
    # Returning the the head of the first linked list.
    return linkedList


def reverseList(head):
    # Basic reversing of the linked list
    node = head
    prev = None
    while node:
        nextNode = node.next
        node.next = prev
        prev = node
        node = nextNode
    return prev
