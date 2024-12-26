"""
You are given a string s consisting only of lowercase English letters.
In one move, you can select any two adjacent characters of s and swap them.
Return the minimum number of moves needed to make s a palindrome.
Note that the input will be generated such that s can always be converted to a palindrome.

Input: s = "aabb"
Output: 2
Explanation:
We can obtain two palindromes from s, "abba" and "baab".
- We can obtain "abba" from s in 2 moves: "aabb" -> "abab" -> "abba".
- We can obtain "baab" from s in 2 moves: "aabb" -> "abab" -> "baab".
Thus, the minimum number of moves needed to make s a palindrome is 2.

https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/description/

Brute Force:

Generate all possible palindromes that can be made from the input string using adjacent swaps
For each possible palindrome, calculate the minimum moves needed to reach it
Return the minimum among all paths

We can do this using backtracking - at each step, try all possible adjacent swaps and keep track of number of moves.
Since each position has a choice to swap with its next position, it's essentially generating all permutations that can
be reached through adjacent swaps.
Time: O(n! * n), because we are doing permutation.
Space: O(n), for the recursion stack

Optimized:
"For each pair of positions (left and right), find the matching character from either direction (right->left or left->right)
and count the moves needed to swap the characters together through adjacent swaps."

The solution works because it's a greedy approach:
1. When we find an unmatched pair, we look for a match from both directions
2. We implicitly choose the shorter path by trying right side first, then left side
3. Variable moves simply accumulates the number of swaps needed
Time: O(n²)
Space: O(n)
"""


def minMovesToMakePalindrome(s):
    s = list(s)
    moves = 0
    left = 0
    right = len(s) - 1

    while left < right:
        # If characters match, no swaps needed
        if s[left] == s[right]:
            left += 1
            right -= 1
            continue

        # Look for matching character from right
        j = right - 1
        found = False
        while j > left:
            if s[j] == s[left]:
                # Found match, swap it to rightmost position
                while j < right:
                    s[j], s[j + 1] = s[j + 1], s[j]
                    moves += 1
                    j += 1
                found = True
                break
            j -= 1

        # If no match found from right side, try from left side
        if not found:
            j = left + 1
            while j < right:
                if s[j] == s[right]:
                    # Found match, swap it to leftmost position
                    while j > left:
                        s[j], s[j - 1] = s[j - 1], s[j]
                        moves += 1
                        j -= 1
                    break
                j += 1

        # Move to next pair
        left += 1
        right -= 1

    return moves
