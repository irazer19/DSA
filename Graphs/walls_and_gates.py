"""
You are given m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the
distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should
remain filled with INF

"""


def wallsAndGates(matrix):
    # Time = Space = O(m x n)
    """
    Logic: Get all the gates, then do BFS by popping the items in the same order. While exploring the children nodes,
    if the child is not a Wall and its current minimum distance is greater than the current gate distance + 1,
    then update the child nodes value and add this child to the queue.

    """

    # Getting all the gates
    gates = getAllGates(matrix)

    # Until we can explore the nodes with minimum distance
    while gates:
        # Popping the nodes in the same order
        row, col = gates.pop(0)
        # top
        # If the child is not a WALL and the distance from the current gate + 1 < current rooms existing distance,
        # then update it.
        if row > 0 and matrix[row - 1][col] != -1 and matrix[row - 1][col] > matrix[row][col] + 1:
            matrix[row - 1][col] = matrix[row][col] + 1
            gates.append([row - 1, col])
        # left
        if col > 0 and matrix[row][col - 1] != -1 and matrix[row][col - 1] > matrix[row][col] + 1:
            matrix[row][col - 1] = matrix[row][col] + 1
            gates.append([row, col - 1])
        # bottom
        if row < len(matrix) - 1 and matrix[row + 1][col] != -1 and matrix[row + 1][col] > matrix[row][col] + 1:
            matrix[row + 1][col] = matrix[row][col] + 1
            gates.append([row + 1, col])
        # right
        if col < len(matrix[0]) - 1 and matrix[row][col + 1] != -1 and matrix[row][col + 1] > matrix[row][col] + 1:
            matrix[row][col + 1] = matrix[row][col] + 1
            gates.append([row, col + 1])

    return matrix


def getAllGates(matrix):
    # Getting all the gates, that is the nodes with value = 0.
    gates = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                gates.append([i, j])
    return gates


matrix_input = [[float('inf'), -1, 0, float('inf')],
                [float('inf'), float('inf'), float('inf'), -1],
                [float('inf'), -1, float('inf'), -1],
                [0, -1, float('inf'), float('inf')]]
print(wallsAndGates(matrix_input))
