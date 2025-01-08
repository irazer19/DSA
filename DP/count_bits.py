"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
1's in the binary representation of i.

https://leetcode.com/problems/counting-bits/description/
"""


def countBits(n):
    # Time = Space: O(n)
    """
    Logic:
    If we observe the pattern of first 10 elements, we will see that if current n is a power of 2, then one more
    extra bit is added + repetition of previous counts.
    By default, for n = 0, the result is 0.
    """
    # Every index is treated as n starting from 0, 1, 2, 3... n
    dp = [0 for _ in range(n + 1)]
    # Offset is the last power of 2 which we have encountered. Default is 2^0 which is 1.
    offset = 1
    # For each n starting from 0
    for i in range(1, n + 1):
        # Lets update the offset if the current i is the power of 2.
        if offset * 2 == i:
            offset *= 2
        # Current total 1's for i = 1 + current index - offset
        # Basically, the pattern repeats after the previous offset was found.
        dp[i] = 1 + dp[i - offset]
    return dp
