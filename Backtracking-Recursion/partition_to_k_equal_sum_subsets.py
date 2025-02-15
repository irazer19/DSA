"""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty
subsets whose sums are all equal.

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/

Brute Force:
Find the target sum for each subset (total sum / k)
Try all possible combinations to create k subsets
Check if we can make k subsets with equal sums
Time Complexity: O(k * 2^n), where n is the length of nums
Space Complexity: O(n) for recursion stack

Optimized:
First we find whether the sum can be divided into k, if yes then we process with the backtracking.
We make function call and update the current sum until the current sum becomes equal to the target, where the
target = total // k.
Next, once we see that we have reached the target, then we will again start backtracking to find the same target
using different set of numbers, and we do it until k == 0, meaning we have backtracked all the k sets where we
found the target.
While doing recursion, we will keep track of already used numbers so that for the next subset, we dont use them.

Time Complexity Analysis:

Initial sort: O(n log n)
Main recursive function (solve):

For each subset (k), we try each number in the array (n)
For each number, we can either include it or exclude it
At each step, we make 2 choices (include/exclude)
The recursion tree has a maximum depth of n

Therefore, for the recursive portion:

Each number has 2 choices
We have n numbers
This creates a recursive tree of size O(2^n)
We do this k times for each subset

The total time complexity is O(k * 2^n)
Space: O(n)
"""


def canPartitionKSubsets(nums, k) -> bool:
    # Edge case
    if sum(nums) % k != 0:
        return False
    # Helps in faster calculation
    nums.sort(reverse=True)
    # Tracking the used numbers inside backtracking
    used = [False for _ in nums]
    # Target sum for each set.
    target = sum(nums) // k
    return solve(nums, k, target, 0, 0, used)


def solve(nums, k, target, idx, currSum, used):
    # Base case, if we have check all the subsets where the target sum was present, we return true
    if k == 0:
        return True
    # If we reach the target sum, we start to find the next subset with different numbers, so we reset the current
    # sum to 0.
    if target == currSum:
        k -= 1
        return solve(nums, k, target, 0, 0, used)
    # We try with all the numbers starting from idx
    for i in range(idx, len(nums)):
        # current value
        val = nums[i]
        # IF we have already used this value, or the total > target, we move to the next element.
        if used[i] or val + currSum > target:
            continue
        # Mark it as used
        used[i] = True
        # Calling the function with the next index and update current sum
        if solve(nums, k, target, i + 1, currSum + val, used):
            return True
        # If we didnt get the result from above, then we unmark this element and move to the next element.
        used[i] = False
    # Return False by default
    return False
