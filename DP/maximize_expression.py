"""
Given an array of integers, maximize the expression: a - b + c - d
Return the max value of the expression.

"""


def maximizeExpression(array):
    # Time = Space = O(n)
    # If there are less than 4 elements, return 0
    if len(array) < 4:
        return 0

    # Using DP, we will approach in steps, first we will maximize a, then a-b, then a-b+c, then a-b+c-d
    maxOfA = [array[0]]  # Stores all the max values of a for all the index
    maxOfAMinusB = [float('-inf')]  # Store the max values of a-b for all the index.
    maxOfAMinusBPlusC = [float('-inf')] * 2  # Store the max values of a-b+c for all the index.
    maxOfAMinusBPlusCMinusD = [float('-inf')] * 3  # Store the max values of a-b+c-d for all the index.

    # First finding the max values of a
    for i in range(1, len(array)):
        curr_max = max(maxOfA[i - 1], array[i])
        maxOfA.append(curr_max)

    # Finding the max values of a-b
    for i in range(1, len(array)):
        curr_max = max(maxOfAMinusB[i - 1], maxOfA[i - 1] - array[i])
        maxOfAMinusB.append(curr_max)

    # Finding the max values of a-b+c
    for i in range(2, len(array)):
        curr_max = max(maxOfAMinusBPlusC[i - 1], maxOfAMinusB[i - 1] + array[i])
        maxOfAMinusBPlusC.append(curr_max)

    # Finding the max values of a-b+c-d
    for i in range(3, len(array)):
        # Explanation: Either the previous value is already max OR we use the current index value as "d"
        # and add it to the max value of a-b+c till the previous index (i-1)
        curr_max = max(maxOfAMinusBPlusCMinusD[i - 1], maxOfAMinusBPlusC[i - 1] - array[i])
        maxOfAMinusBPlusCMinusD.append(curr_max)

    # Result
    return max(maxOfAMinusBPlusCMinusD)


print(maximizeExpression([3, 6, 1, -3, 2, 7]))
