"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other
uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

https://leetcode.com/problems/longest-repeating-character-replacement/description/

Brute Force:
The key idea would be to try every possible substring and check if it can be made valid with k changes.
Time: O(n^3): n^2 to generate all the substrings, and n to check.
Space: O(1)

Optimized:
The key insight is that we don't need to actually perform the character replacements - we just need to know if
they're possible within our k limit. This is done by tracking the most frequent character in our current window.
Time: O(n): because the right pointer moves n times, and the left pointer at max moves n times = O(2n) = O(n)
and Space: O(1)
"""


def characterReplacement(s, k):
    # Initialize character count dictionary
    count = {}
    max_length = 0
    max_count = 0  # Count of most frequent character in current window
    left = 0

    # Iterate through the string with right pointer
    for right in range(len(s)):
        # Add new character to count
        count[s[right]] = count.get(s[right], 0) + 1
        # Update max_count for current window
        max_count = max(max_count, count[s[right]])

        # Current window size - count of most frequent char = chars to change
        # If this is greater than k, shrink window
        while (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
