"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses constant extra space.

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

https://leetcode.com/problems/first-missing-positive/description/
"""


def firstMissingPositive(nums):
    """
    Brute Force Approach:
    Store the nums in a dictionary for easy lookup. Now loop over the ideal values that should have been in the array
    starting from 1. Ex: [1, 2, 3, 4], and check which is the first value that is not present in the dictionary, and
    return it.
    Time: O(n) and Space: O(n)

    Optimized Approach:
    1. Iterate the array, and convert all the -ves to 0.
    2. Iterate the array, and at every ith index, get the val, and then at index (val - 1) convert it to negative to
    mark that val is present in the array.
    3. Now we know that if the array length is 4, then ideally we should have the elements [1, 2, 3, 4], so the
    smallest element is 5, which means that the maximum value of the smallest element = len(nums) + 1.
    Using this logic, we will iterate through the [1, len(nums) + 1], and if we find an element whose (val - 1) index
    values is >= 0, then we return it as the result.
    Time: O(n) and Space: O(1)
    """
    # Convert all the default -ves to 0.
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    # Now here we mark all the found elements if they are within the array range.
    for i in range(len(nums)):
        # Getting the index at which we will mark
        val = abs(nums[i]) - 1
        # If the index is within the bounds
        if 0 <= val < len(nums):
            # If the value at this index is positive, then we mark by making it negative.
            if nums[val] > 0:
                nums[val] *= -1
            # Else if the value is 0, then we will simply add a negative value which is out of bounds.
            elif nums[val] == 0:
                nums[val] = -1 * (len(nums) + 1)
    # Now we iterate through all the possible values [1, len(nums) + 1], where len(nums) + 1 is the max smallest
    # value we can have.
    for n in range(1, len(nums) + 1):
        # We check the value at the n-1 index, if its >=0 then we return n because its not marked as negative.
        if nums[n - 1] >= 0:
            return n
    # By default, we will return this.
    return len(nums) + 1
