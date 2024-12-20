"""
The factorial of a positive integer n is the product of all positive integers less than or equal to n.

For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
We make a clumsy factorial using the integers in decreasing order by swapping out the multiply operations for a fixed rotation of operations
with multiply '*', divide '/', add '+', and subtract '-' in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
However, these operations are still applied using the usual order of operations of arithmetic. We do all multiplication and division steps before any
addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 = 90 / 8 = 11.
Given an integer n, return the clumsy factorial of n.


Example 1:

Input: n = 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1

https://leetcode.com/problems/clumsy-factorial/

"""


def clumsy(n: int) -> int:
    """
    Using a stack-based approach.
    The code uses a stack to calculate expressions like "10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1" by rotating through
    4 operations (multiply, divide, add, subtract). When we hit multiply/divide, we operate on the top of stack;
    for add/subtract, we push numbers (negative for subtraction). Finally, we sum up the stack to get the result.

    Time = Space = O(n)
    """
    # Stack to store intermediate results
    stack = [n]
    n -= 1
    index = 0

    # Process each number with the rotating operations
    while n > 0:
        # Get current operation based on index
        if index % 4 == 0:  # Multiply
            stack.append(stack.pop() * n)
        elif index % 4 == 1:  # Divide
            stack.append(int(stack.pop() / n))  # Use int for floor division
        elif index % 4 == 2:  # Add
            stack.append(n)
        else:  # Subtract
            stack.append(-n)

        n -= 1
        index += 1

    # Sum up all values in the stack
    return sum(stack)
