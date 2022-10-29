"""
Write a function that takes in a string and returns its longest substring without duplicate characters.

string = "clementisacap",
Output: "mentisac"

"""


def longestSubstringWithoutDuplication(string):
	# Time = Space = O(n)
	"""
	Logic:
	We will use start, end pointers to track the length of the substring.
	The end pointer will keep moving forward, and the start pointer will be updated if we see a duplicate
	letter again, now either the duplicate letter appeared before the start of the current substring, or after the
	start of the current substring.
	In any case, we will always update the longest substring result as we move forward.
	"""
	# Start, end pointers for the substring.
	start = 0
	end = 0
	# Store the longest substring result.
	longest = [0, 1]
	# Dictionary to store the last seen for the letters
	lastSeen = {}
	# We iterate to the end of the string.
	while end < len(string):
		# Getting the current letter.
		letter = string[end]
		# If the letter is already seen before
		if letter in lastSeen:
			# We update the start position of the substring.
			# We take max(current start position, last seen letters next position)
			start = max(start, lastSeen[letter] + 1)
		# We always update the last seen of every letter in the dictionary
		lastSeen[letter] = end
		# Updating the result with max substring length.
		longest = max(longest, [start, end], key=lambda x: x[1] - x[0])
		# Moving forward.
		end += 1
	
	return string[longest[0]: longest[1] + 1]
