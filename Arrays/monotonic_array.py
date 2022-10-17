"""
Write a function that takes in an array of integers and returns a boolean representing whether the array is
monotonic.
An array is said to be monotonic if its elements, from left to right are entirely non-increasing or entirely
non-decreasing.

array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Output: True

"""


def isMonotonic(array):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We will create two variables isIncreasing and isDecreasing, while iterating through the array, if both
    the variables are True, then we know that the array is not monotonic.
    """
    # Tracking increasing and decreasing values.
    isIncreasing = None
    isDecreasing = None

    for i in range(len(array) - 1):
        # If its increasing, then we set the isIncreasing to True
        if array[i] < array[i + 1]:
            isIncreasing = True
        # If its decreasing, then we set the isDecreasing to True
        elif array[i] > array[i + 1]:
            isDecreasing = True
    # If both are True, then we return False
    if isIncreasing == isDecreasing == True:
        return False
    return True
