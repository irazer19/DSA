"""
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not
exist a stone. The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by
landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in
the forward direction.

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone,
then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
"""


def canCross(stones):
	# Time = Space = O(n)
	"""
	Logic:
	We'll use BFS starting from store 0 with last jump also as 0, we will store (stone, jump taken) in the queue.
	So from every stone, we will take jump-1, jump, jump+1 to reach the next stone.
	We will also track the visited stones from a given jump.
	If we pop a stone which equals the last stone then we return True

	"""
	# For faster access of the stones
	table = {i: True for i in stones}
	# Tracking the visited stones from a jump
	visited = set()
	# Queue, (current stone we are at, jump it took to reach the current stone)
	q = [(0, 0)]
	visited.add((0, 0))

	# BFS
	while q:
		# Getting the left element
		stone, jump = q.pop(0)
		# Base case
		if stone == stones[-1]:
			return True
		# Making k-1, k, k+1 jumps from the current stone
		for j in [jump - 1, jump, jump + 1]:
			# We dont want to end up to the same stone, so jump should be > 0
			if j > 0:
				# Value of the next stone
				nextStone = stone + j
				# If the next stone is present and is not visited from the jump j
				if table.get(nextStone, False) and (nextStone, j) not in visited:
					# Adding to the queue
					q.append((nextStone, j))
					# Mark it as visited
					visited.add((nextStone, j))
	return False
