"""
Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
Note that:
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the
order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].

https://leetcode.com/problems/longest-arithmetic-subsequence/description/
"""


def longestArithSeqLength(nums):
    # Time = Space = O(n^2)
    """
    Logic:
    At every index, we check whether we already have the current difference which ends at ith index, if yes then we
    add 1 +  whatever we found in the dictionary.
    If no, then we add (diff, jth index) = 1 in the dictionary
    """
    # Stores total subsequence count for (current diff, end index)
    dp = {}
    result = 0
    # We find the difference for each and every array element
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Current diff between ith and jth index elements
            diff = nums[j] - nums[i]
            # If we already have this difference ending at ith index previously
            if dp.get((diff, i), None):
                # We add 1 + whatever we found in the dictionary
                dp[(diff, j)] = 1 + dp.get((diff, i))
            else:
                # Else, we add a 2 because of ith and jth elements
                dp[(diff, j)] = 2
            # Updating the result
            result = max(result, dp[(diff, j)])
    return result
