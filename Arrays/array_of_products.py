"""
Write a function that takes in a non-empty array of integers and returns an array of the same length, where each
element in the output array is equal to the product of every other number in the input array.

Input: = [5, 1, 4, 2]
Output: [8, 40, 10, 20]

"""


def arrayOfProducts(array):
    # Time = Space = O(n)
    """
    Logic:
    First we will traverse the array and collect all the product of all the left elements of every element in the array.
    Again we will traverse the array and collect all the right product of every element in the array.
    Next, we will traverse and multiply the left and right product result as the final result.
    """
    # Getting all left product
    leftProd = [1 for _ in array]
    # We start with index 1 because index 0th element has not left product so by default its 1.
    for i in range(1, len(array)):
        # The below line means, for the current element i
        # leftProd[i - 1] = Product till i - 1
        # array[i - 1] = Value at i - 1
        leftProd[i] = leftProd[i - 1] * array[i - 1]

    # Getting all the right product
    rightProd = [1 for _ in array]
    # We skin the last element because the last element does not have any right element to it, so its right
    # product by default is 1. Note: We go in reverse order for the right products.
    for i in range(len(array) - 2, -1, -1):
        rightProd[i] = rightProd[i + 1] * array[i + 1]
    # Combining the left and right product result by multiplying them.
    arrayProd = [leftProd[i] * rightProd[i] for i in range(len(array))]

    return arrayProd
