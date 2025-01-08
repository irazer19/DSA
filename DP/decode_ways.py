"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the
mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

https://leetcode.com/problems/decode-ways/
"""


def numDecodingsBruteForce(s: str) -> int:
    """
    Brute Force (Recursive):
    Uses recursion to try all possible decodings
    For each position, it tries to decode either 1 or 2 digits
    Time Complexity: O(2ⁿ) - exponential, as it explores all possibilities
    Space Complexity: O(n) due to recursion stack
    """

    def decode(index: int) -> int:
        # Base cases
        if index == len(s):  # Reached end of string
            return 1

        if s[index] == "0":  # Invalid leading zero
            return 0

        # Try single digit
        ways = decode(index + 1)

        # Try two digits if possible
        if index + 1 < len(s):
            value = int(s[index : index + 2])
            if value <= 26:
                ways += decode(index + 2)

        return ways

    return decode(0)


def numDecodingsDP(s: str) -> int:
    """
    We use an array dp[] where dp[i] represents the number of ways to decode the string up to position i. At each position:
        If current digit isn't '0', add dp[i-1] (ways using 1 digit)
        If last two digits form 10-26, add dp[i-2] (ways using 2 digits)
        dp[i] will be sum of both possibilities

    Uses a bottom-up approach with tabulation
    Stores intermediate results in a DP array
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not s or s[0] == "0":
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Empty string
    dp[1] = 1  # First character

    for i in range(2, n + 1):
        # Check if single digit decode is possible
        if s[i - 1] != "0":
            dp[i] += dp[i - 1]

        # Check if two-digit decode is possible
        two_digit = int(s[i - 2 : i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]

    return dp[n]
