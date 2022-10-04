"""
Write a function that takes in the head of a Singly Linked List and an integer k and removes the kth node from the end
of the list.
The removal should be done in place, meaning that the original data structure should be mutated (no new structure
should be created).
Furthermore, the input head of the linked list should remain the head of the linked list after the removal is done,
even if the head is the node that's supposed to be removed. In other words, if the head is the node that's supposed to
be removed, your function should simply mutate its value and next pointer.

Note that your function doesn't need to return anything.
You can assume that the input Linked List will always have at least two nodes and, more specifically, at least k nodes.
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None /
null if it's the tail of the list.

"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We'll use two pointers, first and second, the first pointer will be at the head and the second pointer will
    be moved to the kth distance from the first.
    Now keep moving both the pointers until the second.next becomes None.
    Once second.next becomes None, the target node to be removed will be the next node to the first pointer.
    Therefore, remove the target node using basic pointer manipulation.
    """

    # node variable for traversing
    node = head
    # First pointer
    first = node
    # Second pointer
    second = node

    # Second pointer will move until it is at k distance from the first.
    while second and k > 0:
        second = second.next
        k -= 1

    # Case: IF second is already none, then we know that the head node has to be deleted.
    # So we just copy the next nodes value in the head node.
    if second is None:
        first.value = first.next.value
    else:
        # Else, we move the first and second together until the second.next is None
        while second.next:
            first = first.next
            second = second.next

    # Finally, for either of the cases, we remove the node which is after the first node.
    first.next = first.next.next

    return head
