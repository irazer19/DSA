"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears
in at most one part. Note that the partition is done so that after concatenating all the parts in order, the resultant
string should be s.
Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
"""


def partitionLabels(s):
	# Time = Space = O(n)
	"""
	Logic:
	We will first store all the max index of each letter in a hash table.
	We will maintain a start and end window index.
	Start window starts from 0, and then we compute the end window by getting the largest index of that letter
	present in the string s.
	Now since we have start & end window, we will loop over all letters within the window and update the end window
	if one of the letter has larger index value.
	Once we have looped over all the window elements, we will add the (end - start + 1) to the result, and now
	the start window = end + 1

	"""
	# Get max index for each and every letter
	idxTable = {}
	for i in range(len(s)):
		idxTable[s[i]] = max(idxTable.get(s[i], -1), i)
	# Storing the result
	result = []
	# Start and end window index
	start = 0
	end = 0
	while start < len(s):
		# Getting the end window for the current characters max index found in the string s.
		end = max(idxTable[s[start]], end)
		# Now we iterate over all the elements between start and end window
		j = start
		while j < end:
			# If the jth elements largest index is greater than the current end index, then we update it because
			# we want all the occurrences of this element in the same window.
			end = max(idxTable[s[j]], end)
			j += 1
		# Finally, we add to the result
		result.append(end - start + 1)
		# Now we update the start window = the next index after the current end window index.
		start = end + 1

	return result
