"""
Given the number of tags, generate all possible valid div tags.

Input: 3

Output:

['<div><div><div></div></div></div>', '<div><div></div><div></div></div>', '<div><div></div></div><div></div>',
'<div></div><div><div></div></div>', '<div></div><div></div><div></div>']

"""


def generateDivTags(numberOfTags):
    # Time = Space = O(2n!), because basically we are finding permutation, where the total number of elements
    # is 2 * numberOfTags.

    """
    Logic:
    We use two variables, openTagLeft and closeTagLeft, where
    openTagLeft = Total number of open tags left with us.
    closeTagLeft = Total number of close tags left with us.

    We start the recursive call by using the open tag until we exhaust all open tags, then we start closing the
    tags. At every open/close we append the div tag in the stack, and once the function returns, we pop it from stack.

    Also, we can only use close tag if we have already used an open tag, therefore: openTagLeft < closeTagLeft
    is the condition to use a closing tag.
    If the number of closing tags == 0, then we store the current stack configuration in the result.

    """
    result = []
    # Initially, we have the total open and closed tags = numberOfTags.
    solve(numberOfTags, numberOfTags, result, [])

    return result


def solve(openTagLeft, closeTagLeft, result, stack):
    # We keep using the open tags and call the function until it exhausts.
    if openTagLeft > 0:
        # Appending the open tag to the stack
        stack.append('<div>')
        # In the next call, we subtract 1 from the openTagLeft since we have already used one.
        solve(openTagLeft - 1, closeTagLeft, result, stack)
        # Pop the open tag.
        stack.pop()
    # If we still have closing tags left and also have open tags in the stack, only then we use the close tags.
    # (We cannot close if it's not open.)
    if closeTagLeft > 0 and openTagLeft < closeTagLeft:
        stack.append('</div>')
        # Subtract from the closeTagLeft since we have already used one.
        solve(openTagLeft, closeTagLeft - 1, result, stack)
        stack.pop()

    # If we have exhausted all the closing tags, then we add the stack's configuration to the result.
    if closeTagLeft == 0:
        result.append(''.join(stack))


print(generateDivTags(3))
