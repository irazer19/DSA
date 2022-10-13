"""
Write a function that takes in an array of positive integers representing the heights of adjacent buildings and returns
the area of the largest rectangle that can be created by any number of adjacent buildings, including just one
building. Note that all buildings have the same width of 1 unit.

Input: [1, 3, 3, 2, 4, 1, 5, 3, 2]
Output: 9

"""


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
