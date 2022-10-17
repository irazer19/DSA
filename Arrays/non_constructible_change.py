"""
Given an array of positive integers representing the values of coins in your possession, write a function that
returns the minimum amount of change that you cannot create. The given coins can have any positive integer value and
aren't necessarily unique.

input = [1, 2, 5]
Output: 4

"""


def nonConstructibleChange(coins):
    # Time: O(nlogn) and Space: O(1)
    """
    Logic:
    First we sort the coins, and then we maintain a currSum as we traverse through the coins.
    If a coin is greater than current sum + 1, then we cannot create a currSum + 1 amount.
    """

    coins.sort()
    currSum = 0
    # For each coin.
    for coin in coins:
        # If the current coin is greater than the current sum + 1, we return the currSum + 1
        if coin > currSum + 1:
            return currSum + 1
        # Updating the current sum
        currSum += coin

    # Since we have exhausted all the coins, we know that we cannot create currSum + 1 amount.
    return currSum + 1
