"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
"""


def evalRPN(tokens) -> int:
	# Time = Space = O(n)
	"""
	Logic:
	We will use stack to get all the numbers, and if we encounter an operator then we will pop two elements from
	the stack and do the operation and store the resultant number again in the stack.
	finally, we will return the last remaining number from the stack.
	"""

	stack = []
	# For each token
	for c in tokens:
		# If current char is an operator
		if c in ['+', '-', '*', '/']:
			# We will pop two elements from the stack
			num2 = stack.pop()
			num1 = stack.pop()
			# Do the operation between the num1 and num2 and store in the result in the stack
			if c == '+':
				stack.append(num1 + num2)
			elif c == '-':
				stack.append(num1 - num2)
			elif c == '*':
				stack.append(num1 * num2)
			elif c == '/':
				stack.append(int(num1 / num2))
		else:
			# If the current char is a digit, we store in the stack
			stack.append(int(c))
	# Result
	return stack[-1]
