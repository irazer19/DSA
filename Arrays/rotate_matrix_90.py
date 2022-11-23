"""
Given a square matrix, turn it by 90 degrees in an anti-clockwise direction without using any extra space
Input:
Matrix:    1  2  3
           4  5  6
           7  8  9

Output:  3  6  9
         2  5  8
         1  4  7
"""


def rotate(matrix):
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	To rotate a squared matrix by 90, there are two major steps:
	1. Reverse all rows(anti-clockwise) / columns(clockwise)
	2. Transpose of the matrix.
	"""
	# For this question, we are rotating the matrix in anti-clockwise direction, so we reverse all the rows
	reverseRows(matrix)
	# Then we transpose the matrix.
	transpose(matrix)
	return matrix


def reverseRows(matrix):
	# For each row.
	for rowIdx in range(len(matrix)):
		# We swap the first element with the last element
		startCol, endCol = 0, len(matrix[0]) - 1
		while startCol < endCol:
			matrix[rowIdx][startCol], matrix[rowIdx][endCol] = matrix[rowIdx][endCol], matrix[rowIdx][startCol]
			startCol += 1
			endCol -= 1


def transpose(matrix):
	# At each row, say (0, 0), we start swapping [0, 1] with [1, 0], then [0, 2] with [2, 0] and so on...
	# until the end of the index, and since its a
	# squared matrix, we can just maintain one index pointer.

	# For each row, [0, 0], then [1, 1], [2, 2]....
	for i in range(len(matrix)):
		# Starting from the i, we move till the end of the matrix index and swap with its symmetry.
		for j in range(i, len(matrix)):
			# Swap symmetric elements of the matrix
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
print(rotate(mat))
