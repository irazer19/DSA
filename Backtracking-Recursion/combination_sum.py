"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

https://leetcode.com/problems/combination-sum/description/

Brute Force Solution:
Generate all combinations, and check which sum is equal to the target.
Time Complexity: O(n^k) where n is length of candidates and k is the maximum possible length of any combination
Space Complexity: O(k) for recursion stack

Optimized Solution:
The problem with doing recursion with all the numbers in every function call is that we will have duplicate
results, ex: [2, 2, 3] and [2, 3, 2], but we want a combination where the order should not matter.
So to avoid this issue, we will add the current index element to the stack and make a call again starting from
the same index, after the call is returned, we will pop that element and then again make a call to the next index
without adding the current element.
"""


def combinationSum(candidates, target: int):
    # Time: O(2^n) and Space: O(n)
    # Storing the results
    result = []
    # Main call
    findComb(candidates, [], result, 0, target)

    return result


def findComb(candidates, stack, result, startIdx, remainder):
    # Edge case
    if remainder < 0 or startIdx == len(candidates):
        return
    # Base case
    if remainder == 0:
        result.append(stack[:])
        return
    # Adding the current element to the stack
    stack.append(candidates[startIdx])
    # Calling the function starting from the same index since we can use the same number unlimited times.
    findComb(candidates, stack, result, startIdx, remainder - candidates[startIdx])
    stack.pop()
    # Calling the function without the current element.
    findComb(candidates, stack, result, startIdx + 1, remainder)
