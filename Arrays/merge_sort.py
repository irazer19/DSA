"""
Merge sort.

"""


def mergeSort(array):
	# Time: O(nlogn) and Space: O(n)
	"""
	Logic:
	We will divide the array using start and end pointers until there is only one element in the array.
	For merging, we will compare the two arrays using pointers, first array [start: mid] and second array [mid+1: end],
	We will use the auxiliary array which is the copy of the current array to compare the elements of the two arrays.
	And the store the sorted elements in the original array.
	"""
	# Edge base
	if len(array) <= 1:
		return array
	divide(array, 0, len(array) - 1)
	return array


def divide(array, start, end):
	# Base case for the recursive division.
	# If there is only one element in the array, we will return.
	if start == end:
		return
	# Getting the mid
	mid = (start + end) // 2
	# Left half of the array
	divide(array, start, mid)
	# Right half of the array
	divide(array, mid + 1, end)
	# Merging the left half and right half
	merge(array, start, mid, end)


def merge(array, start, mid, end):
	# First half start index
	i = start
	# Second half start index
	j = mid + 1
	# Start index of the position where we will update the value in the array during sort.
	k = start
	# Auxiliary array, used for comparing the left and right half values.
	aux = array[:]
	# Until both the arrays are valid
	while i <= mid and j <= end:
		# If left val is smaller than right val
		if aux[i] <= aux[j]:
			# Update the original array's kth position with that value.
			array[k] = aux[i]
			# Move the left arrays pointer
			i += 1
		else:
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
