"""
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty
subsets whose sums are all equal.

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
"""


def canPartitionKSubsets(nums, k) -> bool:
	# Time: O(2^ (k*n)) and Space: O(k*n)
	"""
	Logic:
	First we find whether the sum can be divided into k, if yes then we process with the backtracking.
	We make function call and update the current sum until the current sum becomes equal to the target, where the
	target = total // k.
	Next, once we see that we have reached the target, then we will again start backtracking to find the same target
	using different set of numbers, and we do it until k == 0, meaning we have backtracked all the k sets where we
	found the target.
	While doing recursion, we will keep track of already used numbers so that for the next subset, we dont use them.

	"""
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
