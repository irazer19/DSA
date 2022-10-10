"""
Write a function that takes in the head of a Singly LinkedList and returns a boolean representing whether the
linked list's nodes form a palindrome. Your function shouldn't make use of any auxiliary data structure.

Input: 0 --> 1--> 2 --> 2 --> 1 --> 0
Output: True
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We first reach the middle of the linked list, then we reverse the second half of the linked list, and then
    compare the node values of the first half and the second half.

    To reach the middle of the linked list, we use two pointers, first: Moves by one step, and
    second: Moves by two steps. Now the moment the second pointer becomes None, we know that the first pointer has
    reached the middle of the linked list.

    """
    # Initializing the pointers.
    first = head
    second = head

    # Moving the first ptr until the second pointer becomes None.
    while second:
        first = first.next
        second = second.next
        # Taking another step only if the second ptr still exists.
        if second:
            second = second.next
    # Once we are out of loop, we reverse the second half of the list from the node where the first pointer ends.
    headTwo = reverseList(first)
    headOne = head
    # We compare the node values of the first and second half of the linked list for palindrome.
    while headOne and headTwo:
        # If not matching then return False.
        if headOne.value != headTwo.value:
            return False
        headOne = headOne.next
        headTwo = headTwo.next
    return True


def reverseList(head):
    # Basic reversing of the linked list
    node = head
    prev = None
    while node:
        nextNode = node.next
        node.next = prev
        prev = node
        node = nextNode
    return prev
