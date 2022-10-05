"""
Write a function that takes in the heads of two Singly Linked lists that are in sorted order, respectively.
The function should merge the lists in place and return the head of the merged list; the merged list should be in
sorted order. Mutate the list in place.

"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Time: O(n + m) and Space: O(1)
    """
    Logic:
    Compare the current two node values of the lists, and whichever is smaller, append it as the next node of the
    resultant node.
    If one of the lists become None, then we break; and then append the rest of the remaining nodes of the list which
    still had some nodes to the resultant node.next

    """

    # Head of the resultant list.
    newHead = None
    # Used for traversing the resultant list
    currNode = None
    # Used for traversing the input linked list
    nodeOne = headOne
    nodeTwo = headTwo

    # We compare until both the nodes have values.
    while nodeOne and nodeTwo:
        # If node one is less than node two.
        if nodeOne.value <= nodeTwo.value:
            # If the resultant node is not initialized.
            if currNode is None:
                # We make the current node as the head and also currNode for traversing.
                newHead = nodeOne
                currNode = nodeOne
            else:
                # Else, we append the node to the resultant node's next pointer.
                currNode.next = nodeOne
                # Moving the resultant node
                currNode = currNode.next
            # Moving the smaller node
            nodeOne = nodeOne.next
        else:
            # Same thing happens when the node two is smaller than node one.
            if currNode is None:
                newHead = nodeTwo
                currNode = nodeTwo
            else:
                currNode.next = nodeTwo
                currNode = currNode.next
            nodeTwo = nodeTwo.next

    # Now we append all the remaining elements of the list which still has some nodes left.
    if nodeOne:
        currNode.next = nodeOne
    if nodeTwo:
        currNode.next = nodeTwo
    
    return newHead
