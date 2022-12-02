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
"""


def combinationSum(candidates, target: int):
	# Time: O(n!) and Space: O(n)
	"""
	Logic:
	The problem with doing recursion with all the numbers in every function call is that we will have duplicate
	results, ex: [2, 2, 3] and [2, 3, 2], but we want a combination where the order should not matter.
	So to avoid this issue, we will do recursion only from the current index onwards and not starting from 0th index
	of the array.
	"""
	# Storing the results
	result = []
	# Main call
	findComb(candidates, [], result, 0, target)

	return result


def findComb(candidates, stack, result, startIdx, remainingSum):
	# If the remaining sum is less than 0, then we return
	if remainingSum < 0:
		return
	# If the remaining sum is equal then we add the result
	if remainingSum == 0:
		result.append(stack[:])
		return
	# Making a call with all the numbers from index startIdx to the length of the array
	for i in range(startIdx, len(candidates)):
		# Appending the number to the stack, and making the call
		stack.append(candidates[i])
		# We subtract the current number from the remaining sum for the next call.
		findComb(candidates, stack, result, i, remainingSum - candidates[i])
		# Pop the added number, and move to the next number.
		stack.pop()
