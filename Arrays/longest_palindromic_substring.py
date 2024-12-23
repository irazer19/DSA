"""
Write a function that, given a string, returns its longest palindromic substring.
string= "abaxyzzyxf"
Output: "xyzzyx"

https://leetcode.com/problems/longest-palindromic-substring/description/
"""


def longestPalindromicSubstring(string):
    """
    Brute force:
    Use two for-loops to get every substring, and for each substring, check if it is a palindrome.
    Time: O(n^3) [Because of two for-loops and another for palindrome check] and Space: O(1)

    Optimized:
    For every letter we iterate, we will explore whether we can form a palindrome with it.
    From every letter at index i, we can either have an odd length palindrome which can start from i-1, i+1,
    or even length palindrome, which can start from i-1, i.
    We will now check which one is longer between odd and even, and then update the resultant longest accordingly.
    """
    # Current longest palindrome index
    longestPal = [0, 1]
    # For each letter
    for i in range(1, len(string)):
        # Odd length palindrome
        longestPalOne = longestPalindrome(string, i - 1, i + 1)
        # Even length palindrome
        longestPalTwo = longestPalindrome(string, i - 1, i)
        # Longest between odd and even
        currLongest = max(longestPalOne, longestPalTwo, key=lambda x: x[1] - x[0])
        # Updating the result by comparing with the current longest.
        longestPal = max(currLongest, longestPal, key=lambda x: x[1] - x[0])

    return string[longestPal[0] : longestPal[1] + 1]


def longestPalindrome(string, i, j):
    # If the index is out of bounds.
    if i < 0 and j >= len(string):
        return [0, 1]
    while i >= 0 and j < len(string):
        # If the strings match, then we move further to compare.
        if string[i] == string[j]:
            i -= 1
            j += 1
        else:
            # We break if the strings dont match anymore
            break
    # Since we had already moved forward towards the incorrect index, we will move backward by one step and return.
    return [i + 1, j - 1]
