"""
Given an array of integers between 1 and n, inclusive, where n is the length of the array, write a function that
returns the first integer that appears more than once.

input = [2, 1, 5, 2, 3, 3, 4]
Output: 2

"""


def firstDuplicateValue(array):
    """
    Brute Force: Maintain a seen set, and check if the element is already in the set.
    Time: O(n) and Space: O(n)

    Optimized:
    Since all the integers in the array are positive, and between 1 and n, inclusive.
    As we iterate, we will mark the (current element value - 1) index of the array as negative.
    This way, if we ever encounter an element with index (value - 1) which is already negative,
    we will return that element.
    Time: O(n) and Space: O(1)
    """
    # For every element.
    for i in range(len(array)):
        # We will reduce the element value by 1 because if the element val = n, then we dont have nth index in the
        # array.
        idxToCheck = abs(array[i]) - 1
        # If this index element is already negative, we will return this element.
        if array[idxToCheck] < 0:
            return abs(array[i])
        # Else, we will mark it as negative.
        array[idxToCheck] *= -1
    # Default return.
    return -1
