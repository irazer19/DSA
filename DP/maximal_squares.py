"""
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

"""


def maximal_square(arr):
    # Time = Space = O(n x n)
    # Converting all the values to integer.
    arr = [[int(v) for v in row] for row in arr]

    # Using DP, each cell represents: The top left corner of a square, and the value is the size of the square which can
    # be formed.
    store = [[0 for _ in row] for row in arr]
    largest_square = 0  # Stores the result which is the area of the largest square.

    # Since we can only form a square of size 1x1 for the last row/column, so we store its value as its current value.
    # Last Column
    for i in range(len(arr)):
        store[i][len(store[0]) - 1] = arr[i][len(store[0]) - 1]
        # We also update the result in case if its 1, then largest = 1x1
        largest_square = max(largest_square, store[i][len(store[0]) - 1])

    # Last Row
    for i in range(len(arr[0])):
        store[len(store) - 1][i] = arr[len(store) - 1][i]
        largest_square = max(largest_square, store[len(store) - 1][i])

    # Filling th rest of the store matrix. Starting from bottom right.
    for i in range(len(store) - 2, -1, -1):
        for j in range(len(store[0]) - 2, -1, -1):
            # Only if the current value is 1, (because for 0 we cannot form any square with it so we keep as 0).
            if arr[i][j] == 1:
                # We can form a square only if bottom, right and diagonal are all 1's.
                if arr[i + 1][j] == 1 and arr[i][j + 1] == 1 and arr[i + 1][j + 1] == 1:
                    # Now the size of the square which can be formed is 1 + min(bottom, right, diagonal)
                    # We add + 1 because of the current value which increases the size of the square.
                    # We take min(bottom, right, diagonal) because we want a square.
                    store[i][j] = 1 + min(store[i + 1][j], store[i][j + 1], store[i + 1][j + 1])
                else:
                    # Else, the minimum square size is 1x1 as the value is 1.
                    store[i][j] = 1
                largest_square = max(largest_square, store[i][j])

    # We return the area of the square.
    return largest_square ** 2


matrix = [["1", "0", "1", "0", "0"],
          ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"],
          ["1", "0", "0", "1", "0"]]

print(maximal_square(matrix))
