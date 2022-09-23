"""
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary
operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
"""


def expressionAddOperator(num, target):
    # Time: O(4^n) and Space: O(n), space is n because extra space is only used in call stack.
    # We are not counting the space for storing the result.
    """
    Logic:
    We use DFS:
    1. We generate all the possible numbers from the expression:
    Example: '123', we generate [1, 2, 3], [1, 23], [12, 3], [123]
    For each output above, we try adding different operators in between the numbers to find the target.

    stack = We store the order of the numbers with the operators in between them.
    currSum = We maintain the total sum till the current recursive call.
    prev = The previous number in the last recursion, we use it during the multiplication operator.
    result = Stores all the valid expression which sums to target.

    """

    result = []
    dfs(num, target, 0, [], 0, 0, result)

    return result


def dfs(num, target, idx, stack, curSum, prev, result):
    # If the idx is out of bounds and the current sum = target, then we add the stack's expression to the result.
    if idx == len(num) and curSum == target:
        result.append(''.join(stack))
        return

    # Starting from given idx, we slice the num to get different length number,
    # example: 1(first iteration), then 12 (2nd iteration), then 123 (3rd iteration).
    for i in range(idx, len(num)):
        # Getting the sliced number and converting to integer.
        val = int(num[idx: i + 1])
        # If this is the first number, then we cannot add an operator before it
        if idx == 0:
            # i + 1 = Moving to the next index of num
            # stack + [num[idx: i + 1]] = Appending newly sliced number to the stack
            # currSum = val, because for the first number, the total sum is this number itself.
            # prev = val, for the next call, the current value is the previous value.
            dfs(num, target, i + 1, stack + [num[idx: i + 1]], val, val, result)
        else:
            # stack + ['+'] + [num[idx: i + 1]] = Appending newly sliced number to the stack along with the operator.
            # For addition and subtraction, curSum = curSum +/- val, but for multiplication it is tricky,
            # For multiplication: curSum = curSum - prev + val * prev, because of BODMAS rule, if the current
            # operator is *, then let's take an example: 2 + 3 * 4,
            # Here, the currSum = 5, prev = 3, and val = 4. Normally, we get the currSum = 5 * 4 = 20 which is wrong.
            # So that's why we do (val(4) * prev(3)) + 2, we get 2 using (currSum - prev).
            # And therefore, the "prev" for multiplication = val * prev, because of the BODMAS rule.
            dfs(num, target, i + 1, stack + ['+'] + [num[idx: i + 1]], curSum + val, val, result)
            dfs(num, target, i + 1, stack + ['-'] + [num[idx: i + 1]], curSum - val, -val, result)
            dfs(num, target, i + 1, stack + ['*'] + [num[idx: i + 1]], curSum - prev + val * prev, val * prev, result)


print(expressionAddOperator('232', 8))
