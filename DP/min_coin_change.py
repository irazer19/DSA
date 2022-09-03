"""
Given an unlimited supply of coins of given denominations, find the minimum number of coins required to get
the desired change.

"""


def minNumberOfCoinsForChange(n, denoms):
    # Time: O(n x d) and Space: O(n)
    # Using DP, we store the minimum coin for each target change from 1 to n, inclusive.
    # Initializing the store with infinity.
    # For n=0, we need 0 coins.
    store = [float('inf') for i in range(n + 1)]
    store[0] = 0

    # Starting change from 1 to n, inclusive.
    for amt in range(1, len(store)):
        # For each target change, we will use all the denoms to find the minimum coin that was needed to make this
        # target change.
        for d in denoms:
            # Only if the current coin <= target change.
            if d <= amt:
                # Result is: Either the existing value is minimum OR 1 + min coins needed for remaining amount.
                # We add + 1 to indicate we have used the current coin.
                store[amt] = min(store[amt], 1 + store[amt - d])

    # Now if the min coin value for n is still infinity then we were not able to make the change.
    return -1 if store[-1] == float('inf') else store[-1]


print(minNumberOfCoinsForChange(7, [1, 5, 10]))
