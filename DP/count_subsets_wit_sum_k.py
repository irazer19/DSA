"""
Given an array arr[] of length N and an integer k, the task is to find the number of subsets with a sum equal to k.
"""


def brute_force(arr, k):
    # Time = O(2^n), Space = O(n)
    # We try with every element and add to the current sum and move to the next index using recursion.
    res = Res()

    def solve(arr, k, idx, total, res):
        if k == total:
            res.res += 1
            return
        for i in range(idx, len(arr)):
            if total + arr[i] > k:
                continue
            solve(arr, k, i + 1, total + arr[i], res)

    solve(arr, k, 0, 0, res)
    return res.res


class Res:
    def __init__(self):
        self.res = 0


def CountSubsets(arr, k):
    # Time = Space = O(n x k)
    # Using DP, creating a matrix of size n x k
    # Each cell represents: The total number of subsets for sum j
    store = [[0 for _ in range(k + 1)] for _ in range(len(arr) + 1)]
    # The first column is 1 because for sum=0, we can always created a subset by not adding the value.
    for i in range(len(store)):
        store[i][0] = 1

    # Filling the rest of the matrix starting from 1, 1
    for i in range(1, len(store)):
        for j in range(1, len(store[0])):
            # If the current value is at least equal to the current sum j
            if j >= arr[i - 1]:
                # We store the total ways = total ways after adding the element + total ways by not adding the element
                store[i][j] = store[i - 1][j - arr[i - 1]] + store[i - 1][j]
            else:
                # Else, since we cannot add the element, we store only the total ways by not adding the element.
                store[i][j] = store[i - 1][j]

    return store[-1][-1]


print(brute_force([1, 2, 3, 3], 6))
