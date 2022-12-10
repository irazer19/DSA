"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings,
 return any of them. If there is no such string, return the empty string "".

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
"""

import heapq


def longestDiverseString(a: int, b: int, c: int) -> str:
	# Time: O(a + b + c) and Space: O(a + b + c)
	"""
	Logic:
	We will push the letters with the frequency as the key in the max heap.
	Next, we will pop the element from the max heap, and then add it to the result array, if the last two
	letters are same as the current one, then we will hold this letter in "previous" variable and process with the
	next element in the heap, once we add the next element, then we will append this previous letter in the result.
	As we insert back the letter, we will decrease its frequency count by 1.
	"""
	# Initializing the heap
	heap = []
	# Adding the letters to the heap, where the frequency is the key.
	if a > 0:
		heapq.heappush(heap, (-a, 'a'))
	if b > 0:
		heapq.heappush(heap, (-b, 'b'))
	if c > 0:
		heapq.heappush(heap, (-c, 'c'))

	# Result
	result = []
	# To hold the letter if the last two letters of the result are the same
	prev = None
	while heap:
		# Getting the current letter
		curr = heapq.heappop(heap)
		# If the frequency of this letter is 0, then ignore the letter and move to the next letter
		if curr[0] == 0:
			continue
		# If the last two letters in the result and the current letter is same, then we set the current letter to prev.
		if len(result) >= 2 and result[-2] == result[-1] == curr[1]:
			prev = curr
			# After setting the prev, if we see that the heap is empty, then we will break.
			if not heap:
				break
			# We use continue because we directly want the next letter.
			continue
		else:
			# Else, we add the current letter to the result, and push this letter again in the heap by decreasing its
			# frequency.
			result.append(curr[1])
			heapq.heappush(heap, (curr[0] + 1, curr[1]))
		# If prev exists
		if prev:
			# Add to the result
			result.append(prev[1])
			# Push the letter again by decreasing its frequency
			heapq.heappush(heap, (prev[0] + 1, prev[1]))
			# Reset the prev variable
			prev = None
	return ''.join(result)
