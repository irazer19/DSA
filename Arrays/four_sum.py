"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array
of all these quadruplets in no particular order.

array= [7, 6, 4, -1, 1, 2], target=16
quadruplets = [[7, 6, 4, -1], [7, 6, 1, 2]]

https://leetcode.com/problems/4sum/description/
"""


def fourNumberSum(array, targetSum):
    """
    Brute Force:
    Use 4 nested loops to find all the quadruplets.
    Time: O(n^4) and Space: O(1)

    Optimized:
    AS we iterate, we will first get the sum of i and i+1 elements and check whether the remaining sum
    target-currSum exists in the dictionary, if yes then we will add it to the result, else move to the next element.
    After we have exhausted all the elements till n, next we will take the sum of i and all its previous elements
    till 0th index and store the sum in the dictionary.

    Time: O(n^2) and Space: O(n^2) because we are storing pairs.
    """
    # Dictionary to store the sum of two elements.
    sumStore = {}
    result = []
    # We dont start with index 0 because we do not have any previous elements to compute the sum and store in the
    # dictionary.
    # Also we skip the last element because we dont have any next elements to compute the sum with.
    for i in range(1, len(array) - 1):
        # Iterating over all the next elements from the current index, adding it with the current element, and
        # checking whether the remaining sum is present in the dictionary.
        for j in range(i + 1, len(array)):
            currSum = array[i] + array[j]
            remainderSum = targetSum - currSum
            # If present in the dictionary
            if sumStore.get(remainderSum, None):
                # We loop every possible duplets to make a quadruplet, and store in the result.
                for item in sumStore.get(remainderSum):
                    result.append([array[i], array[j]] + item)
        # Now we iterate from the start of the array except the current index, add the sum to the dictionary
        # along with the duplets as the value.
        for k in range(0, i):
            currSum = array[i] + array[k]
            if currSum not in sumStore:
                sumStore[currSum] = []
            sumStore[currSum].append([array[i], array[k]])

    return result
