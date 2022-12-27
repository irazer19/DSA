"""
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero. You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Input: s = "3+2*2"
Output: 7
"""


def calculate(s: str) -> int:
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	We iterate over all the characters, now we assume that the starting operator is +.
	If the current char is a digit, then we use another while loop to parse all the digits to form a number.
	Once we have a number, then we check what was is the current operator, depending on that we update the resultant
	sum.
	If the current char is not a digit but an operator, then we update the current operator.
	"""
	# To store the final result as we move.
	currSum = 0
	# Stores the previous number encountered
	prev = 0
	# Starting operator
	op = '+'
	# Starting from index 0
	i = 0

	while i < len(s):
		# If the current char is a digit.
		if s[i].isdigit():
			# We will form a number and parse all the next digits
			num = 0
			# While the next char is also a digit.
			while i < len(s) and s[i].isdigit():
				# Parsing it to a number
				num = num * 10 + int(s[i])
				i += 1
			# We decrement as we want to make the pointer to the last found digit.
			i -= 1

			# Now if the last seen operator was +, -, *, /
			if op == '+':
				currSum += num
				prev = num
			elif op == '-':
				currSum -= num
				prev = -num
			elif op == '*':
				# The logic is simple here,
				currSum -= prev
				currSum += num * prev
				prev = num * prev
			elif op == '/':
				currSum -= prev
				currSum += int(prev / num)
				prev = int(prev / num)
		# Now if the current char is not a digit and also not a whitespace, then it must be an operator.
		# So we update the operator variable.
		elif s[i] != ' ':
			op = s[i]
		i += 1
	return currSum
