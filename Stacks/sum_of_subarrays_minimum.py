"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr.
Since the answer may be large, return the answer modulo 109 + 7.

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
"""


def sumSubarrayMins(arr) -> int:
	# Time = Space = O(n)
	"""
	Logic:
	So we dont want to generate all the subarrays which will take n^2 time.
	Instead, we will use a formula: for an element i, we can find all the subarrays where this element i will be the
	minimum value by finding all the left greater elements and right greater elements to i and then using:
	(number of left greater elements + 1) * (number of right greater elements + 1)) = Total subarrays where the element i
	will be the minimum.
	We will do the above computation before hand using stack for every element, and then finally compute the
	result

	"""
	# At every index we will store the total number of elements which are greater than the current ith element
	leftLargest = [0 for _ in arr]
	stack = []
	for i in range(len(arr)):
		# While the current element is smaller than the stack's top element, we will keep popping and
		# add the count by : 1 + total elements which were greater than stacks element also
		while stack and arr[i] <= arr[stack[-1]]:
			leftLargest[i] += 1 + leftLargest[stack.pop()]
		# We append to stack the current element
		stack.append(i)

	# Now we move in the reverse direction to find the total greater elements which are to the right of the current
	# element. We use the same logic as above
	stack = []
	rightLargest = [0 for _ in arr]
	for i in range(len(arr) - 1, -1, -1):
		while stack and arr[i] < arr[stack[-1]]:
			rightLargest[i] += 1 + rightLargest[stack.pop()]
		stack.append(i)
	# Finally we compute the result
	result = 0
	# Considering every element as a possible minimum of subarrays
	for i in range(len(arr)):
		# result += current element * (total times this element was minimum in the subarrays)
		# We find the total subarrays = total left greater elements + 1 * total right greater elements + 1
		result += arr[i] * ((leftLargest[i] + 1) * (rightLargest[i] + 1))

	return result % (10 ** 9 + 7)
