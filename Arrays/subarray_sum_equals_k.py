"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
Input : arr[] = {10, 2, -2, -20, 10}, k = -10
Output : 3
"""


def subarraySum(nums, k) -> int:
	# Time = Space = O(n)
	"""
	Logic:
	We will maintain a hashtable which will store all the sums which we compute and its frequency.
	We will loop over every number and add it the current sum, if the currentSum - target which is the remainder
	present in the hashtable, then we will add the result by adding the frequency of the remainder, meaning that
	if we have r remainders then we know that there are r subarrays which can add upto the target.
	"""
	# Current sum
	currSum = 0
	# We always will have the sum=0 so we add it by default.
	sumFrequency = {0: 1}
	# Result
	totalSubarrays = 0
	# For each number
	for n in nums:
		# Adding it to the current sum
		currSum += n
		# Getting the remainder
		remainder = currSum - k
		# If the remainder is present in the hastable
		if remainder in sumFrequency:
			# Updating the result by the remainder's frequency
			totalSubarrays += sumFrequency[remainder]
		# If the current sum is already in the hashtable, then we update its frequency by 1.
		if currSum in sumFrequency:
			sumFrequency[currSum] += 1
		else:
			# Else we create a new key for the current sum
			sumFrequency[currSum] = 1

	return totalSubarrays
