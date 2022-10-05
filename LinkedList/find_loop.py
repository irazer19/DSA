"""
Write a function that takes in the head of a Singly Linked List that contains a loop (in other words, the list's
tail node points to some node in the list instead of None / null ). The function should return the node (the actual
node--not just its value) from which the loop originates in constant
Each LinkedList node has an integer value as well as a next node pointing to the next node in the list.

"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We initialize two pointers, first and second.
    We move the first by 1 distance and the second pointer by 2 distance until they meet at a common node.
    (Maths: Objective is to find the starting loop node from the point where both the pointers meet.
    P = Distance from the start node to the node where the loop begins.
    R = Extra distance traveled by the second pointer after completing one cycle.
    T = Total length of the linkedlist = 2P - R (DIY again.)
    T - (P + R) = P)

    So now we know that we have to travel "P" distance from the meeting node.
    Next, start a pointer from the start index, and a pointer from the node where they met.
    Keep moving the both the pointers until they meet and return the node.

    """
    # Initilizing the first and the second pointers.
    # Making sure that the first pointer is moved by 1 and the second is moved by 2 distance.
    firstPtr = head.next
    secondPtr = head.next.next

    # We want to move both the pointers until they meet
    while firstPtr != secondPtr:
        firstPtr = firstPtr.next
        secondPtr = secondPtr.next.next

    # Now run a new pointer from the start of the linkedlist.
    # And keep moving this new pointer and the pointer where the above met, until the current pointers meet again
    # which will cover the distance "P".
    startPtr = head
    while firstPtr != startPtr:
        firstPtr = firstPtr.next
        startPtr = startPtr.next

    # Returning the starting node where the loop begins.
    return firstPtr
