"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following
operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1
and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

https://leetcode.com/problems/delete-and-earn/description/

"""
from collections import Counter


def deleteAndEarnBruteForce(nums):
    """
    Brute Force Solution using recursion
    For each number, we:
                Calculate points by multiplying the number with its frequency
                Remove the current number and its adjacent numbers (num-1 and num+1)
                Recursively calculate points for remaining numbers
                Keep track of maximum points possible
    Time Complexity: O(2^n) where n is the length of nums, because each number has two choices, take it or leave it.
    Space Complexity: O(n) due to recursion stack
    """

    def recursiveEarn(numbers: Counter) -> int:
        if not numbers:  # Base case: no numbers left
            return 0

        max_points = 0
        # Try each unique number
        for num in numbers.keys():
            # Calculate points for current number
            points = num * numbers[num]

            # Create new counter without num-1, num, num+1
            next_numbers = Counter(numbers)
            del next_numbers[num]
            if num - 1 in next_numbers:
                del next_numbers[num - 1]
            if num + 1 in next_numbers:
                del next_numbers[num + 1]

            # Recursive call for remaining numbers
            points += recursiveEarn(next_numbers)
            max_points = max(max_points, points)

        return max_points

    return recursiveEarn(Counter(nums))


def deleteAndEarnOptimized(nums) -> int:
    """
    Optimized Solution using dynamic programming
    Converts the problem into a form similar to House Robber problem
    Key insights:

    We can group same numbers together (using Counter)
    For each number i, we have two choices:

    Take number i: Get points from i and skip i-1
    Skip number i: Keep points from i-1

    Uses dynamic programming array where dp[i] represents max points up to number i
    Time Complexity: O(n + k) where k is the range of numbers
    Space Complexity: O(k)

        Time Complexity: O(n + k) where n is length of nums and k is range of nums
        Space Complexity: O(k) where k is range of nums
    """
    if not nums:
        return 0

    # Count frequency of each number
    count = Counter(nums)
    max_num = max(nums)

    # dp[i] represents max points that can be earned up to number i
    dp = [0] * (max_num + 1)

    # Base cases
    dp[0] = 0
    dp[1] = count[1] * 1 if 1 in count else 0

    # For each number, we can either:
    # 1. Take current number (skip previous) -> dp[i-2] + current_points
    # 2. Skip current number -> dp[i-1]
    for i in range(2, max_num + 1):
        current_points = count[i] * i
        dp[i] = max(dp[i - 1], dp[i - 2] + current_points)

    return dp[max_num]
