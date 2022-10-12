"""
Write a function that takes in a string made up of brackets and other optional characters. The function should
return a boolean representing whether the string is balanced or not.

string= "([])(){}(())()()"
Output: True

"""


def balancedBrackets(string):
    # Time = Space = O(n)
    """
    Logic:
    For each char, if its open bracket, then add it to the stack.
    If it's a close bracket, then check whether a similar open bracket is already in the stack, if yes then pop it,
    else return False

    Finally, return True only if the stack is empty.

    """
    # To access the open bracket given a closed bracket.
    store = {'}': '{', ']': '[', ')': '('}
    # We maintain the open brackets in the stack.
    stack = []

    # For each char
    for c in string:
        # If its open bracket, then append it to the stack.
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            # Else if its a close bracket, and the top item in the stack is the similar open bracket, then pop.
            if stack and stack[-1] == store.get(c, None):
                stack.pop()
            else:
                # Else False
                return False
    return len(stack) == 0
