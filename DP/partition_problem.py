"""
Given a non-empty array nums containing only positive integers, find if the array can be
partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

https://leetcode.com/problems/partition-equal-subset-sum/description/
"""


def canPartition_bruteforce(nums):
    """
    Brute force solution using recursive backtracking
    Time Complexity: O(2^n) where n is the length of nums
    Space Complexity: O(n) due to recursion stack

    If we add memoization, and cache [index, current_sum] = True/False, then we can save time to O(n * sum)
    """
    total_sum = sum(nums)

    # If total sum is odd, we cannot partition into equal subsets
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    def backtrack(index, current_sum):
        # Base cases
        if current_sum == target:
            return True
        if current_sum > target or index >= len(nums):
            return False

        # Try including the current number
        if backtrack(index + 1, current_sum + nums[index]):
            return True

        # Try excluding the current number
        if backtrack(index + 1, current_sum):
            return True

        return False

    return backtrack(0, 0)


def partition(arr):
    # Time = Space = O(n x m), n = array length and m = total / 2
    # This problem is same as Subset Sum problem, where n is already given.
    # Since we have to divide the array into two subsets having equal sum, we will first calculate the total sum.
    total = sum(arr)
    # Now if the total sum is an Odd number then we cannot equally divide it into two subsets.
    if total % 2 != 0:
        return False
    # Now we find the sum "n" which each subset will sum upto.
    # Logic: If we find a subset having sum == n, then we are sure that rest of the elements will also sum upto n
    # because n + n = total
    n = total // 2
    # Using DP, we create a matrix where, rows = array elements and columns = [0, n], n is inclusive.
    # Each cell represents: "Whether it's possible to make current sum j using all the elements till i.
    store = [[False for _ in range(n + 1)] for _ in range(len(arr) + 1)]
    # For the first columns which is sum=0, it is possible to make because we will not add any elements.
    for i in range(len(store)):
        store[i][0] = True

    # For each element
    for i in range(1, len(store)):
        # For each sum j
        for j in range(1, len(store[0])):
            # If the current element value > current sum j
            if j >= arr[i - 1]:
                # If the previous row value is True then we simply store it (Ignoring current element) OR
                # If the we add this current element value and check whether the remainder was True
                # IF either one of is True then we will consider it.
                store[i][j] = store[i - 1][j] or store[i - 1][j - arr[i - 1]]
            else:
                # Using the previous rows result
                store[i][j] = store[i - 1][j]
    return store[-1][-1]


print(partition([1, 2, 3, 5]))
