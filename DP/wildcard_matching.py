"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

"""


def wildcard(s, p):
    # Time = Space = O(s x p)
    # Using DP, create a matrix, where rows = string and columns = pattern.
    # Each cell represents: Whether it is possible to match the string till i using the pattern till j.
    # We pad the matrix with extra +1 to start with null string
    store = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
    # When pattern is "" and string is "", both match
    store[0][0] = True

    # Now, In the case of *, if the previous column has True/False, we store that in the current column.
    # Logic: For *, If any of the previous diagonal cell, left cell or top cell is True, then we store True in the
    # current cell because it does not matter as the * captures everything including empty chars.
    for j in range(1, len(store[0])):
        if p[j - 1] == '*':
            store[0][j] = store[0][j - 1]

    # Filling the rest of the matrix
    for i in range(1, len(store)):
        for j in range(1, len(store[0])):
            # Case if the wildcard is *, as same reason as discussed above.
            if p[j - 1] == '*':
                store[i][j] = store[i - 1][j] or store[i][j - 1] or store[i - 1][j - 1]
            # If the wildcard is ?, then the current char surely matches, now if the previous diagonal cell is True
            # only then we store True. Same explanation goes if the match happens with wildcard letter [a-z].
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                store[i][j] = store[i - 1][j - 1]

    return store[-1][-1]


print(wildcard(s="adceb", p="*a*b"))
