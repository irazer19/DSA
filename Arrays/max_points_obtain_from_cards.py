"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will
maximize your total score. The optimal strategy is to take the three cards on the right,
giving a final score of 1 + 6 + 5 = 12.

"""


def maxScore(cardPoints, k):
	# Time: O(n) and Space: O(1)
	"""
	Logic:
	Since we want cards consecutively from either the start or end of the array, we will use sliding window approach.
	The elements in the window will be the smallest such that the total - window elements = largest score.
	So we will slide over and whichever window gives the largest score by (total - sum(window)), we will return that
	score.
	"""
	# If we have to remove all the cards, then we simply return the sum of all.
	if k == len(cardPoints):
		return sum(cardPoints)
	# Total sum
	total = sum(cardPoints)
	# Start of the window
	startWindow = 0
	# End of the window
	endWindow = len(cardPoints) - k - 1
	# Curr window sum
	currSum = sum(cardPoints[:endWindow + 1])
	# Result
	result = total - currSum
	# Incrementing the endWindow so that we can add it to the sum
	endWindow += 1
	while endWindow < len(cardPoints):
		# Removing the current startWindow
		currSum -= cardPoints[startWindow]
		# Adding the new endWindow
		currSum += cardPoints[endWindow]
		# Updating the result
		result = max(result, total - currSum)
		# Moving the start and end window.
		startWindow += 1
		endWindow += 1
	
	return result
