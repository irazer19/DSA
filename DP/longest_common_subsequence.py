"""
Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that
appears in the same relative order, but not necessarily contiguous. For example, “abc”, “abg”, “bdf”, “aeg”, ”acefg”,
.. etc are subsequences of “abcdefg”.

"""


def longestCommonSubsequence(str1, str2):
    # Time = Space = O(n x m)
    # Using DP, we start with empty string so +1 extra length.
    # The first row & column is 0 because nothing is common with an empty string.
    store = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    # Filling the rest of the matrix starting from 1, 1
    for i in range(1, len(store)):
        for j in range(1, len(store[0])):
            # If ith letter of string2 == jth letter of string1, then it is a match and so we store
            # 1 + previous diagonal value (Total match before the current letter
            if str2[i - 1] == str1[j - 1]:
                store[i][j] = store[i - 1][j - 1] + 1
            else:
                # Else: Say have 'abcde' so we try: max('abcd', 'bcde'), common sense.
                store[i][j] = max(store[i][j - 1], store[i - 1][j])
    # If we want to build the sequence.
    return build_seq(store, str1, str2)


def build_seq(store, str1, str2):
    # To store the sequence.
    res = []
    # We start at the end of the matrix
    row = len(store) - 1
    col = len(store[0]) - 1
    # If the pointers reach the 1st row or 1st column then we stop, because its an empty string.
    while row > 0 and col > 0:
        # If both the letters match of given row and column, that means we can added this letter and directly
        # move to the previous diagonal.
        if str2[row - 1] == str1[col - 1]:
            res.append(str2[row - 1])
            row -= 1
            col -= 1
        else:  # Else: We move that cell whichever gave the maximum value, either left or top.
            if store[row - 1][col] >= store[row][col - 1]:
                row -= 1
            else:
                col -= 1
    # Reverse the result because we traversed from bottom to top.
    return list(reversed(res))


print(longestCommonSubsequence("ZXVVYZW", "XKYKZPW"))
