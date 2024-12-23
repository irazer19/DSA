"""
Write a function that takes in an array of integers and returns an array of length 2 representing the largest
range of integers contained in that array.

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
output: [0, 7] Where 0 is the smallest element & 7 is the largest element of the consecutive series.

Similar: https://leetcode.com/problems/longest-consecutive-sequence/description/
"""


def largestRange(array):
    """
    Brute Force:
    For each element, we check the left and the right to find its range, so it's like using two for-loops.
    Time: O(n^2) and Space:O(n)

    Optimized:
    Key-intuition: Only numbers that don't have a left neighbor (num-1) in the set can be the start of the longest sequence.
    This means if we see 4 and we know 3 exists in our set, we can skip checking sequences starting at 4.
    That's why the check if num - 1 not in nums is crucial - it ensures we only explore sequences from their true starting points,
    making the solution much more efficient than checking every number as a potential start.
    Time = Space = O(n)
    """

    if not array:
        return []

    # Create hash set for O(1) lookups
    nums = set(array)
    best_range = []
    longest_length = 0

    # Check each possible start of a sequence
    for num in array:
        # Only check numbers that could be start of a sequence
        # If num-1 exists, num can't be start of longest sequence
        if num - 1 not in nums:
            # Find consecutive chain
            current_num = num
            current_length = 1

            # Keep going until chain breaks
            while current_num + 1 in nums:
                current_num += 1
                current_length += 1

            # Update longest range if current is longer
            if current_length > longest_length:
                longest_length = current_length
                best_range = [num, current_num]

    return best_range
