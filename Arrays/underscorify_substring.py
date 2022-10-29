"""
Write a function that takes in two strings, a main string and a potential substring of the main string.
The function should return a version of the main string with every instance of the substring in it wrapped between
underscores.
If two or more instances of the substring in the main string overlap each other or sit side by side, the underscores
relevant to these substrings should only appear on the far left of the leftmost substring and on the far right of the
rightmost substring. If the main string doesn't contain the other string at all, the function should return the main
string intact.

string = "testthis is a testtest to see if testestest it works",
substring = "test"

output = "_test_this is a _testtest_ to see if _testestest_ it works",
"""


def underscorifySubstring(string, substring):
	# Time: O(n + m) because of .find method which uses knuth morris pratt algorithm.
	# Space: O(n)
	"""
	Logic:
	The solution is divided into three parts:
	1. Getting all the locations of the substring, the start and end indices.
	2. Collapsing/merging the locations if it's overlapping, and then flattening the locations.
	3. Underscorify, At every index of the locations array, we will add the underscore.
	"""
	# Getting the flattened locations
	locations = collapse(getLocations(string, substring))
	# Building the new string with underscores
	return underscorify(string, locations)


def getLocations(string, substring):
	# We will search for the substring from this start index
	startIdx = 0
	# Storing all the [start, end] index for the substring found in the string.
	locations = []
	while startIdx < len(string):
		# Finding the substring
		nextIdx = string.find(substring, startIdx)
		# If found
		if nextIdx != -1:
			# We will append the result
			locations.append([nextIdx, nextIdx + len(substring)])
			# New starting index which is the next element of the start index of the found substring.
			startIdx = nextIdx + 1
		else:
			# We break because no more substring is present in the string from current start index onwards.
			break
	return locations


def collapse(locations):
	# Edge case
	if not locations:
		return locations
	# This is similar to merging overlapping intervals.
	newLocations = [locations[0]]
	for i in range(1, len(locations)):
		currLocation = locations[i]
		if currLocation[0] <= newLocations[-1][1]:
			newLocations[-1][1] = currLocation[1]
		else:
			newLocations.append(currLocation)
	# Now we will convert the 2D locations array to 1D array, so that we can access all the indices where
	# we will add underscore
	flattenLocation = []
	# Flatten the locations
	for loc in newLocations:
		flattenLocation += loc
	return flattenLocation


def underscorify(string, locations):
	# Storing the final result
	result = []
	# Starting location index to put the underscore
	locationIdx = 0
	# For each element in the string
	for i in range(len(string)):
		# If that index contains an underscore
		if locationIdx < len(locations) and i == locations[locationIdx]:
			# Add the underscore, and the move to the next location
			result.append('_')
			locationIdx += 1
		# Either way, we will always add the current letter to the result.
		result.append(string[i])
	# If we have finished the string but still have the locationsIdx, then we will add the underscore.
	if locationIdx < len(locations):
		result.append('_')
		locationIdx += 1
	# Final result string.
	return ''.join(result)
