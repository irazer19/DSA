"""
Given a string of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that
the resultant string is a palindrome.

Note: The order of characters should be maintained.

https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
"""


def minDeletionForPalindrome(string):
    # Time = Space = O(n x n)
    # Using DP, we create a matrix of size n x n.
    # Each cell represents: The min deletion to make palindrome from row'th index of the string to
    # the col'th index of the string.
    store = [[0 for _ in range(len(string))] for _ in range(len(string))]

    # We have to move diagonally, lower half of the diagonal is same as upper half of the diagonal, so we ignore it.
    # For all the diagonal index, its a single element, which is already a palindrome, so we store 0
    for i in range(len(store)):
        store[i][i] = 0

    # Now we start filling diagonally, the rest of the matrix.
    # We check all the string of length 2, then 3, then 4, then 5, ... so on till then full length of the string.
    # We start with length 2 because we have already filled the diagonal which was of length 1.
    for length in range(2, len(string) + 1):
        # Now we loop over the rows which start from 0 till the row where diagonal element can be filled.
        for row in range(0, len(string) - length + 1):
            # We calculate the column to fill with respect to the row.
            col = row + length - 1
            # If the letters match at the row and column, then we dont delete anything as its already a palindrome.
            # So we simply store the min deletion for the center elements.
            if string[row] == string[col]:
                store[row][col] = store[row + 1][col - 1]
            else:
                # Else, we take the min of [start, end-1] O [start+1, end], since we have two directions to go.
                # Ex: abbedk = a & k dont match, so we check max (abbed, bbedk)
                # We store extra 1 because we know since two letters dont match, we need at least 1 deletion to
                # make it a palindrome.
                store[row][col] = 1 + min(store[row + 1][col], store[row][col - 1])
    # Since we move diagonally, result is stored at topmost right
    return store[0][-1]


print(minDeletionForPalindrome("leetcode"))
