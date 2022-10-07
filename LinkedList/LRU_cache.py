"""
Implement an LRUCache class for a Least Recently Used (LRU) cache. The class should support:
• Inserting key-value pairs with the insertKeyValuePair method.
• Retrieving a key's value with the getValueFromkey method.
• Retrieving the most recently used (the most recently inserted or retrieved) key with the getMostRecentkey method.
Each of these methods should run in constant time.
Additionally, the LRUCache class should store a maxSize property set to the size of the cache, which is passed in as an
argument! during instantiation. This size represents the maximum number of key-value pairs that the cache can store at
once. If a key-value pair is inserted in the cache when it has reached maximum capacity, the least recently used
key-value pair should be evicted from the cache and no longer retrievable; the newly added key-value pair should
effectively replace it.
Note that inserting a key-value pair with an already existing key should simply replace the key's value in the cache
with the new value and shouldn't evict a key-value pair if the cache is full. Lastly, attempting to retrieve a value
from a key that isn't in the cache should return None / null .

"""


# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        # Time = Space = O(1)
        self.maxSize = maxSize or 1
        self.currSize = 0  # Tracks the current size of the LinkedList
        self.head = None  # Stores the current head of the linked list
        self.tail = None  # Stores the current tail of the linked list
        self.lruDict = {}  # Stores the given key with the value as the Node object

    def insertKeyValuePair(self, key, value):
        # If head does not exist, we create it.
        if not self.head:
            self.handleEmptyList(key, value)

        # If the key already exists, we only update its value and then make it a head.
        elif self.lruDict.get(key, None):
            self.lruDict[key].value = value
            self.makeHead(self.lruDict[key])

        else:
            # Else, this item is new in the linked list.
            # First we check whether the LRU is full to its capacity.
            if self.currSize == self.maxSize:
                # Remove the tail from dictionary and linkedlist because its the least recently used.
                self.lruDict.pop(self.tail.key)
                self.removeTail()
                # Decrease the total size of the linked list counter
                self.currSize -= 1
            # Now if the head does not exists in case, then we create it.
            if not self.head:
                self.handleEmptyList(key, value)
            else:
                # Else, we create a new node item
                node = Node(key, value)
                # Add the item to the list, and make it the tail.
                self.tail.next = node
                self.tail.next.prev = self.tail
                self.tail = self.tail.next
                # Now since we added this item, we make it the new head as a recent item.
                self.makeHead(self.tail)
                # Add the item in the dictionary
                self.lruDict[key] = node
                # Increment the current list size counter.
                self.currSize += 1

    def getValueFromKey(self, key):
        # We check whether the key is already in the dictionary, if yes then we return its value and also make it
        # the head, else we return None.
        node = self.lruDict.get(key, None)
        if node:
            self.makeHead(node)
            return node.value
        else:
            return None

    def getMostRecentKey(self):
        # We return the head's key of the list.
        if self.head:
            return self.head.key
        return None

    def makeHead(self, node):
        # Method used to make the given node as head.
        # Case 1: The node is already a head.
        if node == self.head:
            return
        # Case 2: The node is a tail
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            # Case 3: The node is is between the head and the tail.
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node

    def removeTail(self):
        # Removes the tail from the linked list.
        # Case 1: The tail and head are the same.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            # Case 2: We simply make the 2nd last node as the tail.
            newTail = self.tail.prev
            newTail.next = None
            self.tail = newTail

    def handleEmptyList(self, key, value):
        # Method which initializes the linked list by setting the head and tail.
        node = Node(key, value)
        self.head = node
        self.tail = node
        # Also, inserts the given item in the dictionary
        self.lruDict[key] = node
        self.currSize += 1


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
