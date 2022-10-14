"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return
its area.

"""


def maximalRectangle(matrix):
    # Time: O(m x n) and Space: O(n)
    """
    Logic:
    This problem is an extended version of the largest rectangle problem.
    From the given matrix, we treat every row as the base of the building where the height is the sum of all the 1's
    above it.
    We pass every row to the largestRectangleUnderSkyline to get the largest rectangle area.
    """
    # Getting the heights of the building for every row.
    matrix = matrixToHeights(matrix)
    # storing the result
    largestRect = 0
    # Passing every row to the largestRectangleUnderSkyline to get the largest rectangle.
    for row in matrix:
        largestRect = max(largestRect, largestRectangleUnderSkyline(row))

    return largestRect


def matrixToHeights(matrix):
    # We skip the first row because its building height is fixed.
    # If we encounter 0, then we skip because the building height is 0.
    # Only if we get 1, then we add the previous building's height to the current.
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                # Current building height + whatever is the height above it.
                matrix[i][j] += matrix[i - 1][j]

    return matrix


def largestRectangleUnderSkyline(buildings):
    # Time = Space = O(n)
    """
    Logic:
    At every building we encounter, we check whether the current building is greater than the building in the stack.
    If yes, then we know that we can extend the stack's building further, so we add the current building also into
    the stack.
    If no, then we pop the building from the stack, get its height, we also calculate the width and then
    update the result accordingly, where area = width * height.

    """
    # Edge case
    if not buildings:
        return 0
    # The first element is
    stack = [0]
    # The current max area is the first building.
    result = buildings[0]
    # Now to handle the last element, we pad an extra height 0 at the end of the buildings array so that
    # we can pop out the last element.
    buildings = buildings + [0]
    # For each building starting from index 1.
    for i in range(1, len(buildings)):
        # If the current building is smaller or equal than the building in the stack.
        # We know that we cannot further extend the building width which in the top of the stack, so we pop it
        # and calculate its max area.
        while stack and buildings[i] <= buildings[stack[-1]]:
            # Getting the height of the stacks building
            height = buildings[stack.pop()]
            # If the stack if empty, then we take the entire width till the current index,
            # else we width = current index - 1 (previous building) - index of the stack's top building.
            width = i - stack[-1] - 1 if stack else i
            # Updating the max area
            result = max(result, width * height)
        # Adding the current buildings index to the stack.
        stack.append(i)
    return result


maximalRectangle(
    [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]])
