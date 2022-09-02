"""
Find the total number of ways to make a change for the sum k using the coins.
You may assume unlimited coins.
"""


def numberOfWaysToMakeChange(n, denoms):
    # Time = O(n x d), n = target sum, d = denominations.
    # If we dont have any coin, we can only have 0 sum
    if not denoms:
        return 0
    # Using DP, For each sum starting from 0, we will find the total ways to reach that sum
    arr = [0 for _ in range(n + 1)]
    # Initially, for sum=0, total ways is 1 because we can always have 0 rupees.
    arr[0] = 1
    # Using each denoms, we will find the total ways to reach all the sum from 1 to n.
    for d in denoms:
        for i in range(1, len(arr)):
            # Only if the coin is smaller or equal to the current target sum.
            if i >= d:
                # When we do target - coin, we get the remaining amount, so the number of ways we can reach
                # that remaining amount is the same for current amount.
                arr[i] += arr[i - d]
    return arr[-1]


print(numberOfWaysToMakeChange(4, [1, 2, 3]))
