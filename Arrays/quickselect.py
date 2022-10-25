"""
Write a function that takes in an array of distinct integers as well as an integer k and that returns the kth
smallest integer in that array.

array = [8, 5, 2, 9, 7, 6, 3], k = 3
Output: 5
"""


def quickselect(array, k):
    # Best = Average = O(n) time | O(1) space
    # Worst: O(n^2) time | O(1) space.
    """
    Logic:
    We will use Quick Sort algorithm to solve this.
    First we will start with the entire array, and then apply quick sort algorithm. The rightidx where we will
    swap it with the pivot, we will check whether the rightidx = k, if yes then return this value, else
    we will move to the that half of the array where k can be found.

    """
    return quickSelectHelper(array, 0, len(array) - 1, k)


def quickSelectHelper(array, start, end, k):
    # Outer loop is for again doing the quick sort on the shrinked array which would contain kth position.
    while True:
        if start > end:
            return -1
        # Basic Quick sort
        pivot = start
        left = start + 1
        right = end
        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                array[left], array[right] = array[right], array[left]
            if array[left] <= array[pivot]:
                left += 1
            if array[right] >= array[pivot]:
                right -= 1
        # At this point we swap the pivot with the right idx, which means the right idx has its correct value.
        array[pivot], array[right] = array[right], array[pivot]
        # If this right idx = the kth position, we return it.
        if right == k - 1:
            return array[right]
        # Else if the kth position is greater than the right idx, we use only the right half of the array,
        # and do quick sort again.
        elif right < k - 1:
            start = right + 1
        else:
            # Else if the kth position is less than the right idx, we use the left half of the array.
            end = right - 1
