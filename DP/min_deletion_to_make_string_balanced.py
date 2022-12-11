"""
You are given a string s consisting only of characters 'a' and 'b'
You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j)
such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
"""


def minimumDeletions(s: str) -> int:
	# Time: O(n) and Space: O(n)
	"""
	Logic:
	Store all the a's frequency count at every index starting from the end.
	Now loop from the start of the string, if the char == 'b', then we do the following:
	1. Get total a's that occur after the current 'b'.
	2. Total b's that have already occured before the current 'b'.

	Now we want to achieve this format: aaabbb, so we delete all the b's before the current b and remove all
	the a's after the current b, and update the result of the total deletion at every b.

	"""
	# At every index, we count the total a's to its right.
	aFreq = [0 for _ in s]
	for i in range(len(s) - 1, -1, -1):
		if s[i] == 'a':
			aFreq[i] = 1 if i == len(s) - 1 else 1 + aFreq[i + 1]
		else:
			aFreq[i] = 0 if i == len(s) - 1 else aFreq[i + 1]
	# Final result which stores the min deletion.
	result = float('inf')
	# To count how many b's we have seen before.
	bCount = 0
	# For each char in string.
	for i in range(len(s)):
		# If the char is b
		if s[i] == 'b':
			# Updating the result, where total deletion we are making = total b's to left + total a's to right.
			result = min(result, bCount + aFreq[i])
			# Incrementing the b counter
			bCount += 1
	# Finally, we again check, if the total b's we have seen is less than the total deletions we have made,
	# then its better to delete all those b's and make that as the result.
	result = min(result, bCount)

	return result if result != float('inf') else 0
