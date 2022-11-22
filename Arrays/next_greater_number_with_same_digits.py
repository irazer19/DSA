"""
Given a number n, find the smallest number that has same set of digits as n and is greater than n. If n is the greatest
possible number with its set of digits, then print “not possible”.

Input:  n = "218765"
Output: "251678"

"""


def findNext(n):
	# Time: O(nlogn) and Space: O(n)
	"""
	Logic:
	Step 1: First we find the digit which is smaller than the immediate next digit.
	Step 2: Now we find the digit which is immediate greater than the above found digit.
	Step 3: We swap the above two digits.
	Step 4: Now we sort all the digits which come after the swap of the smaller digit.
	"""
	array = [int(i) for i in n]
	# Starting from the end, find the digit which is smaller than its next digit.
	smallerDigitIdx = None
	i = len(array) - 2
	while i >= 0:
		if n[i] < n[i + 1]:
			smallerDigitIdx = i
			break
		i -= 1
	# Edge Case
	if not smallerDigitIdx:
		return 'Not possible'
	# Find the digit which is immediate greater than the digit found above.
	immediateGreater = float('inf')
	immediateGreaterIdx = None
	for i in range(smallerDigitIdx + 1, len(array)):
		if array[smallerDigitIdx] < array[i] < immediateGreater:
			immediateGreater = array[i]
			immediateGreaterIdx = i

	# Swap
	array[immediateGreaterIdx], array[smallerDigitIdx] = array[smallerDigitIdx], array[immediateGreaterIdx]

	# Sorting the digits which come after smallerDigitIdx
	sortedPart = list(sorted(array[smallerDigitIdx + 1:]))
	resultArray = array[: smallerDigitIdx + 1] + sortedPart
	return ''.join(list(map(str, resultArray)))


print(findNext("4321"))
