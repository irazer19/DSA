"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
exactly k times. Note that k is guaranteed to be a positive integer.

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"
"""


def decodeString(s: str) -> str:
	# Time = Space = O(n)
	"""
	Logic:
	We will iterate over every char. If the char is an alphabet then we will store in the res list,
	if the char is a digit, then we will parse all the digits which follow until we hit a "[", at this point we
	will do recursion and the return will be a string which we will multiply with the number which we parsed.
	Now, if we hit a case where we find the char as closing bracket "]", we will break and return the result

	We will also track the visited indices.
	"""
	# Tracking the visited indices
	visited = set()
	return solve(s, visited, 0)


def solve(s, visited, idx):
	# Stores result for current layer
	res = []

	while idx < len(s):
		# If this index has not been visited.
		if idx not in visited:
			# Visited it
			visited.add(idx)
			# If this char is an alphabet
			if s[idx].isalpha():
				# Append to the result
				res.append(s[idx])
			elif s[idx].isdigit():
				# If its a digit, then we will parse all the digits which may come after it.
				num = 0
				while idx < len(s) and s[idx].isdigit():
					# Mark as visited.
					visited.add(idx)
					num = num * 10 + int(s[idx])
					idx += 1
				idx -= 1
				# Now we want to multiple the bracket's content with the above parsed number, so we make a recursive
				# call, and then add it to the result.
				res.append(solve(s, visited, idx + 1) * num)
			elif s[idx] == ']':
				# If we hit a closing bracket, we will break
				break
		idx += 1
	# returning the resultant string
	return ''.join(res)
