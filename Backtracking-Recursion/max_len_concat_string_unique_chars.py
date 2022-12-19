"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has
unique characters.
Return the maximum possible length of s.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the
order of the remaining elements.

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
"""


def maxLength(arr) -> int:
	# Time: O(2^n) and Space: O(n + n*w)
	"""
	Logic:
	We can either add the current word or the ignore it and move to the next index.
	First call will be when we choose to add it, then we will add all the letter frequency to the hash table and
	then move to the next index in function call.
	Second, we will choose not to add it, then we will first remove all the frequency of the letters from the hash table
	and then do the function call with the next index.

	Now the base case is, if we have the frequency of any letters > 1 in the hash table, then we will return max length
	as 0. And if the idx is out of bounds, then we will return the sum of the frequency of the letters in the hash table

	"""
	# Hash table
	table = {}
	return backtrack(arr, 0, 0, table)


def backtrack(arr, idx, currMax, table):
	# If the frequency of any letters > 1 in the hash table, we return 0 as the max length
	freq = list(table.values())
	if freq and max(freq) > 1:
		return 0
	# IF we have reached the end of the index, we return the sum of the frequency of the letters in the hash table
	if idx == len(arr):
		return sum(list(table.values()))
	# Current word
	currWord = arr[idx]
	# Adding the letter frequency in the hash table for the current word
	updateCount(table, currWord, add=True)
	# Calling with the next index
	currMax = max(currMax, backtrack(arr, idx + 1, currMax, table))
	# Removing the current words letters from the hash table.
	updateCount(table, currWord, add=False)
	# Calling the next index without adding the current word
	currMax = max(currMax, backtrack(arr, idx + 1, currMax, table))

	return currMax


def updateCount(table, word, add=True):
	for c in word:
		if add:
			table[c] = 1 + table.get(c, 0)
		else:
			table[c] -= 1
