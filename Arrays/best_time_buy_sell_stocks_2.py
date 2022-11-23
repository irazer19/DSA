"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
"""


def maxProfit(prices) -> int:
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	We do the transaction on each day. We compare the current price with the previous day price, if its greater,
	then we do the transaction and add the profit to the result.
	"""
	profit = 0
	# We start from index 1, because on index 0, we cannot do any transaction.
	for i in range(1, len(prices)):
		# If the current day price is greater than previous day price
		if prices[i - 1] < prices[i]:
			# We do the transaction and add it to the profit.
			profit += prices[i] - prices[i - 1]
	return profit
