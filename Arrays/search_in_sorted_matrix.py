"""
You're given a two-dimensional array of distinct integers and a target integer. Each row in the matrix is sorted,
and each column is also sorted; the matrix doesn't necessarily have the same height and width.

Write a function that returns an array of the row and column indices of the target integer if it's contained in the
matrix, otherwise [-1 -1]

matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]

Output: [3, 3]

"""


def searchInSortedMatrix(matrix, target):
    # Time: O(n + m) and Space: O(1)
    """
    Logic:
    We start from the top right corner of the matrix, and then move the row, column pointers based on the
    target value and current value of the matrix.
    """
    # Row, column pointers to the top right of the matrix.
    row = 0
    col = len(matrix[0]) - 1
    # While not out of bounds
    while row < len(matrix) and col >= 0:
        # We move down if the target is greater
        if target > matrix[row][col]:
            row += 1
        # We move left if the target is smaller
        elif target < matrix[row][col]:
            col -= 1
        # We return the result if the target == current value.
        else:
            return [row, col]
    # Default result
    return [-1, -1]
