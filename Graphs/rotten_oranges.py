"""
Given a matrix of size m x n, find the minimum number of passes required to convert all the negative values to positive
value. A negative number can be converted to a positive number only if there exists a positive value either to
the top, left, bottom, or right side of the negative number.
0 is neither positive nor negative, so it cannot convert negative values to positive.

Return the minimum number of passes.
"""


def minimumPassesOfMatrix(matrix):
    # Time = Space = O(m x n)

    # Logic: First we collect all the positive values in the matrix, and store inside a queue.
    # Now we pop the positive values from the queue and convert the negative to positive if any around its adjacent.
    # As we convert negative values to positive, we store that newly converted value in the queue.
    # To mark a pass, we loop through all the length of the queue and once out we increase the passes+=1.
    # Finally, we check whether the matrix still contains negative values, if yes then -1 else return passes-1

    # Getting all the positive values
    pos = getAllPositives(matrix)
    passes = 0

    # Until there are positive values in the queue
    while pos:
        # We only loop till the length of the queue so that we can mark the number of passes.
        for i in range(len(pos)):
            row, col = pos.pop(0)
            # We exclude all the zero values
            # Checking top
            if row > 0 and matrix[row - 1][col] < 0:
                matrix[row - 1][col] *= -1  # Converting to positive
                pos.append([row - 1, col])
            # Checking left
            if col > 0 and matrix[row][col - 1] < 0:
                matrix[row][col - 1] *= -1
                pos.append([row, col - 1])
            #  Checking bottom
            if row < len(matrix) - 1 and matrix[row + 1][col] < 0:
                matrix[row + 1][col] *= -1
                pos.append([row + 1, col])
            # Checking right
            if col < len(matrix[0]) - 1 and matrix[row][col + 1] < 0:
                matrix[row][col + 1] *= -1
                pos.append([row, col + 1])

        passes += 1  # Increasing the pass

    # Check whether the matrix still contains negative.
    return -1 if containsNegative(matrix) else passes - 1


def getAllPositives(matrix):
    # Storing all the positive values
    pos = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                pos.append([i, j])
    return pos


def containsNegative(matrix):
    # Checking negative values
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                return True
    return False


print(minimumPassesOfMatrix([
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1],
]))
