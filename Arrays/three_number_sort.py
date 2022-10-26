"""
Sort the given array in the given order of the numbers.

array = [1, 0, 0, -1, -1, 0, 1, 1]
order = [0, 1, -1]
expected = [0, 0, 0, 1, 1, 1, -1, -1]

"""


def threeNumberSort(array, order):
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	We will use three pointers for each of the three numbers in the order.
	We will move the second pointer by comparing its value with the orders, and swap if needed for sorting in the
	given order.
	"""
	# Initializing three pointers
	first = 0
	second = 0
	third = len(array) - 1
	# Since we move the second pointer, we will terminate if the second pointer > third pointer.
	while second <= third:
		# If the second pointer == first order value.
		if array[second] == order[0]:
			# We will swap
			swap(first, second, array)
			# We will increase first pointer because it already has a correct value.
			# We will increment second pointer because it should never be less than the first pointer.
			first += 1
			second += 1
		# If the second pointer == second order value
		# We will move on because its already in a correct position
		elif array[second] == order[1]:
			second += 1
		# Else if the second pointer == third order value
		elif array[second] == order[2]:
			# We will swap
			swap(second, third, array)
			# We will decrease the third pointer because its already has a correct value.
			third -= 1
	return array


def swap(i, j, array):
	array[i], array[j] = array[j], array[i]
