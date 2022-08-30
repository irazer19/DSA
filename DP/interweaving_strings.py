"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

"""


def interweavingStrings(one, two, three):
    # Time = Space = O(n x m)
    # Edge Case where the lengths dont match.
    if len(three) != len(one) + len(two):
        return False

    # We use DP here, inside the cache we store whether its possible to get the answer
    # using the ith index of string1 and jth index of string2. If not then we store cache[i][j] = False
    # We loop one extra length to cover out of bound case if one string length is greater than the other.
    cache = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]
    # We i = 0, j = 0, k = 0, where i = String1, j = String2, k = Target String3
    return solve(one, two, three, 0, 0, 0, cache)


def solve(one, two, three, i, j, k, cache):
    # If the cache already has a boolean value then return that result
    if cache[i][j] != None:
        return cache[i][j]

    # If we have reached the end of the String3, this is a success case.
    if k == len(three):
        return True

    # Trying with the ith index of the String1, if it matches the kth char of the String3
    # then do recursion by moving to i+1 and to k+1
    if i < len(one) and one[i] == three[k]:
        cache[i][j] = solve(one, two, three, i + 1, j, k + 1, cache)
        # If the result is success then just return True
        if cache[i][j]:
            return True
    # Trying with the jth index of the String2, if it matches the kth char of the String3
    # then do recursion by moving to j+1 and to k+1
    if j < len(two) and two[j] == three[k]:
        cache[i][j] = solve(one, two, three, i, j + 1, k + 1, cache)
        # If the result is success then just return True
        if cache[i][j]:
            return True
    # Case where both the conditions above failed, we store False for the current i, j
    cache[i][j] = False
    return False


print(interweavingStrings("aabcc", "dbbca", "aadbbcbcac"))
