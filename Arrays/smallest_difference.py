"""
Write a function that takes in two non-empty arrays of integers, finds the pair of numbers whose absolute difference
is closest to zero, and returns an array containing these two numbers, with the number from the first array in the
first position.

Input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Output: [28, 26]

"""


def smallestDifference(arrayOne, arrayTwo):
    # Time: O(nlogn + mlogm) and Space: O(1)
    """
    Logic:
    Sort the input arrays, use pointers to compare the absolute difference.
    Since we want the smallest absolute difference, to make the diff closer to zero, after comparing the
    values, we will move the smaller values pointer so that the difference reduces.
    If a pointer is already at the end of the array, we will move the other pointer.
    """
    # Sorting the arrays
    arrayOne.sort()
    arrayTwo.sort()
    # Pointers for each array
    idxOne = 0
    idxTwo = 0
    # Tracking the smallest difference
    diff = float('inf')
    # Result
    result = [-1, -1]

    # Until both the pointers are within the array range
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        # Getting the current diff
        currDiff = abs(arrayOne[idxOne] - arrayTwo[idxTwo])
        # Updating the result if the current diff is smaller.
        if currDiff < diff:
            diff = currDiff
            result = [arrayOne[idxOne], arrayTwo[idxTwo]]

        # If the arrayTwo value is smaller
        if arrayOne[idxOne] > arrayTwo[idxTwo]:
            # If the arrayTwo is already at the end of the array, we will move arrayOne's pointer
            if idxTwo == len(arrayTwo) - 1:
                idxOne += 1
            else:
                # Else lets move the arrayTwo
                idxTwo += 1
        elif arrayOne[idxOne] < arrayTwo[idxTwo]:
            # If the arrayOne is already at the end of the array, we will move arrayTwo's pointer
            if idxOne == len(arrayOne) - 1:
                idxTwo += 1
            else:
                idxOne += 1
        else:
            # Case where the diff is zero, we just return the result.
            return [arrayOne[idxOne], arrayTwo[idxTwo]]
        
        return result
