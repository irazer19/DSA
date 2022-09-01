"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

"""


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
                arr[i][j] = min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + 1
    return arr[-1][-1]


print(levenshteinDistance("abc", "yabd"))
