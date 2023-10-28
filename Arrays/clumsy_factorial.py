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

"""


def clumsy(n: int) -> int:
    # Time: O(n) and Space: O(1)
    """
    We will rotate the operator by using modulus %, as we increment the index to the next operator.
    Now in this question, a * is followed by /, so whenever we get *, we will compute the full a * b / c value,
    so that we get the correct mathematical result, and then prev = a * b / c.
    Rest of the operators, +,-, we will simply keep adding/subtract from the result as we move.

    """
    # Edge case, as we start by computing the result for the first 3 elements: a * b / c
    if n == 3:
        return 6
    if n == 2:
        return 2
    if n == 1:
        return 1
    # First 3 elements result
    result = int(n * (n - 1) / (n - 2))
    # Previous computed result
    prev = int(n * (n - 1) / (n - 2))
    # Operators which we will rotate using %
    op = ["*", "/", "+", "-"]
    # Starting operator
    op_idx = 2
    # start from the 4h element
    num = n - 3
    while num > 0:
        # Getting the operator
        op_idx = op_idx % len(op)
        # If its *, then we will try to compute all three elements including / division
        if op[op_idx] == "*":
            # If this is not the last element
            if num - 1 > 0:
                # subtract the prev result
                result -= prev
                # Now compute the all 3 element result
                result += int(prev * num / (num - 1))
                # Make it as prev
                prev = int(prev * num / (num - 1))
                # Move two elements ahead, as we also used / with the next element
                num -= 2
                # Move two operators ahead as we also used /
                op_idx += 2
            else:
                # Else we will only use *, and do the basic computation
                result -= prev
                result += prev * num
                prev = prev * num
                num -= 1
                op_idx += 1
        elif op[op_idx] == "+":
            result += num
            prev = num
            op_idx += 1
            num -= 1
        elif op[op_idx] == "-":
            result -= num
            # Remember: for negative -, we will store the prev = -num
            prev = -num
            op_idx += 1
            num -= 1
    return result
