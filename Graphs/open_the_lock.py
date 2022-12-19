"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can
turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock
will stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of
turns required to open the lock, or -1 if it is impossible.

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

"""


def openLock(deadends, target):
	# Time: O()
	"""
	Logic:
	Starting from 0000, we will generate all possible children by increasing and decreasing by 1 for each digit.
	We will do BFS, and then add the children to the queue along with their updated distance/turn if its not visited.
	If a node == target, then we return its distance/turn.
	"""

	# Edge case.
	if target in deadends or '0000' in deadends:
		return -1
	# Tracking visited nodes.
	visited = set(deadends)
	# Starting from 0000, its distance/turn is 0
	q = [('0000', 0)]
	# BFS
	while q:
		# Getting the leftmost node
		lock, turn = q.pop(0)
		# If this lock == target, then we return its turn
		if lock == target:
			return turn
		# For each child which we generated.
		for child in getChildren(lock):
			# If the child is unvisited
			if child not in visited:
				# Mark as visited
				visited.add(child)
				# Add to queue with updated distance
				q.append((child, turn + 1))
	return -1


def getChildren(lock):
	# Gets all the children from the given lock
	children = []
	# Going over all 4 digits of the lock
	for i in range(4):
		# Adding + 1 to this digit
		children.append(lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i + 1:])
		# Subtracting -1 from this digit.
		# We use % 10 because of overflow of the digits, ex: (9 + 1) % 10 = 0
		children.append(lock[:i] + str((((int(lock[i]) - 1) + 10) % 10)) + lock[i + 1:])
	return children
