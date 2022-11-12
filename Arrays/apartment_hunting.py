"""
Similar: Minimum Window substring in Leetcode.
You're looking to move into a new apartment on specific street, and you're given a list of contiguous blocks on that
street where each block contains an apartment that you could move into.
You also have a list of requirements: a list of buildings that are important to you. For instance, you might value
having a school and a gym near your apartment. The list of blocks that you have contains information at every block
about all of the buildings that are present and absent at the block in question. For instance, for every block,
you might know whether a school, a pool, an office, and a gym are present.
In order to optimize your life, you want to pick an apartment block such that you minimize the farthest distance you'd
have to walk from your apartment to reach any of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings
and that returns the location (the index) of the block that's most optimal for you.
If there are multiple most optimal blocks, your function can return the index of any one of them.

blocks = [
    {"gym": False, "school": True, "store": False},
    {"gym": True, "school": False, "store": False},
    {"gym": True, "school": True, "store": False},
    {"gym": False, "school": True, "store": False},
    {"gym": False, "school": True, "store": True},
]
reqs = ["gym", "school", "store"]

Output: 3
"""


def apartmentHunting(blocks, reqs):
	# Time = Space = O(br), where b = no of blocks and r is the no of requirements.
	"""
	Logic:
	So we want to find the apartment which has all the required amenities at the nearest distance.
	First we will iterate from left to right, and update the distance of the amenities by comparing it with the
	previous amenities which is at distance 1.
	Then we will iterate from right to left, and update the distance of the amenities by comparing it with the
	immediate next amenity which is at distance 1.

	Now, for each block, we will check the maximum distance needed to reach the required amenities.
	We compare this max distance among all the blocks, and the block which has the minimum of all is the best
	apartment for us.
	"""
	# Initializing the minBlocks to store the distances.
	minBlocks = [{} for _ in blocks]
	# Used for storing the smallest distance of a block from the required amenities.
	smallestDist = float('inf')
	# Result
	bestApartment = None
	# Iterating from Left to right
	for i in range(len(blocks)):
		# Initializing the obj to store the required amenities distance
		currObj = {}
		# We will loop through all the amenities of this block
		# Here are only creating a distance object for the current block.
		for currReq in blocks[i]:
			# Only if the amenity is present, and this amenity is also present in the requirement.
			# Its distance is 0 from the current block
			if blocks[i][currReq] and currReq in reqs:
				currObj[currReq] = 0
			else:
				# Else, its distance is inf by default
				currObj[currReq] = float('inf')
		# Main iteration starts from here.
		# If its the first block, then we cannot compare it with the previous block, so we just store
		# the distance obj
		if i == 0:
			minBlocks[i] = currObj
			continue
		else:
			# Else, we loop over all the amenities of the previous block.
			# Either the current distance is less, or the previous blocks distance + 1
			for req, prevDist in minBlocks[i - 1].items():
				currObj[req] = min(currObj[req], 1 + prevDist)
		# Storing the update distance obj.
		minBlocks[i] = currObj
	####################################################################################
	# Now we iterate from Right to left.
	# We compare the curr block with its next right block, that is why we start from the 2nd last block.
	for i in range(len(blocks) - 2, -1, -1):
		# We will need this variable to track the max distance needed for a block to reach out the amenities
		currBlockMax = float('-inf')
		# We loop over all the amenities of the next right block.
		for req, nextDist in minBlocks[i + 1].items():
			# If the current amenities distance is infinity for the next right block, then we skip it.
			if nextDist != float('inf'):
				# Even here, we want to minimize the distance of the amenities from the current block.
				minBlocks[i][req] = min(minBlocks[i][req], nextDist + 1)
				# Now we update the currBlockMax, which will hold the max distance needed to reach the required
				# amenity
				currBlockMax = max(currBlockMax, minBlocks[i][req])
		# Here, to find the best apartment, we want to minimize the max distance needed to reach the required amenity
		if currBlockMax < smallestDist:
			# Update the smallest distance found so far to the amenities
			smallestDist = currBlockMax
			# Update the current apartment index
			bestApartment = i
	return bestApartment
