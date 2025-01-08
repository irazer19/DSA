"""
Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]

https://leetcode.com/problems/concatenated-words/description/
"""


def brute_force(words):
    """
    Time Complexity: O(2^N * M) where N is the length of longest word and M is number of words.
    For each prefix we have two choices, either we do recursion or we don't, which is why its 2^N
    Space Complexity: O(N) for recursion stack
    """
    # Convert words to set for O(1) lookup
    word_set = set(words)
    result = []

    def canForm(word, start, count):
        # If we reached end of word and used at least 2 words
        if start == len(word) and count >= 2:
            return True

        # Try all possible prefixes
        for i in range(start, len(word)):
            prefix = word[start : i + 1]
            # Check if prefix exists in word_set
            if prefix in word_set:
                # Remove the word itself from consideration
                if prefix == word and start == 0:
                    continue
                # Recursively check remaining part
                if canForm(word, i + 1, count + 1):
                    return True
        return False

    # Check each word
    for word in words:
        if canForm(word, 0, 0):
            result.append(word)

    return result


def findAllConcatenatedWordsInADict(words):
    # Time: O(n * w^2) and Space: O(n), where n is number of words, and w is length of the longest word.
    """
    Logic
    For each word, we will break into multiple partitions to check whether its present in the word list.
    Its similar to word break problem, the only difference is that if a partition is present in the word list, then
    it should not be equal to the current word itself.
    """
    # Creating dictionary for fast access
    wordSet = {w: True for w in words}
    # Storing result
    result = []
    # For each word
    for word in words:
        # If we were able to break the word and all those parts were present in the dictionary then we add this
        # word to the result.
        if wordBreak(word, wordSet):
            result.append(word)
    return result


def wordBreak(word, wordSet):
    # Storing whether the word is present starting from ith index
    dp = [False for _ in range(len(word) + 1)]
    # We will start from the end index, so we will pad an extra length to True
    dp[-1] = True

    # Starting from the end index
    for i in range(len(word) - 1, -1, -1):
        # We will compute multiple length of the word from ith index
        for j in range(i + 1, len(word) + 1):
            # If ith to jth word is present in the dictionary, and the next word which starts at jth index is also
            # True, and the current ith to jth word is not the same as the current entire word.
            if word[i:j] in wordSet and dp[j] and word[i:j] != word:
                # We mark at ith index that there is a word present here.
                dp[i] = True
                # We break because we dont need any more words to check at ith index since we already have found a word.
                break
    # The 0th index will either rbe True or False
    return dp[0]
