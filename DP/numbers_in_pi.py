"""
Given a string representation of Pi and an array of strings, find the minimum number of spaces required in the
string Pi such that all the seperated words are present in the array list.
PI = "3141592"
numbers = ["3141", "5", "31", "2", "4159", "9", "42"]

Output: 2
"""


def numbersInPi(pi, numbers):
    # Time: O(n^3 + m) and Space: O(n + m)
    # n is the number of digits in PI and m is the len(numbers).

    # We store all the items of the numbers in a hash table for easy access.
    numbersTable = {n: True for n in numbers}
    # Using DP, we store {idx: min_space}, which is the minimum space needed for string starting from idx to the end
    # of the string Pi. We approach bottom up, so we start from the end of the string.
    cache = {}
    # Starting from end, for each index we calculate the min_space.
    for i in range(len(pi) - 1, -1, -1):
        getMinSpaces(pi, numbersTable, cache, i)

    return cache[0] if cache[0] != float('inf') else -1


def getMinSpaces(pi, numbersTable, cache, idx):
    # This is the main recursive function.
    # If the idx is out of bound, then return -1. We return -1 because when we compute minSpaces we add +1, so
    # to negate that we add -1.
    if idx == len(pi):
        return -1
    # If the cache already contains the minSpace for the idx then return that.
    if idx in cache:
        return cache[idx]

    # Else, we initialize minSpaces to infinity.
    minSpaces = float('inf')
    # We start from the current idx to the end of the string Pi.
    # Ex: For 31415, if we start at 3 that means we are adding 1 space between 3(prefix) and 1415(suffix).
    # Similarly for next idx element 1, we add space between 31(prefix) and 415(suffix)
    for i in range(idx, len(pi)):
        # Slicing the prefix
        prefix = pi[idx: i + 1]
        # Only if the prefix is in the numbersTable we can add a space between prefix and suffix, else
        # move to next idx.
        if prefix in numbersTable:
            # Now we try to get the minSpaces for suffix.
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            # Calculating the minSpaces for idx, either the existing OR
            # 1 + minSpaces which we got from the suffix.
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    # Finally add the minSpaces for the idx in the cache.
    cache[idx] = minSpaces
    return minSpaces


print(numbersInPi("3141592", ["3141", "5", "31", "2", "4159", "9", "42"]))
