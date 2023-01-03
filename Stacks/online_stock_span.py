"""
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for
the current day. The span of the stock's price in one day is the maximum number of consecutive days (starting from that
day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of the stock today is 2, then
the span of today is 4 because starting from today, the price of the stock was less than or equal 2 for 4 consecutive
days. Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then
the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3
consecutive days.

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.

Input
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]
Output
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4, because the last 4 prices (including today's price of 75) were less than or equal
							to today's price.
stockSpanner.next(85);  // return 6
"""


class StockSpanner:
	# Time = Space = O(n)
	"""
	Logic:
	As we get the new price, we will check the top element's price and compare. If the stack's top element price is
	less than or equal to the current price then we will pop that element and add its span to the current span.
	Finally, we will append the current computed span and current price in the stack.
	"""

	def __init__(self):
		self.stack = []

	def next(self, price: int) -> int:
		# Default span value
		span = 1
		# Until the current price is greater or equal to the stack's top element
		while self.stack and price >= self.stack[-1][0]:
			# We will pop the element from the stack and append its span to the current elements span
			prevPrice, prevSpan = self.stack.pop()
			span += prevSpan
		# Append the current price and span of today in the stack.
		self.stack.append([price, span])
		return span
