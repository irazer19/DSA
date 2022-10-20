"""
Write a function that takes in an array of integers and returns an array of length 2 representing the largest
range of integers contained in that array.

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
output: [0, 7]

"""


def largestRange(array):
    # Time = Space = O(n)
    """
    Logic:
    For quick access, we will store all the numbers in a dictionary.
    Now for each element, we will consecutively expand to its left and right until the numbers are present in the
    array. After expanding to both the sides, if the current total length is greater than the existing length,
    then we will update it and also update the result range.
    As we visit the numbers, we will mark it as False because we had already computed the max range using it.
    """
    # Storing the numbers in the dictionary
    nums = {n: True for n in array}
    # To store the largest range.
    result = []
    largestLength = 0

    # For each element
    for n in array:
        # If the number is already visited, we'll move to next.
        if not nums[n]:
            continue
        # Mark it as visited
        nums[n] = False
        # Starting length of the range with just 1 element
        currLength = 1
        # Left and right values for expanding from the current position.
        leftVal = n - 1
        rightVal = n + 1
        # Expanding left and right
        while leftVal in nums:
            nums[leftVal] = False
            # Increasing the length
            currLength += 1
            leftVal -= 1
        # Expanding right
        while rightVal in nums:
            nums[rightVal] = False
            currLength += 1
            rightVal += 1
        # If the current length is greater than the largestLength, we will update it.
        if currLength > largestLength:
            largestLength = currLength
            # Updating the range
            result = [leftVal + 1, rightVal - 1]

    return result
