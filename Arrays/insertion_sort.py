"""
Insertion Sort.

"""


def insertionSort(array):
	# Time: O(n^2) and Space: O(1)
	# We start from index 1 because the first element is already sorted.
	for i in range(1, len(array)):
		# We will compare the current and previous elements
		prev = i - 1
		curr = i
		# Until the previous element is greater than the current, we will swap
		while prev >= 0 and array[prev] > array[curr]:
			array[prev], array[curr] = array[curr], array[prev]
			prev -= 1
			curr -= 1

	return array

