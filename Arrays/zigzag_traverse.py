"""
Traverse the matrix in a zigzag order.
test = [[1, 3, 4, 10],
        [2, 5, 9, 11],
        [6, 8, 12, 15],
        [7, 13, 14, 16]]

Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

"""


def zigzagTraverse(array):
    # Time = Space = O(n)
    """
    Logic:
    We create a flag goingDown to track the direction of the traversal.
    If we are going down then we have will adjust the row,col accordingly and handle the base case.
    Similarly, we will do it while going up.
    As we traverse, we will add the current element to the result.
    """
    # Flag to tack the direction of the traversal
    goingDown = True
    # Stores the result
    result = []
    row = 0
    col = 0
    # While the row and col are the within the bound.
    while not isOutOfBound(row, col, array):
        # Adding the current element to the result
        result.append(array[row][col])
        # If going down
        if goingDown:
            # If element is at the first column or the last row then we know we have to go up now.
            if row == len(array) - 1 or col == 0:
                # Going up now.
                goingDown = False
                # If its the last row, then we will move to the next col
                if row == len(array) - 1:
                    col += 1
                else:
                    # Else if we are the first col, then we move down.
                    row += 1
            else:
                # Else, we can simply keep moving down.
                row += 1
                col -= 1
        else:
            # Else if we are moving up.
            # If we are at the first row or the last column
            if row == 0 or col == len(array[0]) - 1:
                # We will now move down.
                goingDown = True
                # If we are the last column, we will move to the next row.
                if col == len(array[0]) - 1:
                    row += 1
                else:
                    # If we are the first row, then we will move to the next column
                    col += 1
            else:
                # Else we will keep moving up
                row -= 1
                col += 1
    return result


def isOutOfBound(row, col, array):
    # To check whether the current element is out of bounds.
    if not 0 <= row < len(array) or not 0 <= col < len(array[0]):
        return True
    return False
