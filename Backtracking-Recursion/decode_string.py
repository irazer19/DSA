"""
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
exactly k times. Note that k is guaranteed to be a positive integer.

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

https://leetcode.com/problems/decode-string/description/

Brute Force:
Core Idea:
Think of the problem as nested subproblems
Each time we see a '[', we need to solve what's inside before multiplying
Use recursion to handle these nested parts

Key Principles:
When we hit a '[', make a recursive call to process everything inside until matching ']'
Keep track of current position in string using an index
Build numbers digit by digit before '['
Return both the decoded substring and next position after ']'

Time Complexity: O(n * k) where n is the length of the input string and k is the maximum value of the multiplier
Space Complexity: O(n) for the recursion stack

Optimized:
Core Idea:
Use stack to remember "outer" context while processing "inner" brackets
Stack stores tuples of (string_so_far, number_of_repetitions)
Build result incrementally without recursion

Key Principles:
Stack represents the "state" before entering each '['
When we see '[': push current state, start fresh
When we see ']': pop previous state, multiply current string
Numbers and letters are processed as we see them

Time = Space = O(n)

"""


def brute_force(s: str) -> str:
    def decode_helper(s: str, i: int) -> tuple[str, int]:
        result = []
        num = 0

        while i < len(s):
            char = s[i]

            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                # Recursive call to handle nested brackets
                substring, next_i = decode_helper(s, i + 1)
                result.append(substring * num)
                num = 0
                i = next_i
            elif char == "]":
                return "".join(result), i
            else:
                result.append(char)
            i += 1

        return "".join(result), i

    decoded_string, _ = decode_helper(s, 0)
    return decoded_string


def optimized_stack(s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == "[":
            # Push the current state to stack
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0
        elif char == "]":
            # Pop the previous state
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char

    return current_string
