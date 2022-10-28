"""
Write a function that takes in an array of strings and groups anagrams together.

words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
expected = [["yo", "oy"], ["flop", "olfp"], ["act", "tac", "cat"], ["foo"]]
"""


def groupAnagrams(words):
	# Time: O(w * nlogn) and Space: O(w*n)
	"""
	Logic:
	As we iterate over the words, we will sort the current word and then add it to the dictionary.
	The key will be the sorted word, and the value will be the original word itself.
	Because the anagrams after sorting will form the same word, this will work.
	"""
	# Storing word groups
	wordIdx = {}
	# For each word
	for i in range(len(words)):
		# Sorting the word
		word = ''.join(sorted(words[i]))
		# Adding the word in the dictionary for the sorted word as the key.
		if word not in wordIdx:
			wordIdx[word] = []
		# We append the original word to the dictionary value
		wordIdx[word].append(words[i])

	return list(wordIdx.values())
