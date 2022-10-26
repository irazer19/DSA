"""
Write a function that takes in an array of integers and returns the number of inversions in the array. An inversion
occurs if for any valid indices i and j, i < j and array[i] > array[j].

input = [2, 3, 3, 1, 9, 5, 6]
expected = 5
"""


def countInversions(array):
	# Time: O(nlogn) and Space: O(n)
	"""
	Logic:
	The number of inversions in the array is a measure of how unsorted the array is.
	So we will use merge sort to count the number of inversions which can be done in O(nlogn) time.
	At the point where we merge the arrays, if the right element is greater than the left element of the array,
	then we know that since both the arrays are sorted, the right element must also be greater than all the
	elements after the left element onwards, and this is where we calculate the number of inversions.
	"""
	if len(array) <= 1:
		return 0
	return divide(array, 0, len(array) - 1)


def divide(array, start, end):
	# Base case for the recursive division.
	# If there is only one element in the array, we will return 0 inversions
	if start == end:
		return 0
	# Getting the mid
	mid = (start + end) // 2
	# Getting inversions from the left half of the array
	leftInversions = divide(array, start, mid)
	# Getting inversions from the right half of the array
	rightInversions = divide(array, mid + 1, end)
	# Getting the inversions from merging the left half and right half
	mergedInversions = merge(array, start, mid, end)
	# Returning the total inversions
	return leftInversions + rightInversions + mergedInversions


def merge(array, start, mid, end):
	# First half start index
	i = start
	# Second half start index
	j = mid + 1
	# Start index of the position where we will update the value in the array during sort.
	k = start
	# Auxiliary array, used for comparing the left and right half values.
	aux = array[:]
	# Counts the inversions from merging
	inversions = 0
	# Until both the arrays are valid
	while i <= mid and j <= end:
		# If left val is smaller than right val
		if aux[i] <= aux[j]:
			# Update the original array's kth position with that value.
			array[k] = aux[i]
			# Move the left arrays pointer
			i += 1
		else:
			# If the right element > left element, then the right element is also greater than all the elements
			# which come after that left element, which is equal to the number of inversions.
			# Since mid is the end index for the left half of the array, mid - i + 1 = total number of elements
			# after ith element including the ith element.
			inversions += mid - i + 1
			# Else do the same for the right half of the array.
			array[k] = aux[j]
			j += 1
		# We will always move with the next kth position.
		k += 1
	# If left half still has some elements, we will update the array.
	while i <= mid:
		array[k] = aux[i]
		i += 1
		k += 1
	# If right half still has some elements, we will update the array.
	while j <= end:
		array[k] = aux[j]
		j += 1
		k += 1
	# Returning the inversions
	return inversions
