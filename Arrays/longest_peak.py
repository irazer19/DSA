"""
Write a function that takes in an array of integers and returns the length of the longest peak in the array.

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
OutPut: 6

https://leetcode.com/problems/longest-mountain-in-array/description/
"""


def longestPeakInArray(array):
    """
    Brute Force:
    Generate all substring and then check if it is a peak.
    Time: O(n^3) and Space: O(1)

    Logic:
    As we iterate over the array, we will check whether the current element is a peak.
    If yes, then we will expand to the left and right and calculate the peak size and update the result.
    If no, then we will move to the next element.
    Time: O(n) and Space: O(1)
    """
    # Stores the result
    longestPeak = 0
    # We start from index 1, since the first element cannot be a peak.
    currIdx = 1

    # Iterate over the array except for the last element.
    while currIdx < len(array) - 1:
        # If the current element is a peak.
        isPeak = array[currIdx - 1] < array[currIdx] > array[currIdx + 1]

        # If peak
        if isPeak:
            # Expanding left
            # We compare the ith element to the ith + 1 element.
            leftIdx = currIdx - 1
            while leftIdx >= 0:
                # If the current index element is greater or equal to its next element, then we break
                # because the left peak ends.
                if array[leftIdx] >= array[leftIdx + 1]:
                    break
                leftIdx -= 1
            # Getting the total left peak size.
            leftTotal = currIdx - leftIdx - 1

            # Expanding right
            # We compare the ith element to the ith - 1 element.
            rightIdx = currIdx + 1
            while rightIdx < len(array):
                if array[rightIdx] >= array[rightIdx - 1]:
                    break
                rightIdx += 1
            # Getting the total right peak size.
            rightTotal = rightIdx - currIdx - 1
            # Updating the longestPeak result.
            longestPeak = max(longestPeak, leftTotal + rightTotal + 1)
            # We will directly move the pointer to the rightIdx because all the other elements in between
            # were a part of another peak so they cannot be a peak.
            currIdx = rightIdx
        else:
            # Else, we move to the next element
            currIdx += 1

    return longestPeak
