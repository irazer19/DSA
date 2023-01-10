"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
The following rules define a valid string:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Input: s = "(*))"
Output: true
"""


def checkValidString(s: str) -> bool:
	# Time = Space = O(n)
	"""
	Logic:
	We will maintain two stacks, one to store all the balanced brackets and other to store all the * we get.
	We will store the indices of it.
	Once done, we will now check the brackets stack, if it has something then we will pop it and check in the
	asterisk stack whether for that bracket we can have an asterisk as wildcard, if yes then we will pop that asterisk,
	else we will return False.
	"""

	# Stores all the brackets
	stackB = []
	# Stores all the asterisk
	stackA = []
	# For each char
	for i in range(len(s)):
		# IF its open
		if s[i] == '(':
			# We will just add to stack
			stackB.append(i)
		elif s[i] == ')':
			# Else if the top stack already has open, then we will pop
			if stackB and s[stackB[-1]] == '(':
				stackB.pop()
			else:
				# Else will add it to stack.
				stackB.append(i)
		else:
			# IF its *, then we will add in the asterisk stack
			stackA.append(i)

	# Now here we try to find a wildcard for each remaining brackets in the stack
	while stackB:
		# Getting the top bracket index from stack
		brackIdx = stackB.pop()
		# IF its open
		if s[brackIdx] == '(':
			# We want the closing to have greater index than the opening, so we will start checking from the
			# right end of the stackA for the asterisk index
			if stackA and stackA[-1] > brackIdx:
				stackA.pop()
			else:
				# Case where we could not find any asterisk which has greater index than current opening bracket
				return False
		else:
			# IF the bracket is closing
			# We will start searching from the 0th index of the stackA because we want the asterisk index to be smaller
			# than the current closing bracket. And we also want the largest such index.
			idx = 0
			if stackA and stackA[idx] < brackIdx:
				# Until Asterisk index is smaller than current closing bracket index
				while stackA and idx < len(stackA) and stackA[idx] < brackIdx:
					# We move to the next index
					idx += 1
				# Come back to the best index
				idx -= 1
				# Remove that asterisk from the stack
				stackA.pop(idx)
			else:
				return False
	return True
