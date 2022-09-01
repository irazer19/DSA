"""
Given two strings, find the length of longest substring present in both of them. A substring is a sequence that
appears in the same continuous relative order.
"""


def longestCommonSubstring(str1, str2):
    # Time = Space = O(n x m)
    # Using DP, we start with empty string so +1 extra length.
    # The first row & column is 0 because nothing is common with an empty string.
    store = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    result = 0

    # Filling the rest of the matrix starting from 1, 1
    for i in range(1, len(store)):
        for j in range(1, len(store[0])):
            # If ith letter of string2 == jth letter of string1, then it is a match and so we store
            # 1 + previous diagonal value (Total match before the current letter)
            if str2[i - 1] == str1[j - 1]:
                store[i][j] = store[i - 1][j - 1] + 1
            else:
                # Else we store 0, because the current letters dont match so we start with 0 again.
                store[i][j] = 0
            # Update the result with max value
            result = max(result, store[i][j])

    return result


print(longestCommonSubstring("zxabcdezy", "yzabcdezx"))
