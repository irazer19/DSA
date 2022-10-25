"""
Write a function that takes in a sorted array of integers as well as a target integer. The function should use a
variation of the Binary Search algorithm to find a range of indices in between which the target number is contained in
the array and should return this range in the form of an array.

The first number in the output array should represent the first index at which the target number is located, while the
second number should represent the last index at which the target number is located. The function should return
[-1, -1] if the integer isn't contained in the array.

If you're unfamiliar with Binary Search, we recommend watching the Conceptual Overview section of the Binary Search
question's video! explanation before starting to code.

array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], target = 45
Output: [4, 9]

"""


def searchForRange(array, target):
    # Time: O(logn) and Space: O(1)
    """
    Logic:
    For a given target, we have to find the first occurrence and its last occurrence in the array.
    To find the first occurrence, we will do a binary search, where if we find the target, we will try moving to
    the left if possible to find the left most occurrence of it.
    Similarly, we will do it for the last occurrence, where we will try to move to the right if possible.
    Finally, we will return the output of left most occurrence and right most occurrence of the target.
    """
    # Finding the leftmost occurrence of the target.
    leftIdx = search(array, target, True)
    # Finding the rightmost occurrence of the target.
    rightIdx = search(array, target, False)

    return [leftIdx, rightIdx]


def search(array, target, leftMost):
    # Basic binary search with slight modification if the target == current mid value.
    left = 0
    right = len(array) - 1
    # This is the default index we will return if we dont find the target at all in the array.
    idx = -1

    while left <= right:
        mid = (left + right) // 2
        if target < array[mid]:
            right = mid - 1
        elif target > array[mid]:
            left = mid + 1
        else:
            # This part is slightly different
            # Storing the index in the result
            idx = mid
            # Then if we are moving to the left,
            if leftMost:
                # If the index can be moved to the left, and the left value == target, then we move to the left half.
                if mid > 0 and array[mid - 1] == target:
                    right = mid - 1
                else:
                    # Else, we will break out since there are no more occurrence of the target to the left.
                    break
            else:
                # Else we are moving to the right.
                # If the next right value == target, then we move to the right half.
                if mid < len(array) - 1 and array[mid + 1] == target:
                    left = mid + 1
                else:
                    # Else, we break because there are no more occurrence of the target to the right
                    break
    # Returning the index of the target found, either leftmost index or the rightmost index.
    return idx
