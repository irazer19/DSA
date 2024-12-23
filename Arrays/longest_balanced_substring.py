"""
Write a function that takes in a string made up of parentheses, and returns an integer representing the
length of the longest balanced substring with regard to parentheses.

string = "(()))("
expected = 4

https://leetcode.com/problems/longest-valid-parentheses/description/
"""


# Brute Force Solution
def BruteForce(s: str) -> int:
    """
    Time Complexity: O(n³) - We check all possible substrings of even length and validate each one
    Space Complexity: O(n) - For the stack in isValid function
    """

    def isValid(substring: str) -> bool:
        stack = []
        for char in substring:
            if char == "(":
                stack.append(char)
            else:  # char is ')'
                if not stack:  # no matching '(' found
                    return False
                stack.pop()
        return len(stack) == 0

    n = len(s)
    max_length = 0

    # Try all possible substrings
    for i in range(n):
        for j in range(
            i + 2, n + 1, 2
        ):  # j+2 because valid strings must have even length
            if isValid(s[i:j]):
                max_length = max(max_length, j - i)

    return max_length


def longestBalancedSubstring(string):
    """
    Optimized:
    1. We use a stack to keep track of indices of '(' characters and the last invalid position
    2. When we see a '(':
                            i. Push its index onto the stack
    3. When we see a ')':
                            i. Pop from the stack (removing the matching '(' index)
                            ii. If stack becomes empty, push current index (new base)
                            iii. If stack not empty, calculate length between current index and last index on stack
    Time = Space = O(n)
    """
    stack = [-1]  # Initialize with -1 as base index
    max_length = 0

    for i in range(len(string)):
        if string[i] == "(":
            stack.append(i)
        else:  # if s[i] == ')'
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - stack[-1])

    return max_length
