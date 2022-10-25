"""
Write a function that takes in an array of at least three integers and, without sorting the input array, returns a
sorted array of the three largest integers in the input array.

array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
threeLargest: [18, 141, 541]

"""


def findThreeLargestNumbers(array):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    We will initialize an array with 3 items to -infinity for storing the three largest integers.
    As we iterate over the array, we will compare the number with the 1st largest, then 2nd largest, then 3rd largest
    element of the threeLargest array.
    If the number is greater than any of those three, then we will shift the existing elements of the threeLargest
    array to the left and replace with the new number at the index.
    """
    # Initializing the three largest elements
    largestThree = [float('-inf'), float('-inf'), float('-inf')]
    # For each number in the array
    for num in array:
        # If the number is greater than the 1st largest, we will shift the elements to the left
        # starting from index 0 to 2(exclusive), then we replace with the new number at index 2.
        if num > largestThree[2]:
            shiftAndUpdate(2, largestThree, num)
        # We do the same thing for 2nd largest and 3rd largest elements.
        elif num > largestThree[1]:
            shiftAndUpdate(1, largestThree, num)
        elif num > largestThree[0]:
            shiftAndUpdate(0, largestThree, num)

    return largestThree


def shiftAndUpdate(endIdx, largestThree, newVal):
    # For each index, we will update its value = the next array value because we are shifting left.
    for i in range(endIdx):
        largestThree[i] = largestThree[i + 1]
    # Updating the array at endIdx with the new value
    largestThree[endIdx] = newVal
