# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Time = Space = max(n, m), n and me are the length of the linked list one and two.
    """
    Logic:
    We will maintain a new head of a linked list, the first node will be a dummy node.
    We will also have a carry variable.
    Next, we will start with head of both the linked lists, and sum the node values along with the carry.
    We calculate the carry by (total sum) // 10, and the value to be printed by (total sum) % 10.
    We create a new node for the value to be printed, and add it the next pointer of the current node.

    """
    one = linkedListOne
    two = linkedListTwo

    # Initializing the carry
    carry = 0
    node = None
    # Dummy node.
    head = LinkedList(-1)
    # If either of the three. node one, node two or carry exists, then we will add the sum and create a new node.
    while one or two or carry != 0:
        # Getting the value one.
        valOne = one.value if one else 0
        # Getting the value two.
        valTwo = two.value if two else 0
        # Calculating the total sum of all three
        total = valOne + valTwo + carry
        # Then getting the carry from the above sum
        carry = total // 10
        # Getting the remainder to be printed for the above sum
        remainder = total % 10
        # If this is the first node, then we just create it and also add it to the result head.
        if not node:
            node = LinkedList(remainder)
            head.next = node
        else:
            # Else, we create a new node, and push it as the next node.
            node.next = LinkedList(remainder)
            node = node.next
        # If node one exists, then we move to next node.
        if one:
            one = one.next
        if two:
            # If two nodes exist, then we move to the next node
            two = two.next
    # Returning the result except the first node which is a dummy node.
    return head.next
