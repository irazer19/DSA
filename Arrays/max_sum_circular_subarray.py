"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
array = [8, -8, 9, -9, 10, -11, 12]
Output: 22

"""


def maxSumCircularSubarray(array):
	# Time: O(n) and Space: O(n), extra space for inverting the array
	"""
	Logic:
	If the max sum subarray is present within the start and end of the array, then we find it by using regular
	Kadanes algorithm.
	If the max sum subarray is a combination of the start elements and end elements, then we find it by modified
	Kadanes algorithm. What we do is that, we first invert the sign of every element in the array, and then do the
	Kadanes algorithm, which we give us minimum sum present in the array, now we simply subtract this minimum sum
	from the total sum, i.e total - (-minSum) ==> total + minSum.
	We return whichever was the max from either of the kadanes algorithm.
	"""
	# Edge case. If all the elements in the array are negative, then we simply return the max from them.
	allNegative = True
	for n in array:
		if n >= 0:
			allNegative = False
			break
	if allNegative:
		return max(array)

	# Using regular Kadanes Algorithm
	maxSumOne = kadanesAlgorithm(array)

	# Modified version of the kadanes algorithm.
	# Getting the total sum
	total = sum(array)
	# Inverting the sign of each element
	invertedArray = [n * -1 for n in array]
	# Subtracting the result from the total, i.e total - (-min_sum)
	maxSumTwo = total + kadanesAlgorithm(invertedArray)
	# Returning the max of the above two result
	return max(maxSumOne, maxSumTwo)


def kadanesAlgorithm(array):
	# Simple kadanes algorithm.
	maxSum = float('-inf')
	currSum = float('-inf')
	for n in array:
		currSum = max(currSum + n, n)
		maxSum = max(maxSum, currSum)
	return maxSum


print(maxSumCircularSubarray([-10, -7, 9, -7, 6, 9, -9, -4, -8, -5]))
