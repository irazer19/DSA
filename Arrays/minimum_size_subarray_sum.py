"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose
sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""


def minSubArrayLen(target, nums) -> int:
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We will use the start and end index as the window size. We will also maintain a current sum variable.
    Now as we move the end pointer, we will keep adding the new element to the current sum, once the current sum
    becomes greater than or equal to target, we will update the result and then try to shrink the window
    by incrementing the start pointer until the above condition remains true.
    """
    # Tracking the running sum
    currSum = 0
    # Window pointers
    start = 0
    end = 0
    # Result
    smallest = float("inf")
    # Traversing the full array
    while end < len(nums):
        # Updating the current sum with the current element.
        currSum += nums[end]
        # Until the current sum >= target
        while currSum >= target:
            # Keep updating the result
            smallest = min(smallest, end - start + 1)
            # Shrink the window size by subtracting the start pointer element from the current sum
            currSum -= nums[start]
            # Moving the start pointer to the next index.
            start += 1
        # We will anyways, keep moving forward.
        end += 1
    # result
    return 0 if smallest == float("inf") else smallest
