"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above
sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is
less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

leetcode: https://leetcode.com/problems/pacific-atlantic-water-flow/description/

Input: heights = [[1,2,2,3,5],
                  [3,2,3,4,4],
                  [2,4,5,3,1],
                  [6,7,1,4,5],
                  [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
"""


def pacific_atlantic(heights):
    # Time = Space = O(n)
    """
    We will create two matrices, one for storing the boolean of whether its possible to read pacific ocean from a cell,
    and same thing for atlantic.
    We will do DFS from each cell: For Pacific we will start dfs from top left, and for atlantic from bottom right.
    After filling both the arrays, we will loop over every cell, and whichever cell has both True for atlantic and pacific.
    we will add it in the result.
    """

    # Pacific array
    pacific = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
    # Atlantic array
    atlantic = [[False for _ in range(len(heights[0]))] for _ in range(len(heights))]
    result = []

    # Visited set
    visited = set()
    # Starting from top left
    for row in range(len(pacific)):
        for col in range(len(pacific[0])):
            # We want to do dfs starting from only those cells which are connected to the Pacific ocean.
            if row == 0 or col == 0:
                dfs(heights, pacific, row, col, visited, 0)

    visited = set()
    # Starting from bottom right
    for row in range(len(atlantic) - 1, -1, -1):
        for col in range(len(atlantic[0]) - 1, -1, -1):
            # We will do dfs starting from those cells which are connected to the atlantic ocean.
            if row == len(atlantic) - 1 or col == len(atlantic[0]) - 1:
                dfs(heights, atlantic, row, col, visited, 0)

    for i in range(len(heights)):
        for j in range(len(heights[0])):
            # If a cell can reach both pacific and atlantic, then we add in the result
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])

    return result


def dfs(heights, arr, row, col, visited, prev):
    # Common dfs function
    # If the current row and col is in the range
    if 0 <= row < len(arr) and 0 <= col < len(arr[0]):
        # If this cell is not visited and its previous cell is smaller or equal to it, then we know that the water
        # can fall from this current cell to the previous cell.
        if (row, col) not in visited and heights[row][col] >= prev:
            # Mark the current cell as True, means that the water can flow
            arr[row][col] = True
            # Mark as visited
            visited.add((row, col))
            # Explore Top, bottom, left and right
            dfs(heights, arr, row - 1, col, visited, heights[row][col])
            dfs(heights, arr, row + 1, col, visited, heights[row][col])
            dfs(heights, arr, row, col - 1, visited, heights[row][col])
            dfs(heights, arr, row, col + 1, visited, heights[row][col])
