"""
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without
changing the order of the remaining elements.

https://leetcode.com/problems/longest-palindromic-subsequence/

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".


"""


def brute_force(s: str) -> int:
    """
    Time Complexity: O(2^n * n), where n is the length of the string
    Space Complexity: O(2^n)
    Approach:

    Generate all possible subsequences of the string
    Check each subsequence if it's a palindrome
    Keep track of the maximum length palindromic subsequence

    """

    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    def generate_subsequences(s: str) -> list[str]:
        if not s:
            return [""]

        # Get all subsequences without the first character
        subsequences = generate_subsequences(s[1:])

        # Add the first character to all existing subsequences
        return subsequences + [s[0] + sub for sub in subsequences]

    # Generate all possible subsequences
    subsequences = generate_subsequences(s)

    # Find the longest palindromic subsequence
    max_length = 0
    for sub in subsequences:
        if is_palindrome(sub) and len(sub) > max_length:
            max_length = len(sub)

    return max_length


def longestPalindromicSubsequence(string):
    # Time = Space = O(n x n)
    # Using DP, we create a matrix of size n x n.
    # Each cell represents: The longest palindromic subsequence from row'th index of the string to
    # the col'th index of the string.
    store = [[0 for _ in range(len(string))] for _ in range(len(string))]

    # We have to move diagonally, lower half of the diagonal is same as upper half of the diagonal, so we ignore it.
    # For all the diagonal index, its a single element, so the size of palindrome is 1.
    for i in range(len(store)):
        store[i][i] = 1

    # Now we start filling diagonally, the rest of the matrix.
    # We check all the string of length 2, then 3, then 4, then 5, ... so on till then full length of the string.
    # We start with length 2 because we have already filled the diagonal which was of length 1.
    for length in range(2, len(string) + 1):
        # Now we loop over the rows which start from 0 till the row where diagonal element can be filled.
        for row in range(0, len(string) - length + 1):
            # We calculate the column to fill with respect to the row.
            col = row + length - 1
            # If the letters match at the row and column, then we have two different letters whose size is 2.
            # So the palindrome size = 2 + Palindrome size of the center elements.
            if string[row] == string[col]:
                store[row][col] = 2 + store[row + 1][col - 1]
            else:
                # Else, we take the max of [start, end-1] O [start+1, end], since we have two directions to go.
                # Ex: abbedk = a & k dont match, so we check max (abbed, bbedk)
                store[row][col] = max(store[row][col - 1], store[row + 1][col])
    # Since we move diagonally, result is stored at topmost right
    return store[0][-1]


print(longestPalindromicSubsequence("abcb"))
