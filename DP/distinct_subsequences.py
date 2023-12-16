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

"""


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
