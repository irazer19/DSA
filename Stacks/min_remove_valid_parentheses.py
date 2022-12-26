"""
Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
"""


def minRemoveToMakeValid(s: str) -> str:
	# Time = Space = O(n)
	"""
	Logic:
	We will loop over every character, we will use a stack to keep track of balanced parentheses.
	If a closing bracket appears before opening bracket, then we will mark that index = "" because its an invalid char.
	Finally, after the loop if over, and we still have some brackets in the stack, then we know that those aren't
	required, so we make those indices also as "" string.

	"""
	# Converting to array
	s = list(s)
	stack = []
	# For every char
	for i in range(len(s)):
		c = s[i]
		# If the char is open
		if c == '(':
			# Just append to the stack
			stack.append(i)
		elif c == ')':
			# If for closed char
			# If the top value of the stack is open then pop it out
			if stack and s[stack[-1]] == '(':
				stack.pop()
			else:
				# Else the current closing bracket is invalid, and we will mark "" at this index
				s[i] = ''
	# Finally, if the stack contains some elements, then we will mark "" string for those elements
	for i in stack:
		s[i] = ''

	return ''.join(s)
