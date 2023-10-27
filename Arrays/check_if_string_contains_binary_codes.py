"""
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indices 0, 1, 3 and 2 respectively.
"""


def has_all_codes(s: str, k: int) -> bool:
    # Time = O(n^2) and Space: O(2^k)
    """
    Since we know that the total binary codes which can be generated of length k = 2^k, we will find every unique substring
    and add in a result list.
    If the total length of the result list = 2^k, we return True else False
    """
    required = 2**k
    # To track substring which has already been added in the result list
    seen = set()
    result = []
    # For every substring of length k
    for i in range(len(s) - k + 1):
        substring = s[i : i + k]
        if substring not in seen:
            result.append(substring)
            seen.add(substring)

    return len(result) == required
