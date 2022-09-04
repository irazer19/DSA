"""
Given a 2D array, find the maximum sum subarray of the given size.
Return the maximum sum.

"""


def maximumSumSubmatrix(matrix, size):
    # Time = Space = O(w x h)

    """
    First we compute the sum for all sub-array's of different sizes in the matrix.
    Once you have this sumMatrix, run a for loop starting from the given size, and extract the sum of the
    size x size matrix inside the sumMatrix.
    """
    # Getting the sumMatrix
    sumMatrix = getSumMatrix(matrix)
    maxSum = float('-inf')  # Result

    # We start the row and column such that the subarray is size x size.
    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[0])):
            # This is the current total sum until this position of the sumMatrix.
            currSum = sumMatrix[row][col]
            # We check whether this subarray is touching the top border or left border:
            # If its touching then we dont subtract the top/left border from the current sum.
            # Its not touching that means we have to subtract the top/left border values to extract the sum of the
            # size x size subarray
            # Draw on pen/paper to see it better.
            touchingTop = row - size < 0
            touchingLeft = col - size < 0

            if not touchingTop:
                currSum -= sumMatrix[row - size][col]
            if not touchingLeft:
                currSum -= sumMatrix[row][col - size]
            # If its not touching top and left, then we have subtracted the top diagonal twice, so we add once again.
            if not touchingTop and not touchingLeft:
                currSum += sumMatrix[row - size][col - size]
            # Updating the result
            maxSum = max(maxSum, currSum)

    return maxSum


def getSumMatrix(matrix):
    # We create a matrix such that any index represents the total sum of the top left diagonal subarray
    sumMatrix = [[i for i in row] for row in matrix]
    # 1st row
    for i in range(1, len(matrix[0])):
        sumMatrix[0][i] = sumMatrix[0][i - 1] + sumMatrix[0][i]

    # 1st Col
    for i in range(1, len(matrix)):
        sumMatrix[i][0] = sumMatrix[i - 1][0] + sumMatrix[i][0]
    # Filling rest of the matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            # Remember to subtract the diagonal because we have added it twice (from top and left).
            # Below formula = Top + Left - Diagonal.
            sumMatrix[i][j] += sumMatrix[i - 1][j] + sumMatrix[i][j - 1] - sumMatrix[i - 1][j - 1]

    return sumMatrix


mat = [
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2]
]
print(maximumSumSubmatrix(mat, 2))
