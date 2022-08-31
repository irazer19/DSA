"""
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array
such that the integers in the subsequence are sorted in increasing order
"""


def sum_seq(arr):
    # Time: O(n^2) and Space: O(n)
    # Using DP, at each index we store the maximum sum possible. Initially it is the value itself.
    store = [i for i in arr]

    # Since for index 0, the max value is the value itself so we start from index 1.
    for i in range(1, len(store)):
        # We compare the ith value with all the values from 0 to i-1
        for j in range(0, i):
            # If the ith value > jth value (increasing subsequence)
            if arr[i] > arr[j]:
                # We add the maximum of existing or the current
                store[i] = max(store[i], arr[i] + store[j])

    # Return the max score.
    return max(store)


print(sum_seq([1, 101, 2, 3, 100, 4, 5]))
