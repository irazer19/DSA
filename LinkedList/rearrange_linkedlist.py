"""
Write a function that takes in the head of a Singly Linked List and an integer k , rearranges the list in place
(i.e., doesn't create a brand new list) around nodes with value k , and returns its new head.
Rearranging a Linked List around nodes with value k means moving all nodes with a value smaller than k before all
nodes with value k and moving all nodes with a value greater than k after all nodes with value k.
All moved nodes should maintain their original relative ordering if possible.
Note that the linked list should be rearranged even if it doesn't have any nodes with value k.

head = 3 --> 0 --> 5 --> 2 --> 1 --> 4
k = 3

Output: 0 --> 2 --> 1 --> 3 --> 5 --> 4

"""


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We will maintain three node references,
    1. nodeSmaller = All the nodes that are smaller than k.
    2. nodeK = All the nodes with value k.
    3. nodeGreater = All the nodes with value greater than k.

    We will traverse the linked list once, and connect the respective nodes in the above reference pointers.
    Once we are done traversing, we will join the smaller node --> nodeK --> greater nodes, and this will be our
    result.
    """

    # Connects all the nodes which are smaller than k.
    nodeSmaller = None
    # Connects all the nodes which are equal to k.
    nodeK = None
    # Connects all the nodes which are greater than k.
    nodeGreater = None

    # Stores the head node of the above lists
    nodeSmallerHead = None
    nodeGreaterHead = None
    nodeKHead = None
    # node for traversing the linked list
    node = head

    # Traversing the list
    while node:
        # If the current node is less than k.
        if node.value < k:
            # We will connect all such nodes in the same order.
            if not nodeSmallerHead:
                nodeSmaller = node
                nodeSmallerHead = node
            else:
                nodeSmaller.next = node
                nodeSmaller = nodeSmaller.next
        elif node.value > k:
            # If the current node is greater than k.
            if not nodeGreaterHead:
                nodeGreater = node
                nodeGreaterHead = node
            else:
                nodeGreater.next = node
                nodeGreater = nodeGreater.next
        else:
            # If the current node is equal to k.
            if not nodeKHead:
                nodeK = node
                nodeKHead = node
            else:
                nodeK.next = node
                nodeK = nodeK.next
        # Moving to the next node.
        node = node.next

    # Once we are out of the while loop.
    # If the node reference which has value greater than k exists, then we point its tail to None as that is the
    # end of our new list.
    if nodeGreater:
        nodeGreater.next = None
    # If we have nodes with values smaller than k.
    if nodeSmallerHead:
        # If there are nodes with value equal to k.
        if nodeKHead:
            # We will connect all the three references.
            nodeSmaller.next = nodeKHead
            nodeK.next = nodeGreaterHead
            return nodeSmallerHead
        else:
            # Else, we will connect smaller and greater references only.
            nodeSmaller.next = nodeGreaterHead
            return nodeSmallerHead
    elif nodeKHead:
        # Here we will only connect the node reference equal to k with the node reference greater than k.
        nodeK.next = nodeGreaterHead
        return nodeKHead
    else:
        # Else, if both smaller and equal reference are None, then we return whatever is the value of
        # the greater node reference.
        return nodeGreaterHead
