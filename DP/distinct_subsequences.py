"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.
The test cases are generated so that the answer fits on a 32-bit signed integer.


Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

https://leetcode.com/problems/distinct-subsequences/
"""


# Brute force
def numDistinct_brute(s: str, t: str) -> int:
    """Brute Force Solution (Time: O(2^n), Space: O(n) for recursion stack)

    Uses recursive backtracking to try all possible combinations
    At each position in string s, we have two choices:

    If current characters match, we can include it in our subsequence
    We can always skip the current character

    Base cases:
    If we've matched all characters in t, we've found a valid subsequence
    If we've exhausted s without matching t, we return 0"""

    def backtrack(s_idx: int, t_idx: int) -> int:
        # Base cases
        if t_idx == len(t):  # Found a valid subsequence
            return 1
        if s_idx == len(s):  # Reached end of s without finding subsequence
            return 0

        count = 0
        # If current characters match, we have two choices:
        # 1. Include current character
        # 2. Skip current character
        if s[s_idx] == t[t_idx]:
            count += backtrack(s_idx + 1, t_idx + 1)  # Include current char

        # Always try skipping current character in s
        count += backtrack(s_idx + 1, t_idx)

        return count

    return backtrack(0, 0)


def num_distinct(s: str, t: str) -> int:
    # Time = Space = O(s x t)
    """
    If char at s == t, then the total subsequence = total subsequence by adding this char of s + total
    subsequence by not adding this char of s. (store[i - 1][j - 1] + store[i][j - 1])
    If char at s != t, then the total subsequence = total subsequence by not adding this char of s (store[i][j - 1])
    """
    # Creating dp array
    store = [[0 for _ in range(len(s) + 1)] for _ in range(len(t) + 1)]

    # String s always has one subsequence of t which is an empty string ""
    for i in range(len(store[0])):
        store[0][i] = 1

    for i in range(1, len(store)):
        for j in range(1, len(store[0])):
            if t[i - 1] == s[j - 1]:
                # Adding char at s + Not adding char at s
                store[i][j] = store[i - 1][j - 1] + store[i][j - 1]
            else:
                # Not adding char at s
                store[i][j] = store[i][j - 1]

    return store[-1][-1]
