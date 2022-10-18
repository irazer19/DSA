"""
Traverse the matrix in spiral order and return the result.
matrix = [[1, 2, 3, 4],
          [12, 13, 14, 5],
          [11, 16, 15, 6],
          [10, 9, 8, 7]]

Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""


def spiralTraverse(array):
    # Time = Space = O(n)
    """
    Logic:
    We will traverse the outer layer first then move to the inner layer.
    For a layer: We will visit the first row, then last column, then last row, and then first column.
    """
    # Initializing the start, end for row and column.
    startRow = 0
    endRow = len(array) - 1
    startCol = 0
    endCol = len(array[0]) - 1
    # Storing the result.
    result = []

    # While the start is less or equal to the end for row/col
    while startRow <= endRow and startCol <= endCol:
        # first row
        for i in range(startCol, endCol + 1):
            result.append(array[startRow][i])

        # last col
        for i in range(startRow + 1, endRow + 1):
            result.append(array[i][endCol])

        # last row
        for i in range(endCol - 1, startCol - 1, -1):
            if startRow == endRow:
                break
            result.append(array[endRow][i])

        # first col
        for i in range(endRow - 1, startRow, -1):
            if startCol == endCol:
                break
            result.append(array[i][startCol])

        # Increasing the starting index and decreasing the ending index.
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result
