"""
Also called "NEXT PERMUTATION".
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1],
[3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical
order, then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order
(i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger
rearrangement.
Given an array of integers nums, find the next permutation of nums

Input: nums = [1,2,3]
Output: [1,3,2]

"""


def findNext(nums):
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	Step 1: First we find the digit which is smaller than the immediate next digit.
	Step 2: Now we find the largest index digit which is immediate greater than the above found digit.
	Step 3: We swap the above two digits.
	Step 4: Now we reverse from everything from the swapped idx onwards.
	"""

	# Finding the digit whose immediate next digit is greater.
	leftIdxToSwap = -1
	i = len(nums) - 1
	while i > 0:
		if nums[i - 1] < nums[i]:
			leftIdxToSwap = i - 1
			break
		i -= 1

	# If there was no such index, then we simply reverse the nums, ex: [3, 2, 1], the next permutation is [1, 2, 3]
	if leftIdxToSwap == -1:
		reverse(nums, 0, len(nums) - 1)
	else:
		# We want to find the digit which is greater than leftIdxToSwap, and is smallest among all the compared
		# elements, we want to maximize this index so that the we do the swap with the smallest rightmost element.
		# By default, the current next element is greater.
		rightIdxToSwap = leftIdxToSwap + 1
		# We start comparing all the next values
		for i in range(rightIdxToSwap + 1, len(nums)):
			# If the current value is greater than the leftIdxToSwap element, and its greater than or equal to
			# the current rightIdxToSwap element, we update the rightIdxToSwap.
			if nums[i] > nums[leftIdxToSwap] and nums[rightIdxToSwap] >= nums[i]:
				rightIdxToSwap = i
		# Once we have the correct rightIdxToSwap, we do the swap.
		nums[rightIdxToSwap], nums[leftIdxToSwap] = nums[leftIdxToSwap], nums[rightIdxToSwap]
		# Finally, we reverse the last elements starting from the next index of leftIdxToSwap.
		reverse(nums, leftIdxToSwap + 1, len(nums) - 1)


def reverse(nums, start, end):
	while start < end:
		nums[start], nums[end] = nums[end], nums[start]
		start += 1
		end -= 1


print(findNext([1, 2, 3]))
