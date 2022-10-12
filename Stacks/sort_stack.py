"""
Write a function that takes in an array of integers representing a stack, recursively sorts the stack in place,
and returns it.

stack = [-5, 2, -2, 4, 3, 1]
Output: [-5, -2, 1, 2, 3, 4]

"""


def sortStack(stack):
    # Time: O(n^2) and Space: O(n)
    """
    Logic:
    First we pop all the elements from the stack recursively, and then start adding the elements in the same order
    in a different function which uses recursion.
    """
    sortProcess(stack)
    return stack


def sortProcess(stack):
    # If the stack is empty
    if not stack:
        return
    # Else we keep popping elements
    currVal = stack.pop()
    sortStack(stack)
    # On return, we inserting this element.
    insertVal(currVal, stack)


def insertVal(val, stack):
    # If stack is empty, add the element and return
    if not stack:
        stack.append(val)
        return
    # If the last stack element is small then add it.
    if stack[-1] <= val:
        stack.append(val)
        return
    # Else, pop the stack element and call again.
    currVal = stack.pop()
    insertVal(val, stack)
    # We insert back the element which we popped.
    stack.append(currVal)
