"""
Given an array of integers which is initially increasing and then decreasing, find the maximum value in the array.

Input: arr[] = {8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1}
Output: 500

"""


def maxInIncreasingDecreasing(array):
	# Time: O(logn) and Space: O(1)
	"""
	Logic:
	We use binary search. We compare the middle element with the previous and next elements, whichever side is
	greater than the current middle element, we move towards that side.
	If neither previous nor next element is greater, then that means we have found the max element.
	"""
	left = 0
	right = len(array) - 1

	while left <= right:
		mid = (left + right) // 2
		# If the previous element is greater, we move that way.
		if mid > 0 and array[mid] < array[mid - 1]:
			right = mid - 1
		# If the next element is greater, we move that way
		elif mid < len(array) - 1 and array[mid] < array[mid + 1]:
			left = mid + 1
		else:
			# Else we hit the maxima
			return array[mid]
	return -1


print(maxInIncreasingDecreasing([8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]))
