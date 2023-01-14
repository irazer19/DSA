"""
You're given two strings stringOne and stringTwo. Write a function that determines if these two strings can be made
equal using only one edit.
Operations allowed: Replace, Add, Remove.

stringOne = 'hello'
stringTwo = 'hollo'

output: True
"""


def oneEdit(stringOne, stringTwo):
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	We will iterate over the both the strings using pointers. If the chars dont match then we have 3 cases:
	1. if the length of stringone > string2, then we can either remove from stringone or add this char to stringtwo.
	2. Similarly if the length of stringtwo > stringone, we do the above operation.
	3. If the length of stringone == stringtwo, then we will swap the non-matching character with the matching character

	Now if the stringone == stringtwo, then we will simply move to the next characters.
	"""
	# Edge case
	if abs(len(stringOne) - len(stringTwo)) > 1:
		return False

	idxOne = 0
	idxTwo = 0
	# Since we are allowed to make only 1 edit, we will use a boolean to store it.
	madeEdit = False

	while idxOne < len(stringOne) and idxTwo < len(stringTwo):
		# If the current chars dont match in the string.
		if stringOne[idxOne] != stringTwo[idxTwo]:
			# IF we have already made the edit, retutn false
			if madeEdit:
				return False
			# Else we will make the edit
			madeEdit = True
			# Whether length of stringOne >  stringTwo or vice-versa, we will can either remove or add
			if len(stringOne) > len(stringTwo):
				idxOne += 1
			elif len(stringOne) < len(stringTwo):
				idxTwo += 1
			else:
				# Else if the length if same, then we will swap, and move to the next char.
				idxOne += 1
				idxTwo += 1
		else:
			# Case where the chars are matching, then we will move to the next char for both the strings.
			idxOne += 1
			idxTwo += 1

	return True
