"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. If there is no such substring,
return the empty string "".

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

"""


def minimumWindowSubstring(s, t):
	# Time = Space = O(s + t)
	"""
	Logic:
	As we move through the string s, we will update the count of the letters in the string t, and if we have all
	the letters of string t then we will update the result, if have == need, then we will enter in a while loop
	and try to shrink the substring size from the left (startIdx) and keep updating the result until have == need.
	"""
	# Edge case.
	if not t:
		return t

	# Result start, end index, and the length of the substring.
	result, resultLen = [-1, -1], float('inf')
	# We store the count of each letter inside a dictionary for both the strings.
	countT, countS = {}, {}
	# We update the dictionary with frequency of letters of string t
	for c in t:
		countT[c] = 1 + countT.get(c, 0)
	# Initializing the have and need variable
	# need = total number of unique chars in the string t.
	have, need = 0, len(countT)
	# Starting index of the substring.
	startIdx = 0
	# Looping over the string s
	for i in range(len(s)):
		# Char at index i
		c = s[i]
		# Updating the frequency of this letter for the string s dictionary
		countS[c] = 1 + countS.get(c, 0)
		# If the letter is in string t and also its frequency is equal to what is needed.
		if c in countT and countS[c] == countT[c]:
			# We say that we this letter for string t.
			have += 1
		# Until we have all the letters needed
		while have == need:
			# Updating the result if the current substring length is smaller.
			if resultLen > i - startIdx + 1:
				resultLen = i - startIdx + 1
				result = [startIdx, i + 1]
			# Now we try to shrink the substring if possible.
			# Getting the leftmost letter of the window.
			firstLetter = s[startIdx]
			# Decreasing its frequency by 1 because we will to the right.
			countS[firstLetter] -= 1
			# If this letter is in string t, and its frequency now has gone less than needed, then we will
			# decrement have by 1
			if firstLetter in countT and countS[firstLetter] < countT[firstLetter]:
				have -= 1
			# Moving the the start pointer of the window
			startIdx += 1
	# If the string was not found at all, then we return "", else return the sliced substring.
	return "" if resultLen == float('inf') else s[result[0]: result[1]]


print(minimumWindowSubstring(s="ADOBECODEBANC", t="ABC"))
