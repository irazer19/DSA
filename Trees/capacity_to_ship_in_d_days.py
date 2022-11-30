"""
A conveyor belt has packages that must be shipped from one port to another within days days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the
conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped
within days days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
"""


def shipWithinDays(weights, days):
	# Time: O(log(sum(weights)) * w) and space: O(1)
	"""
	Logic:
	Since we have to find the least capacity of the ship, we can use a binary search because we know that
	the answer will lie between 1 to sum(all the weights).
	At every mid we compute, we will send it as the possible capacity into the function which we will compute
	whether it is possible to ship the items within d days within that capacity.
	If its possible, then we will further try to reduce the capacity by moving to the left and update the result.
	If not possible, then we will increase the capacity by moving to the right.
	"""
	# This is the max capacity we can have.
	total = sum(weights)
	# Binary search
	left = 1
	right = total
	# Result
	leastCapacity = total
	while left <= right:
		mid = (left + right) // 2
		# Checking whether it is possible to ship using "mid" capacity
		dayCount = canShip(weights, mid)
		# If its not possible, then we will move to the right
		if dayCount > days:
			left = mid + 1
		else:
			# Else, we will update the result and move to the left
			leastCapacity = min(leastCapacity, mid)
			right = mid - 1
	# Final result
	return leastCapacity


def canShip(weights, capacity):
	# Variable to count the number of days it takes to ship all the weights
	dayCount = 1
	# Current weight
	currWeight = 0
	# For each weight
	for w in weights:
		# If this weight + existing weight exceeds the capacity, then we will ship the items next day and update the
		# current weight with this weight alone.
		if currWeight + w > capacity:
			dayCount += 1
			currWeight = w
		else:
			# Else we will keep adding the weights
			currWeight += w
	# Returning the total days it took to ship the items.
	return dayCount


print(shipWithinDays(weights=[3, 2, 2, 4, 1, 4], days=3))
