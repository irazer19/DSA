"""
Given n, place the queens in the chess board of n x n such that no two queens are in the same row, column, and
diagonals.
Return the total number of placements possible in the board.

Input: n = 4
Output: 2

https://leetcode.com/problems/n-queens/description/
"""


def nonAttackingQueens(n):
    # Time: O(n!) and Space: O(n)
    """
    Logic:
    We start by creating a matrix n x n for placing the queens.
    Using recursive functions, we try placing the queen in every row for the given column.
    If a queen is placed successfully, then we move to the next column.
    If the next column is out of bounds, then we know we have placed all the queens successfully, and so add +1
    to the result and return.

    According to the rules, a queen can be placed only if there are no other queens in the same row, column,
    top left diagonal, and bottom left diagonal.

    """

    # Creating the matrix n x n.
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    result = Result(0)
    # Start of the recursive function.
    placeQueens(matrix, 0, result)

    return result.total


def placeQueens(matrix, col, result):
    # If the column is out of bounds, then we add +1 to the result.
    if col == len(matrix[0]):
        result.total += 1
        return

    # We try placing the queens in every row of the current column.
    for row in range(0, len(matrix)):
        # Check whether the queen can be placed at this position.
        if isValid(matrix, row, col):
            # Placing the queen
            matrix[row][col] = 1
            # Move to the next column
            placeQueens(matrix, col + 1, result)
            # Undo queen placement for the next configuration.
            matrix[row][col] = 0


def isValid(matrix, row, col):
    # Checking the row
    if 1 in matrix[row]:
        return False

    # Checking the column
    for i in range(len(matrix)):
        if matrix[i][col] == 1:
            return False

    # Checking the Top Left Diagonal
    start_row = row
    start_col = col
    while start_row >= 0 and start_col >= 0:
        if matrix[start_row][start_col] == 1:
            return False
        start_row -= 1
        start_col -= 1

    # Checking the Bottom Left Diagonal
    start_row = row
    start_col = col
    while start_row < len(matrix) and start_col >= 0:
        if matrix[start_row][start_col] == 1:
            return False
        start_row += 1
        start_col -= 1

    # True only if no other queen is present in the same row, col, and diagonals
    return True


# Class to store the result
class Result:
    def __init__(self, total):
        self.total = total
