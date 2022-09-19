"""
Find all the permutations of the given list of elements.

Input: [1, 2, 3]

Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

"""


def getPermutations(array):
    # Time = Space = O(n*n!)
    """
    Logic:
    We swap each element with every other element, and after the swap, we again call the function with the next
    index as the position to swap with all other elements after it. Once the function returns, we undo the swap
    to find the next configuration of the elements.

    When we reach the last element, then we cannot swap it with anything, so we add the current array configuration
    to the final result array and return.

    """

    # Edge case.
    if not array:
        return []

    # Stores the permutations.
    result = []
    # Main recursion call, where the start index is 0.
    solve(array, 0, result)

    return result


def solve(array, start_idx, result):
    # The start index is the index element which is swapped with all other elements after it one by one to make
    # different configuration.
    # If the start index is the last element, then we append the result and return.
    if start_idx == len(array) - 1:
        result.append(array[:])
        return

    # We swap the start_idx element with every element in the array which comes after it.
    for i in range(start_idx, len(array)):
        # Swap with the next element in the loop.
        swap(i, start_idx, array)
        # After the swap, we move to the next position, which is start_idx + 1 and again try to find a new
        # configuration.
        solve(array, start_idx + 1, result)
        # After we have added all the permutations to the result after the current start index and ith index was
        # swapped, we undo the swap and restore the original order.
        swap(i, start_idx, array)


def swap(i, start_idx, array):
    array[i], array[start_idx] = array[start_idx], array[i]


print(getPermutations([1, 2, 3]))
