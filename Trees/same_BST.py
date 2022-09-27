"""
An array of integers is said to represent the BST obtained by inserting each integer in the array, from left to right,
into the BST.
Given arrayOne and arrayTwo, determine whether these arrays represent the same BST.
You're not allowed to construct any BSTs in your code.

Input:
    arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
    arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]

Output: True
"""


def sameBsts(arrayOne, arrayTwo):
    # Time: O(n^2) and Space: O(d), d is the depth.
    """
    Logic:
    Here we have to compare the array values such that they represent the same BST.
    For both the arrays we maintain a root pointer which points to the root of the current tree.
    We start the function call by comparing the root values of the array, if they are not the same then return False,
    Else, we get the next root for the left and right subtrees for both the arrays, and call the function again with
    the given lower and upper bounds of the root.

    If both the left and right subtrees return True then we return True.
    While finding the next root value, let's say for left tree, we want the next value < current root and
    the value should be between its lower and upper bounds to satisfy the BST property.

    """

    # Starting root node is 0 for both the arrays, and root range is -inf to inf.
    return compareBST(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))


def compareBST(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, lower, upper):
    # If the length of the two arrays is not equal, we return False directly.
    if len(arrayOne) != len(arrayTwo):
        return False

    # If we did not find any next root, then we get -1, so at this point we check, if both the
    # arrays root idx is -1 then we return True because both are None.
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo

    # If the current root value of the two arrays is not same then return False.
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    # Getting the next root for the left and right subtrees for both the arrays.
    # We also pass the updated lower and upper bounds for the next root.
    arrayOneLeftRootIdx = getLeftRootIdx(arrayOne, rootIdxOne, lower, arrayOne[rootIdxOne] - 1)
    arrayOneRightRootIdx = getRightRootIdx(arrayOne, rootIdxOne, arrayOne[rootIdxOne], upper)
    arrayTwoLeftRootIdx = getLeftRootIdx(arrayTwo, rootIdxTwo, lower, arrayOne[rootIdxOne] - 1)
    arrayTwoRightRootIdx = getRightRootIdx(arrayTwo, rootIdxTwo, arrayOne[rootIdxOne], upper)

    # Recursively comparing the left subtree of both the arrays, and the right subtree of both the arrays.
    leftTreeResult = compareBST(arrayOne, arrayTwo, arrayOneLeftRootIdx, arrayTwoLeftRootIdx,
                                lower, arrayOne[rootIdxOne] - 1)
    rightTreeResult = compareBST(arrayOne, arrayTwo, arrayOneRightRootIdx, arrayTwoRightRootIdx,
                                 arrayOne[rootIdxOne], upper)

    # True only if both the sides were True.
    return leftTreeResult and rightTreeResult


def getLeftRootIdx(arr, currentRootIdx, lower, upper):
    # Finding the next root for the left subtree.
    rootVal = arr[currentRootIdx]
    for i in range(currentRootIdx + 1, len(arr)):
        # BST Property
        if arr[i] < rootVal and lower <= arr[i] <= upper:
            return i
    # Return -1 if we dont find any such index
    return -1


def getRightRootIdx(arr, currentRootIdx, lower, upper):
    # Finding the next root for the right subtree
    rootVal = arr[currentRootIdx]
    for i in range(currentRootIdx + 1, len(arr)):
        if arr[i] >= rootVal and lower <= arr[i] <= upper:
            return i
    # Return -1 if we dont find any such index
    return -1
