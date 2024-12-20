"""
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.

https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/description/

"""


def has_all_codes(s: str, k: int) -> bool:
    """
    Brute Force:
    1. First, generate all possible binary codes of length k
    2. For each binary code, check if it exists as a substring in s
    Time = Space = O(2^k)

    Optimized:
    Since we know that the total binary codes which can be generated of length k is 2^k, we will find every unique substring
    and add in a result set.
    If the total length of the result list = 2^k, we return True else False
    Time = O(n^2) and Space: O(2^k)
    """
    # Early termination if string is too short
    if len(s) < k:
        return False

    # Use a set to store all unique substrings of length k
    seen = set()

    # Slide through the string
    for i in range(len(s) - k + 1):
        seen.add(s[i : i + k])

    # If we found all possible combinations,
    # the set size should be 2^k
    return len(seen) == 2**k
