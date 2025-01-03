"""
Given the number of tags, generate all possible valid div tags.

Input: 3

Output:

['<div><div><div></div></div></div>', '<div><div></div><div></div></div>', '<div><div></div></div><div></div>',
'<div></div><div><div></div></div>', '<div></div><div></div><div></div>']

Brute force:
The idea is to generate all possible combinations of opening and closing div tags, then filter out invalid ones
Time = Space = O(2^(2n))


Optimized Solution (Backtracking):
Uses backtracking to only generate valid combinations
The core insight is based on two key rules for generating valid div tags:
- At any point while building the string, you can add an opening tag <div> as long as you haven't used all n opening tags yet.
- You can only add a closing tag </div> if you have more opening tags than closing tags used so far (to ensure proper nesting).

Time Complexity: O(C(n)) where C(n) is the nth Catalan number
Space Complexity: O(n) for recursion stack
"""


def generateDivTags(numberOfTags):
    result = []
    # Initially, we have the total open and closed tags = numberOfTags.
    solve(numberOfTags, numberOfTags, result, [])

    return result


def solve(openTagLeft, closeTagLeft, result, stack):
    # We keep using the open tags and call the function until it exhausts.
    if openTagLeft > 0:
        # Appending the open tag to the stack
        stack.append("<div>")
        # In the next call, we subtract 1 from the openTagLeft since we have already used one.
        solve(openTagLeft - 1, closeTagLeft, result, stack)
        # Pop the open tag.
        stack.pop()
    # If we still have closing tags left and also have open tags in the stack, only then we use the close tags.
    # (We cannot close if it's not open.)
    if closeTagLeft > 0 and openTagLeft < closeTagLeft:
        stack.append("</div>")
        # Subtract from the closeTagLeft since we have already used one.
        solve(openTagLeft, closeTagLeft - 1, result, stack)
        stack.pop()

    # If we have exhausted all the closing tags, then we add the stack's configuration to the result.
    if closeTagLeft == 0:
        result.append("".join(stack))


print(generateDivTags(3))
