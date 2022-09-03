"""
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.
You can assume that you can always reach the last index.

"""


def minNumberOfJumps(array):
    # Time: O(n) and Space: O(1)
    # If the array is empty or contains single element then return 0.
    if len(array) in [0, 1]:
        return 0

    # We maintain two variables, curr_steps = tracks the current number of steps left until it becomes 0.
    # total_steps_left = the total number of steps left with which we can continue if curr_steps becomes 0.
    curr_steps = array[0]
    total_steps_left = array[0]
    jumps = 1  # Since we are at the start index, the next move will mean a jump.

    # At each index starting from 1. We dont enter the last index because that's where we have to reach.
    for i in range(1, len(array) - 1):
        # For the curr index, we reduce the curr_steps and total_steps_left.
        # Then we check whether we can get more steps at the current index. If yes, then we update the
        # total_steps_left with the current element.
        curr_steps -= 1
        total_steps_left -= 1
        total_steps_left = max(total_steps_left, array[i])

        # If the curr_steps has become 0, this means we need to make a jump.
        # And then we assign the curr_steps = total_steps_left to keep moving forward.
        if curr_steps == 0:
            curr_steps = total_steps_left
            jumps += 1
    # Result
    return jumps


print(minNumberOfJumps([2, 3, 1, 1, 4]))
