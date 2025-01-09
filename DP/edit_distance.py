"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

https://leetcode.com/problems/edit-distance/
"""


def minDistance_brute(word1: str, word2: str) -> int:
    """
    The brute force approach would involve trying every possible combination of operations recursively.
    Time Complexity: O(3^(m+n)) where m and n are lengths of word1 and word2
    Space Complexity: O(m+n) due to recursion stack
    """

    def recursive_distance(i: int, j: int) -> int:
        # Base cases
        if i == len(word1):
            return len(word2) - j  # Insert remaining characters from word2
        if j == len(word2):
            return len(word1) - i  # Delete remaining characters from word1

        # If characters match, move to next characters
        if word1[i] == word2[j]:
            return recursive_distance(i + 1, j + 1)

        # Try all three operations and take minimum
        insert = recursive_distance(i, j + 1)  # Insert:
        delete = recursive_distance(i + 1, j)  # Delete
        replace = recursive_distance(i + 1, j + 1)  # Replace

        return 1 + min(insert, delete, replace)

    return recursive_distance(0, 0)


def levenshteinDistance(str1, str2):
    # Time = Space = O(n x m)
    # Creating a matrix starting with empty string.
    arr = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    # Filling the first row/column with same index, because to convert empty string to x, we will need x add operations.
    for i in range(len(arr)):
        arr[i][0] = i
    for i in range(len(arr[0])):
        arr[0][i] = i

    # Starting to fill the matrix from 1, 1
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            # If the letters are same then we dont perform any operation so just add previous diagonal.
            if str1[j - 1] == str2[i - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                # Else, take the minimum of the top, left, diagonal and add 1.
                # We add 1 because since the letters dont match, at least 1 operation will be performed to match them.
                # Delete: arr[i - 1][j]
                # Insert: arr[i][j - 1]
                # Replace: arr[i - 1][j - 1]
                arr[i][j] = min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + 1
    return arr[-1][-1]


print(levenshteinDistance("abc", "yabd"))
