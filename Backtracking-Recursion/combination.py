"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

https://leetcode.com/problems/combinations/description/

The brute force approach would be to generate all possible pairs and then filter out duplicates and invalid combinations.
Time: O(n^k)
Space: O(k)

Optimized:
We only consider numbers greater than our last picked number (avoid duplicates)
We calculate the last possible starting number that could give us enough remaining numbers
We prune branches that can't possibly lead to valid combinations

Time Complexity: O(C(n,k)) - we only generate valid combinations
Space Complexity: O(k) - for the recursion stack

"""


def combine(n: int, k: int):
    # Total nums in the array
    nums = [i for i in range(1, n + 1)]
    result = []
    solve(nums, k, 0, [], result)
    return result


def solve(nums, k, idx, stack, result):
    # If we have k elements, we add to result and return
    if len(stack) == k:
        result.append(stack[:])
        return
    # We make recursive calls to all other elements from this index
    for i in range(idx, len(nums)):
        # Add the current element to the stack
        stack.append(nums[i])
        # Make the call starting from next index.
        solve(nums, k, i + 1, stack, result)
        # Removing the current element
        stack.pop()
