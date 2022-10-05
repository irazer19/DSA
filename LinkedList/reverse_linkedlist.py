"""
Reverse a LinkedList, and return the new head of the list.
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We maintain the previous node.
    While traversing the linked list, we first store the next node in a temp variable, and then manipulate
    the pointers to point to the previous node, and then assign the current node as the temp.

    We return the previous node because the current node becomes None at the end of the while loop.
    """
    # Initializing the previous node.
    prev = None
    node = head
    # Traversing the linked list
    while node is not None:
        # Storing the next node
        temp = node.next
        # Changing the pointer to the previous node.
        node.next = prev
        # Updating the previous node.
        prev = node
        # Updating the current node.
        node = temp

    return prev
