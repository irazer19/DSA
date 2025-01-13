"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

"""


def brute_force(k: int, prices: list[int]) -> int:
    """Brute Force Solution:
    Uses recursion to try all possible combinations of buying and selling
    For each day, we have three choices:

    Skip the day
    Buy stock (if we can buy)
    Sell stock (if we are holding)

    Time Complexity: O(3^n) where n is the number of days
    Space Complexity: O(n) due to recursion stack"""

    def recursive_profit(index: int, canBuy: bool, count: int) -> int:
        # Base cases
        if index >= len(prices) or count >= k:
            return 0

        # Skip current day
        profit = recursive_profit(index + 1, canBuy, count)

        if canBuy:
            # Buy stock on current day
            buy = -prices[index] + recursive_profit(index + 1, False, count)
            profit = max(profit, buy)
        else:
            # Sell stock on current day
            sell = prices[index] + recursive_profit(index + 1, True, count + 1)
            profit = max(profit, sell)

        return profit

    return recursive_profit(0, True, 0)


def maxProfitWithKTransactions(prices, k):
    # Time = Space = O(nk)

    """
    Idea: Either we can do the transaction today or keep the last daya's profit.
    If we do the transaction today, the profit = current days purchase price + max(last transactions profit.)
    """
    # Base case
    if k == 0 or not prices:
        return 0
    # Using DP, rows = number of transactions, columns = prices on each day.
    # Each cell represents: the max profit for ith transaction on jth day
    # 1st row and 1st col will be 0 because we cannot make profit for 0 transactions
    store = [[0 for _ in prices] for _ in range(k + 1)]

    # Starting with 1 transaction.
    for i in range(1, len(store)):
        # We will keep track of the max profit we made on last transaction till previous day.
        max_prev_trans = float("-inf")
        # Starting from day 1
        for j in range(1, len(store[0])):
            # Calculating the max profit till previous day, either existing profit is greater OR
            # the immediately previous day profit maybe greater.
            max_prev_trans = max(max_prev_trans, store[i - 1][j - 1] - prices[j - 1])
            # Calculating the max profit for today with jth transaction.
            # Which is = max(We dont do the transaction, We do the transaction)
            store[i][j] = max(store[i][j - 1], max_prev_trans + prices[j])

    # Max profit with kth transaction on nth day
    return store[-1][-1]


print(maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2))
