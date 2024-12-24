"""
Write a function that takes in a string and returns its longest substring without duplicate characters.

string = "clementisacap",
Output: "mentisac"

https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Brute Force:
Generate every substring, and then check for the longest.
Time: O(n^3) and Space: O(m), m is the size of the character set

Optimized:
The key insight for optimization is that when we find a repeating character, we can jump our start pointer directly
to the position after its last occurrence, rather than checking all possible substrings.

Time: O(n) and Space: O(m), m is the size of the character set
"""


def longestSubstringWithoutDuplication(string):
    # Start, end pointers for the substring.
    start = 0
    end = 0
    # Store the longest substring result.
    longest = [0, 1]
    # Dictionary to store the last seen for the letters
    lastSeen = {}
    # We iterate to the end of the string.
    while end < len(string):
        # Getting the current letter.
        letter = string[end]
        # If the letter is already seen before
        if letter in lastSeen:
            # We update the start position of the substring.
            # We take max(current start position, last seen letters next position)
            start = max(start, lastSeen[letter] + 1)
        # We always update the last seen of every letter in the dictionary
        lastSeen[letter] = end
        # Updating the result with max substring length.
        longest = max(longest, [start, end], key=lambda x: x[1] - x[0])
        # Moving forward.
        end += 1

    return string[longest[0] : longest[1] + 1]
