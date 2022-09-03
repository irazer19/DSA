"""
Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if the length of the
rod is 8 and the values of different pieces are given as the following, then the maximum obtainable value is 22
(by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
"""


def rodCutting(n, prices):
    # Time: O(n^2) and Space: O(n)
    # Using DP, we will use the store array to store the max price till rod of length i.
    # We add an extra 0 to start with rod length of 0 whose price is 0.
    store = [0] + [p for p in prices]

    # Now we start calculating for rod of length starting from 1 to n (inclusive)
    for i in range(1, n + 1):
        # We try to cut the current length rod in various ways, j represents the cut size.
        for j in range(0, i):
            # Here we calculate the max profit. Either the existing price or
            # (price of the cut size + price of the remaining size)
            store[i] = max(store[i], store[j] + store[i - j])

    return store[-1]


print(rodCutting(5, [2, 5, 7, 8, 10]))
