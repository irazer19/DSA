"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or
right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the
bottom-right corner.
Leetcode: Unique Paths
"""


def unique_paths(width, height):
    # Time = Space = O(w x h)
    # Creating the matrix, in every cell we will store the total number of ways to reach that cell.
    store = [[0 for _ in range(width)] for _ in range(height)]
    # We can reach all the cells of the first column and first row only in 1 way
    for i in range(len(store)):
        store[i][0] = 1
    for i in range(len(store[0])):
        store[0][i] = 1

    # Starting from [1, 1], the total ways = top val + left val.
    for i in range(1, len(store)):
        for j in range(1, len(store[0])):
            store[i][j] = store[i - 1][j] + store[i][j - 1]

    return store[-1][-1]


print(unique_paths(3, 7))
