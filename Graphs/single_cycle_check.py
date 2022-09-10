"""
You're given an array of integers where each integer represents a jump of its value in the array. For instance, the
integer 2 represents a jump of two indices forward in the array; the integer -3 represents a jump of three indices
backward in the array.

If a jump spills past the array's bounds, it wraps over to the other side. For instance, a jump of -1 at index © brings
us to the last
index in the array. Similarly, a jump of 1 at the last index in the array brings us to index e

Write a function that returns a boolean representing whether the jumps in the array form a single cycle. A single cycle
occurs if, starting at any index in the array and following the jumps, every element in the array is visited exactly
once before landing back on the starting index.

"""


def hasSingleCycle(array):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We will track the number of nodes we visit using numElementsVisited. We will keep the start index as 0.
    Using the while loop, we will compute the next node to visit and also update the numElementsVisited +=1.
    If we are back at the starting index after visited few other elements then we return False.
    Else the while loop will terminate if numElementsVisited == total elements, once we are out of the loop,
    if we are back at the starting index then we return True else False.

    """
    # Edge case
    if not array:
        return True

    # Tracking total visited elements
    numElementsVisited = 0
    # Keeping start index as 0, hardcoded!
    start = 0
    # Starting node
    node = 0

    # Until we have visited all elements
    while numElementsVisited < len(array):
        # If we have already visited other elements and still come back at start index then definitely
        # there is a cycle and we return False.
        if numElementsVisited > 0 and node == start:
            return False

        # Increasing the visited count
        numElementsVisited += 1
        # Next node = (current index + current value) % total elements, this works even for -ve values because
        # in python, taking % will automatically convert to positive number.
        node = (node + array[node]) % len(array)
    # If we are at the start index return True else return False
    return node == start


print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
