"""
Write a function that takes in a sorted array of distinct integers and returns the first index in the array that
is equal to the value at that index. Your function should return the minimum index where index == array[index]

array = [-5, -3, 0, 3, 4, 5, 9]
expected = 3

"""


def indexEqualsValue(array):
    # Time: O(logn) and Space: O(1)
    """
    Logic:
    We will use modified binary search.
    If the mid == array[mid], then we will further explore the left side of the middle index to find the minimum index
    where mid == array[mid].

    We will move to the left half when the current value > current index, because since the elements are distinct,
    the next elements can never be equal to the index so right half can never have the result.
    """
    left = 0
    right = len(array) - 1
    # Default output if there is no match.
    firstIdx = -1
    while left <= right:
        mid = (left + right) // 2
        # If mid == array[mid]
        if array[mid] == mid:
            # We will update the result
            firstIdx = mid
            # We will move to the left so that we may find minimum index with mid == array[mid].
            right = mid - 1
        # Else, we will move to the left half, if the current value > current index, this condition will guarantee
        # that the right values of the array will always be greater than their indices.
        elif array[mid] > mid:
            right = mid - 1
        # Else, we will move the right half.
        else:
            left = mid + 1

    return firstIdx
