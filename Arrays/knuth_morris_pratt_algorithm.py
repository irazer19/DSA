"""
Write a function that takes in two string and checks if the first string contains the second one using the Knuth
Morris Pratt algorithm.

string: "aefoaefcdaefcdaed"
substring: "aefcdaed"

"""


def knuthMorrisPrattAlgorithm(string, substring):
    # Time: O(n + m) and Space: O(m), n=string and m=substring
    """
    Logic:
    Naively, if the the letters of the two strings dont match then we would start the match again from the start
    of the second string. But we will overcome this.
    We will create a pattern of the second string such that we dont have to again start from the beginning but
    from the last pattern found.
    Once the pattern is created we will match the string and substring using the pattern.
    """
    # Building the pattern
    pattern = buildPattern(substring)
    # Result
    return doesMatch(string, substring, pattern)


def buildPattern(substring):
    # Pattern will contain at each index i, the end of the pattern at index j.
    pattern = [-1 for _ in substring]
    # Initializing the i and j
    j = 0
    i = 1
    # Iterating each char using i
    while i < len(substring):
        # If string i == j, then we know that the two same patterns exists, one ends at j and another ends at i.
        if substring[i] == substring[j]:
            # We store the end of the first pattern j at the ith index.
            pattern[i] = j
            # Move both the pointers because we may have more patterns
            i += 1
            j += 1
        # If the strings dont match and j > 0, then we move back j where the last pattern was found and select
        # the next index to it as our new j.
        elif j > 0:
            j = pattern[j - 1] + 1
        # If strings dont match and j=0, then we keep moving i as our pattern has not even begun.
        else:
            i += 1
    return pattern


def doesMatch(string, substring, pattern):
    # Initializing the the pointers for match
    i = 0
    j = 0
    # Moving till the end of the first string.
    while i < len(string):
        # IF the strings match
        if string[i] == substring[j]:
            # If this the last index of the substring, then its True
            if j == len(substring) - 1:
                return True
            # Keeping moving both the pointers
            i += 1
            j += 1
        # Same argument as above function buildPattern
        elif j > 0:
            j = pattern[j - 1] + 1
        # Same argument as above function buildPattern
        else:
            i += 1
    return False
