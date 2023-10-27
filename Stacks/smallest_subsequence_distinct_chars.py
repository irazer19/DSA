"""
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Example 1:
Input: s = "bcabc"
Output: "abc"

Example 2:
Input: s = "cbacdcbc"
Output: "acdb"

"""


def smallest_subsequence(s: str) -> str:
    # Time = Space = O(n)
    """
    Lexicographically smallest means: abc < bac because a occurs before b in the alphabet.
    We will use a stack to add the distinct chars, if we have not seen a char, then we will check whether this new
    char is lex-smaller that the current top element of the stack and if the top stack char is also present in the future
    of the string, if yes, then we will pop out the stack element so that we get lex-smaller arrangement in the stack.

    """
    # Getting the last occurance of the elements in the string s.
    last_seen = {s[i]: i for i in range(len(s))}
    # stacks to store the result
    stack = []
    visited = set()
    # For each char
    for i in range(len(s)):
        c = s[i]
        # If its an unseen char
        if c not in visited:
            # Now if the this unseen char is lex-smaller than the top stack element, and the top stack element
            # can also be found somewhere after this unseen element, then we will pop the stack element.
            # Ex: bab, since ab < ba, we will pop the first b element because we have seen that b again occurs after a.
            while stack and c < stack[-1] and last_seen[stack[-1]] > i:
                visited.remove(stack.pop())
            # Adding this new char to stack
            stack.append(c)
            # Marking it as seen
            visited.add(c)
    # Result
    return "".join(stack)


smallest_subsequence("bcabc")
