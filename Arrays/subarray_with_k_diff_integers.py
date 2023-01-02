"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
"""

from collections import defaultdict


def subarraysWithKDistinct(nums, k):
	# Time = Space = O(n)
	"""
	Logic:
	We will first get all the subarrays with at most k distinct elements.
	Then get all the subarrays with at most k-1 distinct elements.
	Now we will subtract result(k) - result(k-1) to get the answer.
	"""
	return getKMostCount(nums, k) - getKMostCount(nums, k - 1)


def getKMostCount(nums, k):
	# We track the frequency of the letters we encounter
	counter = defaultdict(int)
	# start of the window
	left = 0
	# Stores all the subarrays with at most k distinct elements
	result = 0
	# This is the end window
	for right, num in enumerate(nums):
		# Increasing the frequency of this letter
		counter[num] += 1
		# Now if we have more than k distinct letters in the dictionary, then we will shrink the subarray window
		# by increasing the left counter.
		while len(counter) > k:
			# Decreasing the frequency of this letter
			counter[nums[left]] -= 1
			# If the freq becomes 0, then we pop out the letter
			if counter[nums[left]] == 0:
				del counter[nums[left]]
			# Shrinking the window size
			left += 1
		# This is the tricky part.
		# We store all the possible subarrays within the window [left, right], and we can get that by
		# continuously storing the length of the window at each result
		result += right - left + 1

	return result
