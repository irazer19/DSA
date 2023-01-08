"""
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the
largest possible number of stones that can be removed.

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
"""


def removeStones(stones) -> int:
	# Time = Space = O(n)
	"""
	Logic:
	We will create two graphs, one to store x coordinates stones and another to store y coordinates stones.
	Ex: For x = 0, we can have stone [0,0] and [0,1]
	Then we do BFS from each stone. We also track all the visited stones, and while popping the stone in BFS, we will
	increment the currLargest result which is the total number of stones visited(connected).
	After the BFS is over, the total number of stones which we can remove = currLargest - 1 because we can remove all
	except 1 stone.
	We keep adding the currLargest result to the final result from every stone we start the BFS from.
	"""
	# Creating graphs to store all the stones that share the same x coordinate
	xTable = {}
	# Creating graph to store all the stones that share the same y coordinate
	yTable = {}
	for coord in stones:
		x, y = coord
		coord = tuple(coord)
		if x not in xTable:
			xTable[x] = []
		if y not in yTable:
			yTable[y] = []

		xTable[x].append(coord)
		yTable[y].append(coord)

	# Tracking the visited stones
	visited = set()
	# Final result
	largest = 0
	# For each coordinate we will do BFS
	for coord in stones:
		coord = tuple(coord)
		# If the stone is unvisited
		if coord not in visited:
			q = [coord]
			# Result from the current stone
			currLargest = 0
			visited.add(coord)
			while q:
				x, y = q.pop(0)
				# Incrementing the result as we process the stones
				currLargest += 1
				# Collect its children
				# X children
				for xChild in xTable[x]:
					if xChild not in visited:
						visited.add(xChild)
						q.append(xChild)
				# Y children
				for yChild in yTable[y]:
					if yChild not in visited:
						visited.add(yChild)
						q.append(yChild)
			# We will update the final result.
			# We can remove all stones except 1 stone from the current result
			largest += currLargest - 1

	return largest
