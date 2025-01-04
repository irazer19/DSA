"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has
unique characters.
Return the maximum possible length of s.
A subsequence is an array that can be derived from another array by deleting some or no elements without changing the
order of the remaining elements.

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/

Uses recursion with backtracking
For each string in the array, we have two choices:

Include it in our concatenation
Skip it and move to the next string

Time Complexity: O(2^n), where n is the length of input array
Space Complexity: O(n) for the recursion stack

"""


def max_length(arr):
    def is_valid(s):
        # Check if string has all unique characters
        return len(s) == len(set(s))

    def backtrack(index, current):
        if index == len(arr):
            # If current combination is valid, return its length
            return len(current) if is_valid(current) else 0

        # Don't include current string
        length1 = backtrack(index + 1, current)

        # Include current string
        length2 = backtrack(index + 1, current + arr[index])

        return max(length1, length2)

    return backtrack(0, "")
