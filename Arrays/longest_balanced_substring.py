"""
Write a function that takes in a string made up of parentheses, and returns an integer representing the
length of the longest balanced substring with regard to parentheses.

string = "(()))("
expected = 4
"""


def longestBalancedSubstring(string):
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	We will move from left to right, now as we move, we will count the opening and closing brackets.
	If at any moment, # of opening == # of closing, then we will update the max result.
	Else, if closing > opening, then we reset the opening = closing = 0, because the parentheses become invalid at this
	point.

	Now we repeat the same above process by moving from right to left, we do it so that we can cover the edge
	case where # of opening > # of closing, in that case the above left to right will never catch the result.
	"""
	# We will return the max of whichever is greater, which is, from left to right, or from right to left.
	return max(getLongestInDirection(string, True), getLongestInDirection(string, False))


def getLongestInDirection(string, leftToRight):
	# Initializing opening and closing counters.
	opening = 0
	closing = 0
	# Result
	currMax = 0
	# Initializing the start and end index for traversing for either left or right direction
	start = 0 if leftToRight else len(string) - 1
	end = len(string) if leftToRight else -1
	step = 1 if leftToRight else -1

	for idx in range(start, end, step):
		# If we are moving from left to right,
		if leftToRight:
			# If the char is open
			if string[idx] == '(':
				opening += 1
			else:
				# Else for closing string.
				closing += 1
		else:
			# If we are moving from right to left, out open string is ')'
			# And the closing char becomes '('
			if string[idx] == ')':
				opening += 1
			else:
				closing += 1
		# If the opening == closing, then we have a balanced brackets so we update the result.
		if opening == closing:
			currMax = max(currMax, opening + closing)
		# If the closing > opening, then we will reset the counters
		if closing > opening:
			opening = 0
			closing = 0
	# Returning the longest balanced substring.
	return currMax
