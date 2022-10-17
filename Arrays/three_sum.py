"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array
of all these triplets.

Input: [12, 3, 1, 2, -6, 5, -8, 6]
Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""


def threeNumberSum(array, targetSum):
    # Time: O(n^2) and Space: O(n)
    """
    Logic:
    First we sort the array, then we use three pointers.
    The first pointer will be fixed as we move the second and third pointers to find the target sum.
    Once the second pointer and third pointers have crossed each other, then we first pointer moves, and then
    we again reset the second and third pointers.
    If the sum of these three pointers equal to the target sum, then we add it to the result.
    """
    # Sorting the array so that we can move the pointers in the correct direction.
    array.sort()
    # To store all the triplets equal to the target sum.
    result = []
    # Iterating through the array elements which will be out first pointer, we skip the last two elements
    # so that there is a room for second and third pointers.
    for firstPtr in range(len(array) - 2):
        # Setting the second and third pointers.
        secondPtr = firstPtr + 1
        thirdPtr = len(array) - 1

        # We move the second and third pointers until they cross each other.
        while secondPtr < thirdPtr:
            # Computing the current sum
            currSum = array[firstPtr] + array[secondPtr] + array[thirdPtr]
            # If the current sum is greater than target, we move the third pointer to decrease the overall sum
            if currSum > targetSum:
                thirdPtr -= 1
            elif currSum < targetSum:
                # Else if the current sum is less than target, we move the second pointer to increase the overall sum
                secondPtr += 1
            else:
                # Else we add the current triplets to the result and move both the pointers.
                result.append([array[firstPtr], array[secondPtr], array[thirdPtr]])
                secondPtr += 1
                thirdPtr -= 1
    return result
