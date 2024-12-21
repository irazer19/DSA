"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

https://leetcode.com/problems/find-k-closest-elements/

"""


def findClosestElements(arr, k, x):
    """
    Brute Force:
    For each number in the array:
    1. Calculate its distance from x
    2. Store both the distance and the original number as a tuple
    3. Sort the tuples based on the distance
    4. Return the first k elements in sorted order.
    Time: O(nlogn) and Space: O(n)

    Optimized:
    The key intuition is that we're sliding a window of size k through the array and using binary search to efficiently
    find the best position where the elements in the window have the closest distance to the target x.

    Time: O(logn) and Space: O(1)
    """
    if k >= len(arr):
        return arr

    # Initialize left and right pointers for binary search
    # Right pointer is len(arr)-k because we need k elements if we assume the mid to be the start of the window
    left = 0
    right = len(arr) - k

    # Binary search to find the starting position of k elements
    while left < right:
        mid = (left + right) // 2
        # Lets assume that the mid element is the start of the window, and the next k elements are the part of the result, where
        # the last element in the mid + k if the last element of the window.
        # Now if the first element of the window is > the last element of the window then we know we can move the windo
        # to the right since the absolute distance is less towards the right.
        # If x-arr[mid] > arr[mid+k]-x, we should move window to right
        if abs(x - arr[mid]) > abs(arr[mid + k] - x):
            left = mid + 1
        else:
            right = mid

    # Return k elements starting from the found start position
    return arr[left : left + k]
