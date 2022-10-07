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
    # Counting the total number of nodes in the linked list.
    totalNodes = getTotalNodes(head)
    # Taking the mod of k for knowing the exact distance which will be between 0 to k-1.
    k = k % totalNodes
    # Edge case, if k is 0, then we just return the same list.
    if k == 0:
        return head
    # Else we compute the distance to traverse from the head node, we want to reach the node which is before
    # the new head that's why we add -1
    nodesToTravel = totalNodes - k - 1

    # variable for traversing.
    node = head
    # Traversing the computed distance.
    counter = 0
    while counter != nodesToTravel:
        node = node.next
        counter += 1
    # Grabbing the new head.
    newHead = node.next
    # Here we want to find the tail of the new head so that we can connect it to the older head.
    newTail = newHead
    while newTail.next:
        newTail = newTail.next
    # The first part of the original list becomes the tail, so we make its end point to None.
    node.next = None
    # Now the new tail if the last part of the original list which points to the head of the original list.
    newTail.next = head

    return newHead


def getTotalNodes(node):
    # Function to count the total numbers of nodes in the list.
    total = 0
    while node:
        node = node.next
        total += 1
    return total
