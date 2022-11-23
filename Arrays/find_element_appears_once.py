"""
Find the element which appears only once. The rest of the elements appear exactly twice.
Input: [1, 12, 3, 12, 1, 2, 3]
Output: 2

"""


def appearsOnce(array):
	"""
	Logic:
	If rest of all the elements appear twice, then we can directly do XOR operation with every element and return the
	final value of the XOR operation.
	NOTE: If the rest of the elements appear thrice, then the logic is complex.
	"""
	currVal = array[0]
	for i in range(1, len(array)):
		# XOR
		currVal = currVal ^ array[i]
	return currVal


print(appearsOnce([1, 12, 3, 12, 1, 2, 3]))
