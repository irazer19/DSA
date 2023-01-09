"""
You are given an array of strings equations that represent relationships between variables where each string
equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase
letters (not necessarily different) that represent one-letter variable names.
Return true if it is possible to assign integers to variable names so as to satisfy all the given equations,
or false otherwise.

["c==c","f!=a","f==b","b==c"]

true
"""


def equationsPossible(equations):
	# Time: O(n^2) and Space: O(n)
	"""
	Logic:
	First we will create a set to store all the letters which have == sign, and then we will do BFS
	for each equation which has != sign, and check whether we can reach letter2 from letter1, if yes then we return
	False, else continue to the next equation which has !=.

	The logic is that once we have all the sets where letters are equal to each other, then for != equations those
	letters should still satisfy the condition.
	"""
	# To store all the sets where the letters are ==
	store = {}
	# We will only gof or == equations
	for e in equations:
		letter1, letter2, op = e[0], e[3], e[1]
		if op == '=':
			# Initializing set for every unique == letters and adding the letter to it.
			if letter1 not in store:
				store[letter1] = set(letter1)
			if letter2 not in store:
				store[letter2] = set(letter2)
			store[letter1].add(letter2)
			store[letter2].add(letter1)

	# Now for each != equation
	for e in equations:
		letter1, letter2, op = e[0], e[3], e[1]
		if op == '!':
			# if both the letters are equal then just return False
			if letter1 == letter2:
				return False
			# BFS from letter 1
			q = [letter1]
			visited = set()
			while q:
				curr = q.pop(0)
				visited.add(curr)
				# If we are able to reach letter2 from letter1 then we return False because the current operator says
				# that they should not be equal.
				if curr == letter2:
					return False
				# Adding child nodes/letters which are a part of the current letters set.
				for nextLetter in store.get(curr, []):
					if nextLetter not in visited:
						q.append(nextLetter)

	return True
