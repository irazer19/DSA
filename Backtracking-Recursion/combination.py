"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
"""


def combine(n: int, k: int):
	# Time = Space = O(k * c(n, k)), where c is the total number of combinations
	"""
	Logic:
	We make recursive calls from each index to all other elements until the result stack contains k elements in it, once
	we have k elements, we add to the final result array and return.

	"""
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
