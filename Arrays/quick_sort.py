"""
Quick Sort
"""


def quickSort(array):
	# Best = Average = O(nlogn), Worst = O(n^2)
	# Space: O(logn)
	"""
	Logic:
	We will take the pivot as the first element, and then use left pointer to place all elements smaller/equal than
	the pivot and the right pointer to place all elements greater than or equal to the pivot.
	Once the left > right, the right pointer is swapped with the pivot, and then we again recursively call the
	function by passing the lower half and the upper half of the array.
	"""
	sortHelper(array, 0, len(array) - 1)
	return array


def sortHelper(array, start, end):
	# If array size is invalid.
	if start >= end:
		return
	# Pointers
	pivot = start
	left = start + 1
	right = end
	while left <= right:
		# If the left element is greater and the right element is smaller than the pivot then we swap them.
		if array[left] > array[pivot] and array[right] < array[pivot]:
			array[left], array[right] = array[right], array[left]
		# If the left element is already in the correct position then we move to next
		if array[left] <= array[pivot]:
			left += 1
		# If the right element is already in the correct position then we move to next.
		if array[right] >= array[pivot]:
			right -= 1
	# Swapping the the pivot and the right index element. This swap will place the pivot value in the its correct
	# position which is the right index.
	array[right], array[pivot] = array[pivot], array[right]
	# Calling the same function with the lower and upper half of the array divided by the right index.
	sortHelper(array, start, right - 1)
	sortHelper(array, right + 1, end)
