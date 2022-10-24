"""
Write a function that takes in a non-empty array of integers and returns the maximum sum that can be obtained
by summing up all of the integers in a non-empty subarray of the input array.

Input: [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4],
Output: 19

"""


def kadanesAlgorithm(array):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We will maintain a current sum as we iterate, and then check whether the current sum is less than the
    current array value, if yes then we will update the current sum.
    Then we will also update the max sum.
    """
    # Result
    maxSum = float('-inf')
    # Current sum
    currSum = 0
    # For each element
    for i in range(len(array)):
        # Adding the current value to the current sum
        currSum += array[i]
        # Updating the current sum, either the current sum is larger or the current value alone is bigger.
        currSum = max(currSum, array[i])
        # Updating the max sum
        maxSum = max(maxSum, currSum)
    return maxSum
