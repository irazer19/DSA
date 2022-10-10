"""
Write a function that takes in the head of a singly linked list, swaps every pair of adjacent nodes in place.
If the input linked list has an odd number of nodes, its final node should remain the same.

Input: 0 --> 1 --> 2 --> 3 --> 4 --> 5
Output: 1 --> 0 --> 3 --> 2 --> 5 --> 4

"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We check the current node and its next node, if they exist then we swap them. Now after swapping we have
    to maintain the previous pointer so that it can point to the current node after swapping.
    first ptr = Current node.
    second ptr = 2nd node from the current node.
    third ptr = 3rd node from the current node.
    """
    # Stores the new head of the resultant list
    newHead = None
    # Previous node, so that we can later point it to the correct node after swapping.
    prev = None
    node = head

    # If there is no node or just one node, we return the current head.
    if not node or not node.next:
        return head
    # If current node and next node exists for swap.
    while node and node.next:
        # Grabbing the first 3 nodes.
        first = node
        second = node.next
        third = node.next.next
        # Pointing the second to first.
        second.next = first
        # If prev node exists
        if prev:
            # Pointing previous to the second.
            prev.next = second
        # Updating the previous node.
        prev = first
        # Initializing the new head. This happens only once during the execution.
        if not newHead:
            newHead = second
        # Since we have swapped first and second, now we move directly to the third node.
        node = third

    # If node still exists, we point the previous to it.
    if node:
        prev.next = node
    else:
        # Else, we simply make the previous.next to None
        prev.next = None
    return newHead
