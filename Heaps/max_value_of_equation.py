"""
You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where
points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.
Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get
3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
"""


def findMaxValueOfEquation(points, k: int):
	# Time: O(nlogn) and Space: O(n)
	"""
	Logic:
	Since we know that xi < xj, so the equation can be written as (yi - xi) + (xj + yj).
	We want to maximize this equation, so essentially we as we traverse, we will assume its the right hand side
	value of the equation (xj + yj), and then we will also have a max heap which will store the max previous value
	of (yi - xi).
	So we compare the top value of the heap with the current element, if the constraint |xi - xj| <= 1 satisfies
	then we will update the result and then push this new element into the heap.
	"""
	import heapq
	# Heap
	heap = []
	# Result
	result = float('-inf')

	# As we move, each point is assumed as jth item
	for xj, yj in points:
		# If heap is empty, then we simply append the key as the left hand side of the equation and also x value
		# so that we can compare the constraint later.
		if not heap:
			heapq.heappush(heap, (-(yj - xj), xj))
		else:
			# Else, until the constraint is not satisfied with the top value, then we simply pop that item from heap.
			while heap and abs(heap[0][1] - xj) > k:
				heapq.heappop(heap)
			# If we still have elements in heap, then we update the result
			if heap:
				result = max(result, xj + yj + (-heap[0][0]))
			# We push the current element to the heap.
			heapq.heappush(heap, (-(yj - xj), xj))
	return result
