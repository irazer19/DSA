"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

"""


def palindromePartitioningMinCuts(string):
    # Time = Space = (n^2)
    # First step is to find all the palindromes starting from size 1 to n and store in the boolean matrix.
    arr = [[False for _ in range(len(string))] for _ in range(len(string))]

    # Since we wil move diagonally, the lower diagonal is useless.
    # The diagonal elements represent a single letter so it is a palindrome, so we store True.
    for i in range(len(string)):
        arr[i][i] = True

    # Now filling the upper diagonal of the matrix.
    # Starting from string size of length 2.
    for length in range(2, len(string) + 1):
        # Looping rows for every string of length 2.
        for row in range(0, len(string) - length + 1):
            # Calculating the column accordingly.
            col = row + length - 1
            # If the length is 2, just check whether the letters of row and column match.
            if length == 2:
                arr[row][col] = string[row] == string[col]
            else:
                # Else, check whether the current row and column match along with whether the center elements are
                # also a palindrome.
                arr[row][col] = string[row] == string[col] and arr[row + 1][col - 1]

    # Second step: We will use DP to store all the minimum cuts required till index i.
    # Since we want to minimize, we will initialize with infinity.
    min_cuts = [float('inf') for _ in string]
    # For every letter in the string
    for i in range(len(string)):
        # If the string from 0 to i is a palindrome then we dont need to cut at all, so we store 0.
        if arr[0][i]:
            min_cuts[i] = 0
        else:
            # Else, minimum cut is initialized as below, now 1 because since the current string was not a palindrome
            # we will have to cut at least once + whatever cut was required before the current letter.
            # Previous letter min cuts represents: the minimum cut needed till that letter.
            min_cuts[i] = 1 + min_cuts[i - 1]
            # Now we loop from 1 to i to check whether any previous letter till current letter is a palindrome.
            for j in range(1, i):
                # If yes, and the min_cuts is also lower then we update the min_cuts for current letter.
                # Else, the default initialized 1 + min_cuts[i - 1] will be used.
                if arr[j][i] and min_cuts[j - 1] + 1 < min_cuts[i]:
                    min_cuts[i] = min_cuts[j - 1] + 1

    # Last index contains the min_cuts till the full length of the string.
    return min_cuts[-1]


print(palindromePartitioningMinCuts('noonabbad'))
