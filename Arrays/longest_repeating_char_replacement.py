"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

"""


def characterReplacement(s, k):
	# Time = Space = O(n)
	"""
	Logic:
	We will use sliding window here. As we iterate we will track the frequency of each letter.
	At every iteration, we will get the max frequency found so far and subtract it from the current window size to get
	the replaceable elements, the total number of replaceable elements must be <= k according to the question.
	If we see that the number of replaceable elements is > k, then we will decrease the window size by incrementing
	the start index
	"""
	# Frequency count table
	freq = {c: 0 for c in s}
	# Result
	result = 1
	# Start window index
	start = 0
	# End window index
	end = 0
	# Moving the window size
	while end < len(s):
		# Increasing the frequency count for the current letter
		freq[s[end]] += 1
		# Get the largest frequency in this window
		largestFreq = max(list(freq.values()))
		# Computing the total elements which need to be replaced
		toReplace = end - start + 1 - largestFreq
		# If the total replaceable elements is within k, then we compute the result
		if toReplace <= k:
			# The result is the entire current window since we can replace all the chars.
			result = max(result, end - start + 1)
			# Increasing the window size
			end += 1
		else:
			# Else, if we will decrease the window size and also remove the elements frequency which is at the
			# start index of the window.
			freq[s[start]] -= 1
			start += 1
			# Here we decrease the frequency of the current end window element because in the next loop we will
			# again encounter this element as we are not increasing the end pointer.
			freq[s[end]] -= 1

	return result
