"""
A string s is called good if there are no two different characters in s that have the same frequency.
Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example,
in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
"""


def minDeletions_bruteforce(s: str) -> int:
    """
    Keep a set of seen frequencies. For each character's frequency, keep decrementing it until we find an unused frequency (including 0), counting each decrement as a deletion.
    Time Complexity: O(n·k) where n is the length of string and k is the maximum frequency of any character
    Space Complexity: O(k) where k is the number of unique frequencies
    """
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    deletions = 0
    seen_frequencies = set()

    # For each character frequency
    for char, count in freq.items():
        current_count = count
        # Keep reducing frequency until we find a unique one
        while current_count > 0 and current_count in seen_frequencies:
            current_count -= 1
            deletions += 1
        seen_frequencies.add(current_count)

    return deletions


def minDeletions_optimized(s: str) -> int:
    """
    Sort frequencies in descending order, then ensure each frequency is strictly less than the previous one by reducing it as needed.
    The core idea is that for frequencies to be unique, when sorted in descending order, each number must be less than the previous
    one (like 5,4,2,1). Any time this rule is violated, we must reduce numbers until the rule is satisfied.

    Time: O(n + k²) where:
    n is the length of input string (for counting frequencies)
    k is the number of unique characters (k ≤ 26)
    The k² comes from the nested while loops that may need to check previous frequencies

    Space: O(1) since we're still using a fixed-size array (max 26 characters)
    """
    # Count frequencies
    freq = [0] * 26
    for char in s:
        freq[ord(char) - ord("a")] += 1

    # Sort frequencies in descending order and remove zeros
    freq = sorted([f for f in freq if f > 0], reverse=True)

    deletions = 0

    # Process each frequency
    for i in range(1, len(freq)):
        # If current frequency needs to be reduced
        while freq[i] >= freq[i - 1] and freq[i] > 0:
            freq[i] -= 1
            deletions += 1
        # If we have equal frequencies greater than 0
        while freq[i] > 0 and freq[i] in freq[:i]:
            freq[i] -= 1
            deletions += 1

    return deletions
