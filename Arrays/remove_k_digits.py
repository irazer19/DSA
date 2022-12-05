"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer
after removing k digits from num.

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
"""


def removeKdigits(num: str, k: int):
	# Time: O(n) and Space: O(n)
	"""
	Logic:
	To make the number smallest be removing k digits, we first have to analyze something,
	For [1, 2, 3, 4, 5], since the array is increasing, we should start removing from the end.
	For [5, 4, 3, 2, 1], here the array is decreasing, so we should start removing from the beginning.
	So, whenever we have decrease like [4, 3], then we remove the 4 to reduce the number.

	We will use a stack, and compare the top value of the stack with the current value, if its decreasing, then we will
	pop the stack.
	"""
	# Stack to store the result as we move
	stack = []
	# For each digit.
	for n in num:
		# If k is still > 0, and stack is not empty, and the top stack value is greater than the current element.
		while k > 0 and stack and int(stack[-1]) > int(n):
			# We pop from the stack
			stack.pop()
			# Decrease the k
			k -= 1
		# Adding the current element to the stack.
		stack.append(n)
	# Since we are decreasing k in the above, if we were not able to make k=0, then we should subtract k number of
	# elements from the final result.
	result = stack[:len(stack) - k]
	# Finally, if result exists, then we will first convert to integer so that leading zero is removed and then
	# again convert to string.
	return str(int(''.join(result))) if result else "0"
