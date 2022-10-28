"""
Generate all the valid IP's from the given string.
input = "1921680"

expected = [
    "1.9.216.80",
    "1.92.16.80",
    "1.92.168.0",
    "19.2.16.80",
    "19.2.168.0",
    "19.21.6.80",
    "19.21.68.0",
    "19.216.8.0",
    "192.1.6.80",
    "192.1.68.0",
    "192.16.8.0",
]
"""


def validIPAddresses(string):
	# Time = Space = O(1)
	"""
	Logic:
	Every IP has 4 parts, so we will compute all the parts in steps.
	We will validate every part by checking the range between 0 and 255, and also ignore all the leading 0 numbers.
	If all the parts are valid, then we will add it to the result.
	"""
	# Stores the result
	result = []
	# For the first part, we will need at least 4 characters of the string.
	for i in range(min(len(string), 4)):
		# Getting the first part.
		firstPart = string[: i + 1]
		# Validating the first part
		if isValid(firstPart):
			# We will start the second part from i + 1, we will skip last two elements for the third and fourth parts
			for j in range(i + 1, len(string) - 2):
				# Getting the second part.
				secondPart = string[i + 1: j + 1]
				# if the second part is valid.
				if isValid(secondPart):
					# We will loop from j + 1 for the third and fourth part, we will skip the last element for
					# the fourth part.
					for k in range(j + 1, len(string) - 1):
						# Getting the third and the fourth part.
						thirdPart = string[j + 1: k + 1]
						fourthPart = string[k + 1:]
						# If both are valid
						if isValid(thirdPart) and isValid(fourthPart):
							# Adding the result in a string format.
							result.append('.'.join([firstPart, secondPart, thirdPart, fourthPart]))
	return result


def isValid(part):
	# If the part is within the range 0 and 255
	if 0 <= int(part) <= 255:
		# If there is no leading zero in the part.
		return len(part) == len(str(int(part)))
	return False
