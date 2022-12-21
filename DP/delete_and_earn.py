"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following
operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1
and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
"""
from collections import Counter


def deleteAndEarn(nums):
	# Time = Space = O(n)
	"""
	Logic:
	At every index, we will compute the max points we can collect till that index.
	So, first we will sort the array and also get the frequency count of the elements to handle the constraints
	easily.
	Once the array is sorted, if the num[i] - 1 = num[i - 1], then we know that we cannot include the result of
	the previous element, so we add the result of the previous to previous element which is at index i - 2 because
	it will surely not have the value val = num - 1 as we have sorted the array and removed duplicate elements.
	Therefore, we can generalize this by just maintaining two variables, earn1 and earn2 to track the result of the
	previous two elements.
	"""
	if not nums:
		return 0

	# Getting the frequency count of the elements
	count = Counter(nums)
	# Removing duplicate elements and sorting
	nums = sorted(list(set(nums)))
	# stores the result of the previous two elements.
	earn1, earn2 = 0, 0
	# For each element
	for i in range(len(nums)):
		# Getting the total points by selecting the current element
		currPoints = nums[i] * count[nums[i]]
		# Now if the i - 1 element is one less than the current element, then we cannot add its result
		if i > 0 and nums[i] - 1 == nums[i - 1]:
			# cannot include earn2, so we either include the current element and add earn1 result(i-2 element) or
			# dont include the current element and use the previous element fully.
			currPoints = max(earn2, currPoints + earn1)
			# Updating the earn1 and earn2
			earn1 = earn2
			earn2 = currPoints
		else:
			# Here we are sure that we can use the earn2 result(i-1), and also we dont need to use the max function
			# because we know that the previous(earn2) is maximum always.
			# Updating the current points and earn1, and earn2.
			currPoints = currPoints + earn2
			earn1 = earn2
			earn2 = currPoints
	return earn2
