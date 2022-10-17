"""
You're given an array of integers and an integer. Write a function that moves all instances of that integer in the
array to the end of the array. The function should perform this in place.

Input: [2, 1, 2, 2, 2, 3, 4, 2], toMove = 2
Output: [1, 3, 4, 2, 2, 2, 2, 2]

"""


def moveElementToEnd(array, toMove):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We'll use two pointers, one at the start and other at the end.
    The end pointer will track for thMove element, and the start pointer will keep other elements.
    We will move these pointers based on values found, and swap when needed.
    """
    # Initializing the pointers
    firstPtr = 0
    secondPtr = len(array) - 1

    while firstPtr < secondPtr:
        # If the last pointer already has the correct value, we move it.
        if array[secondPtr] == toMove:
            secondPtr -= 1
        # If the first pointer already has a correct value(other than toMove), then we move it.
        elif array[firstPtr] != toMove:
            firstPtr += 1
        # If the first pointer has toMove value, then we swap with the second pointer, and move both the pointers.
        elif array[firstPtr] == toMove:
            array[firstPtr], array[secondPtr] = array[secondPtr], array[firstPtr]
            firstPtr += 1
            secondPtr -= 1
    return array
