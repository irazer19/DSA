"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]
"""


def findAllConcatenatedWordsInADict(words):
	# Time: O(n * w^2) and Space: O(n), where n is number of words, and w is length of the longest word.
	"""
	Logic
	For each word, we will break into multiple partitions to check whether its present in the word list.
	Its similar to word break problem, the only difference is that if a partition is present in the word list, then
	it should not be equal to the current word itself.
	"""
	# Creating dictionary for fast access
	wordSet = {w: True for w in words}
	# Storing result
	result = []
	# For each word
	for word in words:
		# If we were able to break the word and all those parts were present in the dictionary then we add this
		# word to the result.
		if wordBreak(word, wordSet):
			result.append(word)
	return result


def wordBreak(word, wordSet):
	# Storing whether the word is present starting from ith index
	dp = [False for _ in range(len(word) + 1)]
	# We will start from the end index, so we will pad an extra length to True
	dp[-1] = True

	# Starting from the end index
	for i in range(len(word) - 1, -1, -1):
		# We will compute multiple length of the word from ith index
		for j in range(i + 1, len(word) + 1):
			# If ith to jth word is present in the dictionary, and the next word which starts at jth index is also
			# True, and the current ith to jth word is not the same as the current entire word.
			if word[i: j] in wordSet and dp[j] and word[i: j] != word:
				# We mark at ith index that there is a word present here.
				dp[i] = True
				# We break because we dont need any more words to check at ith index since we already have found a word.
				break
	# The 0th index will either rbe True or False
	return dp[0]
