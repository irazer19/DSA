"""
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i],
and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no
possible sequence of jumps that lands the bug on position x, return -1.

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1
"""


def minimumJumps(forbidden, a, b, x):
	# Time: O(2 * x) because for each position we have True/False flag.
	# Space: O(x), storing all the positions
	"""
	Logic:
	We will do BFS, lets start from 0th position where the last move was not backwards.
	After we pop the element, we can either move forward or backward, and we will try with both and append to the queue.
	After completing all the layers of the queue, we will update the result steps += 1.
	"""
	# Storing (current position, was the last move backwards?)
	q = [(0, False)]
	# Result
	steps = 0
	# Tracking all the visited nodes
	visited = set()
	# Forbidden states to set for fast access
	forbidden = set(forbidden)
	# BFS
	while q:
		# Going through all the layers of the queue
		for _ in range(len(q)):
			# Popping the left element
			currPos, isLastBackward = q.pop(0)
			# If the current position is the target, we return the result
			if currPos == x:
				return steps
			# Trying to move forward
			forwardPos = currPos + a
			# We cap the forward position to 6000, and it should not be in forbidden state and not visited.
			if forwardPos <= 6000 and forwardPos not in forbidden and (forwardPos, False) not in visited:
				# Add to the queue and visited set
				q.append((forwardPos, False))
				visited.add((forwardPos, False))
			# Going backward
			backwardPos = currPos - b
			# If the current element was a backward move, only then we try to move backward.
			if isLastBackward is False:
				# Because of the constraint we cannot go to negative numbers, and it should not be in visted and
				# forbidden states
				if backwardPos >= 0 and backwardPos not in forbidden and (backwardPos, True) not in visited:
					q.append((backwardPos, True))
					visited.add((backwardPos, True))
		# Updating the steps after completing the layer
		steps += 1

	return -1
