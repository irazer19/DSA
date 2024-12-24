"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
array = [8, -8, 9, -9, 10, -11, 12]
Output: 22

https://leetcode.com/problems/maximum-sum-circular-subarray/description/

Brute Force:
- Checking all possible starting positions in the array
- For each starting position, trying all possible subarray lengths
- For each length, calculating the sum by wrapping around the array using modulo
- Keeping track of the maximum sum found
Time Complexity: O(n^2)
Space Complexity: O(1)

Optimized:
1. The maximum sum subarray in a circular array can be one of two cases:
   - Case 1: A regular subarray (no wrapping) -> Use standard Kadane's
   - Case 2: A wrapped subarray -> Use (Total Sum - Minimum Subarray Sum)

2. For Case 2, the wrapped maximum sum is equivalent to:
   Total Sum - Minimum Subarray Sum
   Because removing the minimum subarray from the total gives us the wrapped maximum

3. Special Case: If all numbers are negative:
   - Both Case 1 and Case 2 would give wrong results
   - We should return the maximum element (least negative)
Time Complexity: O(n)
Space Complexity: O(n)

"""


def maxSumCircularSubarray(array):
    # Edge case. If all the elements in the array are negative, then we simply return the max from them.
    allNegative = True
    for n in array:
        if n >= 0:
            allNegative = False
            break
    if allNegative:
        return max(array)

    # Using regular Kadanes Algorithm
    maxSumOne = kadanesAlgorithm(array)

    # Modified version of the kadanes algorithm.
    # Getting the total sum
    total = sum(array)
    # Inverting the sign of each element
    invertedArray = [n * -1 for n in array]
    # Subtracting the result from the total, i.e total - (-min_sum)
    maxSumTwo = total + kadanesAlgorithm(invertedArray)
    # Returning the max of the above two result
    return max(maxSumOne, maxSumTwo)


def kadanesAlgorithm(array):
    # Simple kadanes algorithm.
    maxSum = float("-inf")
    currSum = float("-inf")
    for n in array:
        currSum = max(currSum + n, n)
        maxSum = max(maxSum, currSum)
    return maxSum


print(maxSumCircularSubarray([-10, -7, 9, -7, 6, 9, -9, -4, -8, -5]))
