"""
Write a function that takes in a sorted array of distinct integers as well as a target integer. The caveat is that
the integers in the array have been shifted by some amount; in other words, they've been moved to the left or to
the right by one more positions.
The function should use a variation of the binary search algorithm to determine if the target integer is contained
in the array and should return its index if it is, otherwise -1.

array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37], target = 33
Output: 8
"""


def shiftedBinarySearch(array, target):
    # Time: O(logn) and Space: O(1)
    """
    Logic:
    Since the array has been shifted, we will normally get the mid element of the array, and check which
    half of the array is in the sorted order (left or right). We will check whether the sorted half of the array
    can contain the target integer, if yes then we will move to that half.
    If no, then we will move the pointer to the unsorted half of the array.
    At every mid value, we will check whether its equal to the target integer.

    """
    # Using binary search, initializing left and right pointers.
    left = 0
    right = len(array) - 1
    while left <= right:
        # Getting the mid index
        mid = (left + right) // 2
        # If the mid = target, we found it.
        if array[mid] == target:
            return mid
        # Checking which side is sorted.
        # Condition is the left half is sorted.
        if array[left] <= array[mid]:
            # If the target is within the range of the left half, then we move there.
            if array[left] <= target < array[mid]:
                right = mid - 1
            else:
                # Else we move to the unsorted half.
                left = mid + 1
        # Else the right side is sorted.
        else:
            # If the target is within the range of the right half, then we move there.
            if array[mid] < target <= array[right]:
                left = mid + 1
            else:
                # Else we move to the unsorted half.
                right = mid - 1
    return -1
