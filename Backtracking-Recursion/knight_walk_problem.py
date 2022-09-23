"""
Given a square chessboard of N x N size, the position of the Knight and the position of a target.
We need to find out the minimum steps a Knight will take to reach the target position.

Input: n=30, knight=[1, 1], target=[30,30]
Output: 20
"""


def knightWalk(n, knight, target):
    # Time = Space = O(n x n)
    """
    Logic:
    Create a matrix with 0's, 0 means that the cell is unvisited, and we will store in it the minimum distance from
    knight's position.
    Now add the position of the knight in the queue, and
    do BFS, a knight can visit 8 different positions, so for each position, check whether it's valid and unvisited,
    If yes, then update the new cell's distance to 1 + current cell's distance (since we have moved 1 step forward) and
    add this new cell to the queue.

    This way we will visit all the cells, and update its distance from the knight as we do BFS, which will also
    include the target cell.

    Finally, we return the value in the target cell.

    """

    # Initializing the board with 0's
    board = [[0 for _ in range(n)] for _ in range(n)]
    # Eight different positions, adding each value to the row, col will get us the new position on the board.
    eightPos = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]

    # Adding the knights positions in the queue.
    q = [[knight[0], knight[1]]]

    # BFS
    while q:
        # Getting the current node/cell
        row, col = q.pop(0)
        # Moving to eight different positions from the current cell.
        for toRow, toCol in eightPos:
            # Computing the new row and new column values.
            newRow = row + toRow
            newCol = col + toCol
            # Checking whether the new position is within the bounds and is unvisited.
            if isValid(n, newRow, newCol) and board[newRow][newCol] == 0:
                # Updating the new cell with the distance from the knight, which is 1 + distance from the current cell.
                board[newRow][newCol] = 1 + board[row][col]
                # Adding the new position to the queue.
                q.append([newRow, newCol])

    # Return the distance of the target position.
    return board[target[0]][target[1]]


def isValid(n, newRow, newCol):
    # Checks out of bounds condition
    return 0 <= newRow < n and 0 <= newCol < n


print(knightWalk(30, [1, 1], [29, 29]))
