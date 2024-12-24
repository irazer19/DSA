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

https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

Brute Force:
The brute force approach would be to try every possible combination of taking k cards from either the beginning or end.
We use backtracking, and at every recursion, we try the left card then the right card, and return the max of either.
Time Complexity: O(2^k) since for each of the k choices, we have 2 options: Either left card of right card.
Space Complexity: O(k) for the recursion stack.

Optimized:
Instead of thinking about "taking k cards from either end", we can reframe the problem as:
"Find the subarray of length (n-k) with the minimum sum, where n is the total number of cards"
Why? Because:

- You're taking k cards in total
- Whatever k cards you take, the remaining (n-k) cards must be consecutive (in the middle)
- So if you want to maximize the sum of k cards you take, you want to minimize the sum of cards you don't take!

Time: O(n-k) and Space: O(1)

"""


def maxScore(cardPoints, k):
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
    currSum = sum(cardPoints[: endWindow + 1])
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
