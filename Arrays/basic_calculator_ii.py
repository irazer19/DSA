"""
Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero. You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Input: s = "3+2*2"
Output: 7

https://leetcode.com/problems/basic-calculator-ii/description/

"""


def calculate(s: str) -> int:
    # Time: O(n) and Space: O(1)
    """
    Brute force:
    Process the string character by character and follow the standard order of operations (multiply/divide first, then add/subtract)
    We use a stack to store the processed number.
    Time: O(n) and Space: O(n)

    Optimized:
    The code processes the expression by scanning each character one by one. As it reads digits, it builds them into a complete number
    (curr_num). When it encounters an operator or reaches the end of the string, it performs the previous operation stored in op.

    """
    s = s.strip()
    # To store the final result as we move.
    currSum = 0
    # Stores the previous number encountered
    prev = 0
    # Starting operator
    op = "+"
    # Store the current number at hand
    curr_num = 0

    for i in range(len(s)):
        # If the current char is a digit.
        if s[i].isdigit():
            curr_num = curr_num * 10 + int(s[i])
        if s[i] in ["+", "-", "*", "/"] or i == len(s) - 1:
            if op == "+":
                currSum += curr_num
                prev = curr_num
            elif op == "-":
                currSum -= curr_num
                prev = -curr_num
            elif op == "*":
                currSum -= prev
                currSum += curr_num * prev
                prev = curr_num * prev
            elif op == "/":
                currSum -= prev
                currSum += int(prev / curr_num)
                prev = int(prev / curr_num)
            op = s[i]
            curr_num = 0
    return currSum
