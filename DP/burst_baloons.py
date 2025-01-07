"""
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array
nums. You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of
bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

https://leetcode.com/problems/burst-balloons/description/


"""


def brute_force(nums):
    """
    Brute Force Solution (Recursive):
    The idea is to try bursting each balloon and recursively solve for the remaining balloons
    For each balloon we burst:

    Calculate coins as: left * current * right (where left/right are 1 if out of bounds)
    Recursively solve for remaining balloons
    Track maximum coins possible

    Time Complexity: O(n!) as we try all possible permutations
    Space Complexity: O(n) for recursion stack
    """

    def solve(balloons):
        if not balloons:
            return 0

        max_coins = 0
        for i in range(len(balloons)):
            # Get left and right values (1 if out of bounds)
            left = balloons[i - 1] if i > 0 else 1
            right = balloons[i + 1] if i < len(balloons) - 1 else 1

            # Current coins from bursting balloon i
            coins = left * balloons[i] * right

            # Recursively solve for remaining balloons
            remaining = balloons[:i] + balloons[i + 1 :]
            max_coins = max(max_coins, coins + solve(remaining))

        return max_coins

    return solve(nums)


def maxCoins(nums):
    # Time: O(n^3) and Space: O(n^2)
    # For given n, the total number of subarrays which can be formed is n^2, and we are using for loop to iterate
    # at every call, so another n is added making the time complexity O(n^3)
    """
    Logic:
    What if we pop an element the last? Then the total coins which we can get = whatever is before the left boundary
    * current coin * whatever is there after the right boundary.
    Plus we also have the added the coins which we got from the left subarray and the right subarray which we can
    find using recursion. We will also store the result for every subarray (left, right) into the cache.
    """
    # We pad an extra one at both the sides so that we can compute the coins for the first and the last baloons.
    nums = [1] + nums + [1]
    cache = {}
    # Starting the call from the range where we have baloons.
    return dfs(nums, 1, len(nums) - 2, cache)


def dfs(nums, left, right, cache):
    # Base case for recursion
    if left > right:
        return 0
    # Returning cache coins if any
    if (left, right) in cache:
        return cache[(left, right)]
    # We compute the coins for the given range of left and right index
    cache[(left, right)] = 0
    # We will try with all the baloons starting from left to right, and assume that the current baloon is getting
    # popped in the last.
    for i in range(left, right + 1):
        # Compute the total coins if this baloon was popped at the last.
        coins = nums[left - 1] * nums[i] * nums[right + 1]
        # Now we will add the coins from the left and right subarray (sub problems)
        coins += dfs(nums, left, i - 1, cache) + dfs(nums, i + 1, right, cache)
        # Updating the cache for the current [left and right] range
        cache[(left, right)] = max(cache[(left, right)], coins)
    # Returning the total coins for the current [left and right] range
    return cache[(left, right)]
