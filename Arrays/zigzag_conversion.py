"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""


def convert(s: str, numRows: int) -> str:
	# Time: O(n) and Space: O(n)
	"""
	Logic:
	We will visit the elements row wise, so for the first and the last row, we have the increment of the pointer
	fixed, which is, increment = (number of rows - 1) * 2
	So as we traverse through the elements, we will jump by "increment" amount.

	Now for the rows between first and the last row, there are more elements which needs to be captured, and we will
	do it by checking whether this index is valid or not, which is = (current index + increment) - 2 * current row

	"""
	# Base case, if we just have 1 row, then return the input string.
	if numRows == 1:
		return s

	result = ""
	# For each row.
	for r in range(numRows):
		# This is the increment jump which we take.
		increment = (numRows - 1) * 2
		# Going through the string from rth index
		for i in range(r, len(s), increment):
			# Adding the letter to the result
			result += s[i]
			# Now if this row lies between first and the last row, then we check one more possible element using
			# this formula.
			if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
				# Adding this element too
				result += s[i + increment - 2 * r]
	return result
