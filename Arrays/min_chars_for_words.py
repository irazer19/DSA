"""
Write a function that takes in an array of words and returns the smallest array of characters needed to form all
of the words.

input = ["this", "that", "did", "deed", "them!", "a"]
expected = ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"]
"""


def minimumCharactersForWords(words):
	# Time: O(n * l) and Space: O(c), n is the number of words, l is the longest length of a word,
	# c is the number of unique letters
	"""
	Logic:
	We will calculate the frequency of letters for every word, then compare it with the frequency of resultant
	letters, then update that letters frequency if the current words' frequency > existing resultant frequency.
	"""
	# Resultant frequency
	finalFreq = {}
	# For every word
	for word in words:
		# Current words letter frequency.
		currWordFreq = {}
		# For every letter
		for letter in word:
			# Updating the letters frequency
			if letter not in currWordFreq:
				currWordFreq[letter] = 0
			currWordFreq[letter] += 1
		# Update the resultant frequency.
		for letter, freq in currWordFreq.items():
			# If the letter is in resultant frequency.
			if letter in finalFreq:
				# We will update the final frequency to max of the two for this letter.
				finalFreq[letter] = max(freq, finalFreq[letter])
			else:
				# If this letter is not in final frequency, we will add it.
				finalFreq[letter] = freq
	# Returning the result in the expected format.
	return freqToChar(finalFreq)


def freqToChar(finalFreq):
	result = []
	for letter, freq in finalFreq.items():
		result += [letter] * freq
	return result
