"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""


def wordBreak(s: str, wordDict) -> bool:
    # Time: O(n^2 x m) and Space: O(n), where n = length of s and m = len(wordDict)
    # Extra n in the time is because the slicing takes O(n).
    # Using DP, starting for every letter we store whether any word is possible.
    # Extra + 1 length is because the last letter as empty string is always present.
    store = [False for _ in range(len(s) + 1)]
    store[-1] = True
    # We start checking for the word from the end of the string.
    for i in range(len(s) - 1, -1, -1):
        # Now we check whether any word of the wordDict is present starting from index i of the string s.
        for word in wordDict:
            # To check the word, first we check whether the current word length starting from index i is within
            # the bounds of the string.
            if i + len(word) <= len(s):
                # Now we slice the string starting from index i to the current word length and match the word.
                # If the word matches and also if the next word was also present, only then we add True for the current
                # word.
                if s[i: i + len(word)] == word and store[i + len(word)] is True:
                    store[i] = True
                    break  # We break because there is no need to check for another word.
                # Else: the store[i] will remain False.
    # Store[0] will be True only if all the next words were also present.
    return store[0]


print(wordBreak('leetcode', ['leet', 'code']))
