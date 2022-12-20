"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the
mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


def numDecodings(s: str):
	# Time = Space = O(n)
	"""
	Logic:
	We start from the end of the string, if the current letter is between [1, 26] then we can use this letter
	so the total ways for it becomes = result in i + 1.
	Now we can also make the current i and i+1 letters as 2 digit and decode it, if we do so then the total ways =
	current existing ways + result at i + 2
	"""
	# Initializing dp to store the result at every index
	dp = [0 for _ in range(len(s) + 1)]
	# The last index is dummy so we add 1.
	dp[-1] = 1
	# Starting from the end
	for i in range(len(s) - 1, -1, -1):
		# If the current letter is 0, we store 0 in the result
		if s[i] == '0':
			dp[i] = 0
		else:
			# Else, we consider a single digit for the current letter and therefor store the result of i + 1
			dp[i] = dp[i + 1]
			# Now we also consider 2 digit number for decode.
			# If the index is in bound, and the first digit = 1, then we are okay to have 10..to 19.
			# If the first digit is 2, then we want the second digit to be between [0, 6]
			if i + 2 < len(dp) and int(s[i]) == 1 or (int(s[i]) == 2 and i + 1 < len(s) and 0 <= int(s[i + 1]) <= 6):
				# Also storing the i + 2 index result because we considered i and i + 1 as a 2 digit number
				dp[i] += dp[i + 2]
	return dp[0]
