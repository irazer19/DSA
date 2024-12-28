"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Input : arr[] = {10, 2, -2, -20, 10}, k = -10
Output : 3

https://leetcode.com/problems/subarray-sum-equals-k/description/

Brute Force Solution:
The brute force approach involves checking all possible subarrays and counting those with sum equal to k.
Time Complexity: O(n²)
Space Complexity: O(1)

Optimized Solution:
A prefix sum (also called cumulative sum) is a running total of numbers in an array from the beginning up to each position.
If we have two prefix sums (cumulative sums) P1 and P2, and their difference (P2 - P1) equals k, then the subarray between these positions must sum to k.
In other words:

If currentSum - k exists in our hashmap, it means we found a subarray with sum k
The value in hashmap tells us how many times we've seen that prefix sum before, which equals the number of valid subarrays ending at current position

This turns "finding subarrays with sum k" into "finding pairs of prefix sums with difference k", making it O(n) with a hashmap lookup.
Time = Space = O(n)
"""


def subarraySum_optimized(nums, k):
    count = 0
    curr_sum = 0
    # Dictionary to store prefix sum frequencies
    prefix_sum = {0: 1}  # Initialize with 0 sum having frequency 1

    for num in nums:
        curr_sum += num
        # If (curr_sum - k) exists in prefix_sum,
        # it means we have found subarrays with sum k
        if curr_sum - k in prefix_sum:
            count += prefix_sum[curr_sum - k]
        # Update prefix_sum frequency
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

    return count
