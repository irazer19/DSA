"""
Write a function that takes in a "special" array and returns its product sum.
A "special" array is a non-empty array that contains either integers or other "special" arrays. The product sum of a
"special" array is the sum of its elements, where "special" arrays inside it are summed themselves and then multiplied
by their level of depth.
The depth of a "special" array is how far nested it is. For instance, the depth of [] is 1 ; the depth of the inner
array in [[]] is 2: the depth of the innermost array in [[[]]] is 3.
Therefore, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum
of [x, [y, [z]]] is x + 2 + (y + 3z).

Sample Input:
[5, 2, [7, -1], 3, [6, [-13, 8], 4]]

Output: 12

"""


def productSum(array):
    # Time: O(n) and Space: O(d), where n is the total number of elements and d is max depth in the list.
    """
    Logic:
    We will call a function recursively, at start the depth is 1.
    We loop every element in the current list, and add to the curr_sum if it's an integer.
    If an element is a list, then we again call the function by passing this list as the array with depth+1.
    We return the current sum * depth as the output of the current array.

    """

    # Empty array has a product sum of 0
    if not array:
        return 0
    # Final out from the recursion. Using depth = 1
    return solve(array, 1)


def solve(array, depth):
    # Current sum is the product sum for the current array.
    curr_sum = 0
    # For every element in the array we check whether it's an integer or list.
    for n in array:
        # If list
        if type(n) == list:
            # Call the function by passing the current list as the array, with +1 depth.
            curr_sum += solve(n, depth + 1)
        else:  # If integer
            curr_sum += n
    # The current sum is return by multiplying with its depth.
    return depth * curr_sum
