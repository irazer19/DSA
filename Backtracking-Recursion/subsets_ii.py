"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

https://leetcode.com/problems/subsets-ii/description/
"""


def subsetsWithDup(nums):
    # Time = Space = O(n * 2*n)
    """
    Logic:
    Since the nums contains duplicate values, while we do recursion we will make two calls,
    the first will be to the immediate next index, and then second will to the idx where the curr val != that idx value.
    We do it because we dont want duplicate set of result.

    """
    # Final result
    result = []
    # Sorting the numbers so that we can skip all the duplicates while traversing.
    nums.sort()
    # First function call starting from index 0
    solve(nums, 0, result, [])
    return result


def solve(nums, idx, result, stack):
    # Base case, if the index is out of bounds, we append the result.
    if idx > len(nums) - 1:
        result.append(stack[:])
        return
    # Current value
    currVal = nums[idx]
    # Appending the current value to the stack.
    stack.append(currVal)
    # Making the regular function call to the next index
    solve(nums, idx + 1, result, stack)
    # Removing the above appended value for making the next call.
    stack.pop()
    # Preparing for the next call, we will move the index until that element is != to the current value.
    while idx < len(nums) and nums[idx] == currVal:
        idx += 1
    # Making the second call to that index.
    solve(nums, idx, result, stack)
