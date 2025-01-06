"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the
input string valid.
Return all the possible results. You may return the answer in any order.

Input: s = "()())()"
Output: ["(())()","()()()"]

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]

https://leetcode.com/problems/remove-invalid-parentheses/description/

Brute Force: Try all combinations and check if the string is valid.
Time: O(2^n) and Space: O(n)

"""


def removeInvalidParentheses(s):
    # Time: O(2^n) and Space: O(n)
    """
    Logic:
    At every char, we will make two function calls, with including the current char and excluding the current char.
    If its a letter then we will just include and move to the next index.
    Base case: If total opened brackets == total closed brackets, then we will append the stack in the result.

    Finally, since the result can contain multiple different length strings, we will select those strings which
    have the longest length covering all the brackets till the end of the string.

    """
    # Storing results in set to remove duplicates
    result = set()
    # Calling dfs
    dfs(s, 0, result, [], 0, 0)
    # Finding the longest string present in the result, and including only those strings which have that length.
    longestString = max(result, key=lambda x: len(x))
    result = [r for r in result if len(r) == len(longestString)]

    return result


def dfs(s, idx, result, stack, opened, closed):
    # Base case
    if idx >= len(s):
        # If opened and closed brackets are balanced, we append the stack to the result
        if opened == closed:
            result.add("".join(stack))
        return
    # If the current char is open
    if s[idx] == "(":
        # Including in the stack and making the function call
        stack.append(s[idx])
        dfs(s, idx + 1, result, stack, opened + 1, closed)
        stack.pop()
        # Making the function call by removing from the stack
        dfs(s, idx + 1, result, stack, opened, closed)
    elif s[idx] == ")":
        # First making the function call by excluding the closed bracket
        dfs(s, idx + 1, result, stack, opened, closed)
        # Now we will only include the closed bracket, if the number of open brackets > closed brackets
        if opened > closed:
            stack.append(s[idx])
            dfs(s, idx + 1, result, stack, opened, closed + 1)
            stack.pop()
    else:
        # If the current char is an alphabet, we just include it and move to the next index.
        stack.append(s[idx])
        dfs(s, idx + 1, result, stack, opened, closed)
        stack.pop()
