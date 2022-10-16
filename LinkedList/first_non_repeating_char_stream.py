"""
Find first non-repeating character from a stream of characters

Input: abcabc
Output: ['a', 'a', 'a', 'b', 'c']

"""


def firstNonRepeatingCharStream(stream):
    # Time: O(n) and Space: O(1), if the letters are from a-z
    # Query time of non-repeating character is O(1)
    """
    Logic:
    As we get new letters, we will maintain a doubly linked list which will store the non-repeating character at the
    head. If an upcoming character is already in the linkedlist, then we will remove that node from the linkedlist
    because the current character make it a repeating character.
    To access the node, we will store all list nodes in a hashtable.
    Also, we will store the frequency of the characters in a hashtable to check whether a char is repeating.

    """
    # Hashtable to store the frequency of the characters in
    charFreq = {}
    # Hashtable to store the nodes of characters.
    charNodes = {}
    # Initializing the linked list
    linkedList = LinkedList()
    # Result which will contain non-repeating characters at every point of stream
    result = []
    # Starting index for iteration in the stream.
    idx = 0
    while idx < len(stream):
        # Getting the char
        char = stream[idx]
        # If the head and tail or the list is not initialized, then we create it.
        if not linkedList.head and not linkedList.tail:
            newNode = Node(char)
            linkedList.head = newNode
            linkedList.tail = newNode
            charFreq[char] = 1
            charNodes[char] = newNode
        else:
            # If this character is new, then we add it to the end of the list.
            if char not in charFreq:
                # Creating a new node.
                newNode = Node(char)
                charFreq[char] = 1
                charNodes[char] = newNode
                # Adding the node char to the list.
                linkedList.tail.next = newNode
                newNode.prev = linkedList.tail
                # Updating the tail.
                linkedList.tail = linkedList.tail.next
            elif charFreq[char] == 1:
                # If the character is already in the list, we will remove it from all the hashtable and the linkedList.
                charFreq.pop(char)
                charNode = charNodes.pop(char)
                linkedList.removeNode(charNode)
        # Moving to the next stream of character.
        idx += 1
        # Adding to the result.
        if linkedList.head:
            result.append(linkedList.head.value)
    return result


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def removeNode(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:
            newTail = self.tail.prev
            newTail.next = None
            self.tail = newTail
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


print(firstNonRepeatingCharStream('abcabc'))
