"""
Fill the board with valid numbers where the board is a Sudoku board.
Numbers can be between 1 and 9, and 0 represents empty cell.

input = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

Output =
    [7, 8, 5, 4, 3, 9, 1, 2, 6]
    [6, 1, 2, 8, 7, 5, 3, 4, 9]
    [4, 9, 3, 6, 2, 1, 5, 7, 8]
    [8, 5, 7, 9, 4, 3, 2, 6, 1]
    [2, 6, 1, 7, 5, 8, 9, 3, 4]
    [9, 3, 4, 1, 6, 2, 7, 8, 5]
    [5, 7, 8, 3, 9, 4, 6, 1, 2]
    [1, 2, 6, 5, 8, 7, 4, 9, 3]
    [3, 4, 9, 2, 1, 6, 8, 5, 7]

https://leetcode.com/problems/valid-sudoku/description/
"""


def solveSudoku(board):
    # Time = Space = O(1), because the board size 9x9 is fixed.
    """
    Logic:
    We will move through the board, and if we find the current cell > 0, then we just move to the next cell.
    And if we find the current cell == 0 (empty), then we try to fill it with number between 1 and 9 one by one,
    and move to the next cell. For each number, we check whether the number can be placed at the current cell
    according to the rules of sudoku. If yes, then we make the function call and move to the next cell else try
    with the next number.
    If none of the numbers work then we come out of the for loop and restore the original state of the cell which is 0.
    If we have reached the end of the board, then we return True.

    Sudoku rule:
    The number should not already exist in the same row, same column, and same grid of 3x3.

    """

    # We start the function call, populate the board cells and return the board.
    solve(board, 0, 0)

    return board


def solve(board, row, col):
    # If the next cell does not exist, then we move to the next row and reset the column = 0.
    if col == len(board[0]):
        row += 1
        col = 0
        # If the row also does not exist, then we have reached the end of the board and return True.
        if row == len(board):
            return True

    # If the current cell already has a number > 0, it means that this is not an empty cell.
    # So we move to the next cell.
    if board[row][col] > 0:
        if solve(board, row, col + 1):
            return True
    else:
        # Else, we try to fill the current cell with values from 1 to 9.
        for val in range(1, 10):
            # Check whether this number's placement breaks any sudoku rules.
            if isValidPosition(board, row, col, val):
                # If the number can be placed, then we store the number in the current cell and move to the next cell.
                board[row][col] = val
                # If the return is True, then we know we have filled all the cells correctly, therefore we return True.
                if solve(board, row, col + 1):
                    return True
        # Else, if none of the numbers work, then we restore the current cell value to 0.
        board[row][col] = 0
    # Return False because we could not find the correct number to fill the cell.
    return False


def isValidPosition(board, row, col, val):
    # The number should not already exist in the row.
    for i in range(len(board[0])):
        if board[row][i] == val:
            return False

    # The number should not already exist in the column.
    for i in range(len(board)):
        if board[i][col] == val:
            return False

    # The number should not already exist in the 3x3 grid.
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == val:
                return False
    return True


input = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

print(solveSudoku(input))
