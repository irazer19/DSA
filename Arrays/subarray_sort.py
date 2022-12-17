"""
Write a function that takes in an array of at least two integers and that returns an array of the starting and
ending indices of the smallest subarray in the input array that needs to be sorted in place in order for the entire
input array to be sorted.

array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
Output: [3, 9]

"""


def subarraySort(array):
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	First we will find the smallest and the largest value in the array which are at incorrect positions.
	Then we will run two separate for loops to find the correct index of the smallest and the largest number
	respectively.

	"""
	# Initializing the smallest and the largest values
	smallestVal = float('inf')
	largestVal = float('-inf')
	# For each element
	for i in range(len(array)):
		# To store the index of the current element if its at incorrect position.
		incorrectIdx = None
		# If its the first element, we will compare it with the next element.
		if i == 0:
			if array[i] > array[i + 1]:
				incorrectIdx = i
		elif i == len(array) - 1:
			# If its the last element, we will compare it with the previous element.
			if array[i] < array[i - 1]:
				incorrectIdx = i
		else:
			# Else, we will compare the current element with its next and previous element.
			if array[i] < array[i - 1] or array[i] > array[i + 1]:
				incorrectIdx = i
		# If incorrectIdx is present, then we will update the smallest and the largest value
		if incorrectIdx is not None:
			smallestVal = min(smallestVal, array[i])
			largestVal = max(largestVal, array[i])
	# Initializing the default result
	result = [-1, -1]
	# Finding the correct index for the smallest value
	# The first element from left which is greater than the smallest value is the correct index.
	for i in range(len(array)):
		if array[i] > smallestVal:
			result[0] = i
			break
	# Finding the correct index for the largest value
	# The first element from right which is smaller than the largest value is the correct index
	for i in range(len(array) - 1, -1, -1):
		if array[i] < largestVal:
			result[1] = i
			break

	return result
