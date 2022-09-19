"""
Print the nth fibonacci number.
Ex: 0, 1, 1, 2, 3, 5, 8, 13...
The 6th fibonacci number is 5.

"""


# Recursive Solution
def getNthFibRecursive(n):
    # Time = Space = O(n)
    # This is a top down approach.
    # Using cache to avoid duplicate computation.
    cache = {}
    return solve(n, cache)


def solve(n, cache):
    # If we have the nth fibonacci number in the cache, we return it.
    if cache.get(n, None):
        return cache[n]
    # If n is 1 or 2, we return it.
    if n == 1:
        return 0
    if n == 2:
        return 1
    # Nth fibonacci number is the sum of previous two fibonacci numbers which are n-1 and n-2.
    curr_sum = solve(n - 1, cache) + solve(n - 2, cache)
    # We store the result in the cache for future use.
    cache[n] = curr_sum
    # Return the result
    return curr_sum


# Iterative Solution.

def getNthFibIterative(n):
    # Time: O(n) and Space: O(1)
    # This is a bottom-up solution.
    first = 0
    second = 1
    result = 0
    if n == 1:
        return first
    if n == 2:
        return second
    # We start the loop from 3 because we already have the result for first two numbers.
    # We go till n + 1 because we want the nth fibonacci number inclusive.
    for i in range(3, n + 1):
        # Simple logic where next number is the sum of the previous two, and update of pointers.
        result = first + second
        first = second
        second = result

    return result
