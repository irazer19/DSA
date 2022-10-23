"""
Find the Greatest Common Divisor (GCD) between two given numbers.

Input: num1=3, num2=6
Output: 3

"""


def findGCD(num1, num2):
    """
    Logic:
    Euclidean Algorithm is used in solving this efficiently.
    """
    while True:
        # Base Case
        if num1 == 0:
            return num2
        if num2 == 0:
            return num1
        # num1 becomes num2, and num2 =  remainder of num1 and num2
        num1, num2 = num2, num1 % num2


print(findGCD(98, 56))
