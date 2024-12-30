"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

https://leetcode.com/problems/subarrays-with-k-different-integers/

Brute Force:
We try all possible subarrays by using two nested loops (start and end points)
For each subarray, we maintain a set of unique integers
If the set size equals k, we increment our counter
If set size exceeds k, we break the inner loop as any larger subarray will also have more than k distinct integers
Time Complexity: O(n²)
Space Complexity: O(k)

Optimized Solution (Sliding Window):
The key insight is that we can solve this using the difference between:
Number of subarrays with at most k distinct integers
Number of subarrays with at most (k-1) distinct integers

The atMostK helper function:
Uses a sliding window approach with two pointers (left and right)
Maintains a frequency map of integers in current window
When window has more than k distinct integers, shrinks from left
For each valid window, adds count of all possible subarrays ending at right pointer

Time Complexity: O(n)
Space Complexity: O(k)

Let me explain this key part of the sliding window solution with a detailed example.
When we have a valid window (a window with at most k distinct integers), right - left + 1 represents the count of all possible subarrays that:
- End at the current right pointer
- Have at most k distinct integers

Let's break this down with the example: nums = [1,2,1,2,3], k = 2
I'll show you step by step how the counting works when we have a valid window:

nums = [1,2,1,2,3]
# Let's say right pointer is at index 2 (value = 1)
# And left pointer is at index 0 (value = 1)
# Window is [1,2,1]

# Current window state:
# left = 0, right = 2
# right - left + 1 = 2 - 0 + 1 = 3

# This means we count these subarrays:
1. [1]       # subarray using just position 2
2. [2,1]     # subarray using positions 1,2
3. [1,2,1]   # subarray using positions 0,1,2

"""


def subarraysWithKDistinct(nums, k):
    return getKMostCount(nums, k) - getKMostCount(nums, k - 1)


def getKMostCount(nums, k):
    if k == 0:
        return 0

    count = 0
    left = 0
    freq = {}

    for right in range(len(nums)):
        # Add the right element to frequency map
        freq[nums[right]] = freq.get(nums[right], 0) + 1

        # Shrink window while we have more than k distinct integers
        while len(freq) > k:
            freq[nums[left]] -= 1
            if freq[nums[left]] == 0:
                del freq[nums[left]]
            left += 1

        # VERY IMPORTANT: Add count of all valid subarrays ending at **RIGHT** INDEX.
        count += right - left + 1

    return count
