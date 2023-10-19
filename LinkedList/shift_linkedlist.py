"""
Shift the given linked list by k distance and return the new head of the list.

head: 0 --> 1 --> 2 --> 3 --> 4 --> 5
k = 2

output: 4 --> 5 --> 0 --> 1 --> 2 --> 3
"""


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    Shifting the linked list by k distance means that the new head of the list will be the node at k distance
    from the end of the linked list whose tail is connected to the old head of the list.
    To do that, we traverse the linked list at the k-1 node and then grab the new head and manipulate the pointers
    to point to the old head.
    """
    # we move the node pointer to the k distance
    node = head
    while k > 0:
        node = node.next
        k -= 1
    # Now we create new pointer variables, where first ptr is at 0th node and second ptr is at kth distance.
    # We will move both the pointers until we the second ptr reaches the end so that we can divide the linkedlist
    # into two havles such that to shift it.
    second_ptr = node
    first_ptr = head
    while second_ptr.next:
        first_ptr = first_ptr.next
        second_ptr = second_ptr.next
    # At this point, we get the new head of the list
    newhead = first_ptr.next
    # We find the old tail by which will now become the middle node of the list
    curr = newhead
    while curr.next:
        curr = curr.next
    oldtail = curr
    # Connecting the old head to the older header
    oldtail.next = head
    # The first pointer is already at the node which will be out new tail so its next = None
    first_ptr.next = None

    return newhead
