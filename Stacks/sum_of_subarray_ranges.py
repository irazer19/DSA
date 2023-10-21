"""
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
Return the sum of all subarray ranges of nums.
A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.

"""


def sum_of_subarray_ranges(nums):
    """
    Logic:
    Concept: If there are L number of elements to the left of an element, and R number of elements to the right of
    that element, then the total number of subarrays which can be formed = (L + 1) * (R + 1)

    Now, since we have to find the max - min for each subarray and sum them to get the result, instead of computing
    the max - min for each subarray (brute force), we will compute the sum of all Max elements and sum of all Min
    elements in the subarrays, and then do the subtraction to get the answer.
    To get all the max elements of a subarray, consider each element as a max value, and use the above concept.
    Similarly do it to get the min elements from all the subarray.
    """

    # Find min elements first
    # We consider each element as a minimum of its subarray
    # First we find all the left elements which are greater than this element
    left_min = [0 for _ in nums]
    stack = [0]  # There are no elements to the left for the first index
    for i in range(1, len(nums)):
        # While we have elements to the left which are greater than the current element
        while stack and nums[stack[-1]] >= nums[i]:
            # we pop that element
            idx = stack.pop()
            # Update the total element count for this index meaning, total elements which are greater than index i
            # which are left to it.
            left_min[i] += (
                1 + left_min[idx]
            )  # We also add the result computed for that idx element
        stack.append(i)  # Now add this ith element to the stack and move on..

    # Repeat the same thing to find the total elements which are greater than an element i which are to the right
    # of the element i
    right_min = [0 for _ in nums]
    stack = [len(nums) - 1]  # Since the last element has nothing to the right
    for i in range(len(nums) - 2, -1, -1):
        while stack and nums[stack[-1]] > nums[i]:
            idx = stack.pop()
            right_min[i] += 1 + right_min[idx]
        stack.append(i)

    # Now we compute the total number of arrays formed and so compute the total min sum
    total_min_sum = 0
    for i in range(len(left_min)):
        # If there are 5 arrays where the element 2 is minimum, then sum = 2 * 5 = 10, this is what we are doing below.
        total_subarrays = (left_min[i] + 1) * (right_min[i] + 1)
        total_min_sum += nums[i] * total_subarrays

    # Now the do the exact same thing but this time find the Max of all the subarrays and compute the sum
    left_max = [0 for _ in nums]
    stack = [0]
    for i in range(1, len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            idx = stack.pop()
            left_max[i] += 1 + left_max[idx]
        stack.append(i)

    right_max = [0 for _ in nums]
    stack = [len(nums) - 1]
    for i in range(len(nums) - 2, -1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            idx = stack.pop()
            right_max[i] += 1 + right_max[idx]
        stack.append(i)

    total_max_sum = 0
    for i in range(len(left_max)):
        total_subarrays = (left_max[i] + 1) * (right_max[i] + 1)
        total_max_sum += nums[i] * total_subarrays

    # Finally, we take the difference of the:
    # [sum of all the max elements of subarrays] - [sum of all the min elements of subarrays]
    return total_max_sum - total_min_sum


print(sum_of_subarray_ranges([1, 3, 3]))
