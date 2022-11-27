"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words
beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest
transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
"""


def ladderLength(beginWord, endWord, wordList):
	# Time: O(n*m^2) and Space: O(n*m)
	"""
	Logic:
	First we create a graph, where the key is the all different patterns possible for the word and the value
	is the words which share that pattern. Ex: hot can have patterns [*ot, h*t, ho*].
	Once we have the graph, we will do a BFS from the beginWord, we will generate all the patterns for this word
	and then append all the next words to the queue which shared these patterns. After each layer we will increment
	the distance by one, which will give us our final result.
	If a word == endWord, then we return the result.
	"""
	# Edge case
	if endWord not in wordList:
		return 0
	# Creating the graph
	graph = {}
	# For each word
	for word in wordList:
		# For each letter in word
		for j in range(len(word)):
			# Pattern by replace the current letter with *
			pattern = word[:j] + '*' + word[j + 1:]
			# Adding the pattern in the graph along with the word
			if pattern not in graph:
				graph[pattern] = []
			graph[pattern].append(word)
	# BFS
	# Starting word
	q = [beginWord]
	# Result length is 1 because we have beginWord in the queue
	result = 1
	# Visited words
	visited = {beginWord}
	while q:
		# Looping the current layer
		for _ in range(len(q)):
			# Getting word from the left
			word = q.pop(0)
			# If the word matches with endWord, return the result.
			if word == endWord:
				return result
			# We will get all the next words from the graph using the patterns which will be formed by this word.
			for j in range(len(word)):
				# Pattern
				pattern = word[:j] + '*' + word[j + 1:]
				# Getting all the next words which share the same pattern
				for nextWord in graph.get(pattern, []):
					# If the nextWord has not been visited.
					if nextWord not in visited:
						# Appending to the queue.
						visited.add(nextWord)
						q.append(nextWord)
		# Updating the distance count after every layer.
		result += 1
	# Default response if the word could not be found.
	return 0


print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
