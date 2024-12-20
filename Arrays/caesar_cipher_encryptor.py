"""
Given a non-empty string of lowercase letters and a non-negative integer representing a key, write a function that
returns a new string obtained by shifting every letter in the string by k positions in the alphabet, where k is the key.

strings= "xyz"
key=2
Output= "zab"

Similar: https://leetcode.com/problems/shifting-letters/
"""


def caesarCipherEncryptor(string, key):
    # Time: O(n) and Space: O(n)
    """
    Logic:
    We will take the mod of the key, and the for every letter, we will add the key to its ordinal value.
    We will check whether the ordinal value is within the alphabet range or greater than 122, and extract the
    correct letter.
    """
    # Mod of key
    key = key % 26
    result = []
    for c in string:
        # new ordinal value after adding the key
        totalOrd = ord(c) + key
        # If the new ordinal value is <= 122, then we are good.
        # Else we will take the mod of 122, and then add the remainder to the starting letters ordinal value.
        newCharOrd = totalOrd if totalOrd <= 122 else 96 + (totalOrd % 122)
        result.append(chr(newCharOrd))
    return "".join(result)
