"""
A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example,
in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
"""


def minDeletions(s: str) -> int:
	# Time: O(n * Freq) and space: O(n), where n is the total chars, and Freq is the max freq value.
	"""
	Logic:
	First we compute the frequency of all the characters in the string, and then loop over the frequencies, and
	check whether its present in the seen hash table or not. If no, then add it. If yes, then subtract the
	frequency by 1 and check again until frequency becomes 0.
	As we move forward, we will keep updating the seen hash table with the unique frequency of the characters.
	Also, while decreasing the frequency count, we will increase the min deletion count for the result.
	"""
	# Stores all the frequencies of the characters in the string
	freq = {}
	for c in s:
		if c not in freq:
			freq[c] = 0
		freq[c] += 1
	# Seen hash table
	seen = {}
	# Result to store min deletion
	result = 0
	# For each frequency
	for f in list(freq.values()):
		# If we have seen this frequency, then we will keep reducing it by 1 and check again.
		while seen.get(f, 0) > 0:
			f -= 1
			# Increasing the result
			result += 1
		# Once out of the while loop, we will add the current unique frequency for this letter to the hash table only
		# if the frequency > 0
		if f > 0:
			if f not in seen:
				seen[f] = 0
			seen[f] += 1

	return result
