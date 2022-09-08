"""
Given a matrix of 0's and 1's, an island is a group of 1's horizontally or vertically which is not touching the
border of the matrix.
Return the matrix where all the islands(1's) are converted to 0's.

"""


def removeIslands(matrix):
    # Time = Space = O(n x n)
    # Tracks which node is already visited.
    visited = [[False for _ in row] for row in matrix]

    # Logic: Since an island cannot touch the border of the matrix, we will first collect all the 1's which are
    # on the border of the matrix, and explore all the nearby 1's and convert them to 2.
    # Once all the 1's become 2, then the remaining 1's will be part of an island which we cannot directly convert
    # to 0, and then again convert the 2's to 1 to restore the original form of the matrix. Return this matrix.

    # Getting all the border Ones
    borderOnes = getBorderOnes(matrix)
    # Exploring all the children nodes of the border 1's and converting to 2.
    explore(matrix, visited, borderOnes)

    # Now, converting 1's(islands) to 0 and 2's to 1.
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                matrix[i][j] = 0
            elif matrix[i][j] == 2:
                matrix[i][j] = 1
    return matrix


def explore(matrix, visited, q):
    # Exploring children using BFS
    while q:
        row, col = q.pop(0)
        # Only unvisited nodes.
        if visited[row][col]:
            continue
        visited[row][col] = True
        matrix[row][col] = 2  # Converting to 2
        # top
        if row > 0 and matrix[row - 1][col] == 1 and not visited[row - 1][col]:
            q.append([row - 1, col])

        # left
        if col > 0 and matrix[row][col - 1] == 1 and not visited[row][col - 1]:
            q.append([row, col - 1])

        # bottom
        if row < len(matrix) - 1 and matrix[row + 1][col] == 1 and not visited[row + 1][col]:
            q.append([row + 1, col])

        # right
        if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1 and not visited[row][col + 1]:
            q.append([row, col + 1])


def getBorderOnes(matrix):
    # Getting all the nodes which has a value = 1 and is at the border of the matrix.
    q = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and (i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[0]) - 1):
                q.append([i, j])

    return q


print(removeIslands([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]))
