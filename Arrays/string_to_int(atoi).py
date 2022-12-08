"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi
function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is
either. This determines if the final result is negative or positive respectively. Assume the result is positive if
neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the
string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
Change the sign as necessary (from step 2).

If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in
the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be
clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
"""


def myAtoi(s: str) -> int:
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	1. First remove the left whitespaces
	2. Now check the first index value, if its a sign(+ ,-), then store that sign into a variable.
	3. Iterate through the string, and check whether its a digit, if not break, if yes then construct the integer using
	parsed = parsed * 10 + current number
	4. Now we have the parsed integer, multiply it with the sign variable.
	5. If the integer is < -2**31 return -2**31 elif the integer > 2**31 - 1 then return 2**31 - 1 else return parsed.
	"""

	# Removing thw whitespace
	s = s.lstrip()
	# If the string is empty, then return 0
	if not s:
		return 0
	# Starting index.
	idx = 0
	# Default sign is positive
	sign = 1
	# If the first char is negative, then we create -1
	if s[0] == '-':
		sign = -1
		# Move to the next index.
		idx += 1
	elif s[0] == '+':
		idx += 1

	# Result
	parsed = 0
	# Iterate over the string.
	while idx < len(s):
		# If not digit, break
		if not s[idx].isdigit():
			break
		# Construct the integer using the current digit.
		parsed = parsed * 10 + int(s[idx])
		# Moving to the next char
		idx += 1
	# Final result with sign.
	parsed *= sign
	# Conditions according to the question for returning the result.
	if parsed > (2 ** 31) - 1:
		return (2 ** 31) - 1
	elif parsed < -2 ** 31:
		return -2 ** 31
	return parsed
