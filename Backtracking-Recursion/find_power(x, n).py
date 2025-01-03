"""
Given x and n, find the power of x^n.

https://leetcode.com/problems/powx-n/description/

Brute force:
Loop n times, and keep multiplying the result with x.
Time: O(n) and Space: O(1)

Optimized:
The idea is to find the power of one half of the given n, and multiply the result with itself because
the other half is symmetric.
Ex: For 3^4, we have n = 4, here one half is 3^2 and other half is 3^2,
now we will calculate the result for one half 3^2 = 9 and then multiply the result with itself,
9 x 9 = 81, because the other half is symmetric.

If n is odd, then we multiply the result with one more x.
Time = Space = O(log(n))
"""


def myPow(x: float, n: int) -> float:
    # Handling the case where n is < 0.
    # Whether n is +ve or -ve, we first find the result using +ve n only.
    result = calculate(x, n if n > 0 else n * -1)
    # For negative powers, we simply return the reciprocal of the result.
    if n < 0:
        return 1 / result
    return result


def calculate(x, n):
    # Edge cases
    if x == 0:
        return 0

    if n == 0:
        return 1
    # Base case for the recursion.
    if n == 1:
        return x

    # Calculating the one half of the result
    result = calculate(x, n // 2)
    # Multiplying the result with itself because the second half is symmetric.
    result *= result

    # If n is odd, then we multiply the result with x.
    if n % 2 != 0:
        result = result * x

    return result


print(myPow(3, 4))
