"""
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.
You start your journey from building 0 and move to the next building by possibly using bricks or ladders.
While moving from building i to building i+1 (0-indexed),
If the current building's height is greater than or equal to the next building's height,
you do not need a ladder or bricks. If the current building's height is less than the next building's height, you can
either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
"""

from heapq import *
from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
	# Time: O(n*logn) and Space: O(n)
	"""
	Logic:
	We will get the height difference of current and next building, and if the diff > 0 then we can climb either using
	bricks or ladder, now we will push the diff in the heap and if the total heap elements is greater than the ladders
	then we know that we have to use bricks, so we keep popping the minimum diff from min heap and subtract from the
	heap. After this if the bricks have gone < 0, then we know that this is the max index we can reach and return i.
	"""
	# Min heap to store height difference
	heap = []
	for i in range(len(heights) - 1):
		# Height difference between next and current building
		diff = heights[i + 1] - heights[i]
		# If the next building is taller
		if diff > 0:
			# We will push this diff to the min heap
			heappush(heap, diff)
			# Now until total heap elements are more than the ladders available, we will have to use bricks only
			if len(heap) > ladders:
				# Remove the item and subtract from the available bricks
				curr = heappop(heap)
				bricks -= curr
			# At this point we know that the total elements in the heap will be either equal or smaller than the
			# ladders available to us, and if its equal then we will assume that we have used all those ladders.
			# Thus, if bricks < 0, it means that we wont be able to reach the next i + 1 building as we didnt have
			# sufficient number of bricks.
			if bricks < 0:
				return i
	# If we reach the end of the building.
	return len(heights) - 1
