"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in
candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[[1,1,6], [1,2,5], [1,7], [2,6]]

https://leetcode.com/problems/combination-sum-ii/

"""


def combinationSum2(candidates, target):
    # Time: O(2^n) and Space: O(number of combinations + n)
    """
    Logic:
    We will either include an element or move to the next index without adding that element in the stack.
    Because we can have duplicate elements, we will sort the input array, and for the second function call, we will
    move to the index where is element is not the same as the current index element.
    If the sum of the stack == target, we will the result and return.

    """
    # Sorting the input array
    candidates.sort()
    # Result
    result = []
    solve(candidates, target, 0, [], result)
    return result


def solve(candidates, target, idx, stack, result):
    # Base case
    if sum(stack) == target:
        result.append(stack[:])
        return
    # Base case
    if idx >= len(candidates) or sum(stack) > target:
        return
    # Getting the current element
    currVal = candidates[idx]
    # Adding this element to the stack and moving to the next index.
    stack.append(currVal)
    solve(candidates, target, idx + 1, stack, result)
    stack.pop()
    # Now for the next call, we will not include the current element, and move to the element which is not equal to
    # the current element.
    while idx < len(candidates) and candidates[idx] == currVal:
        idx += 1
    solve(candidates, target, idx, stack, result)
