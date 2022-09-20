"""
Write a function that takes in an array of unique integers and returns its powerset.

Input: [1, 2, 3]

Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

"""


def powerset(array):
    # Time = Space = O(n * 2^n)
    """
    Logic: For each item we append that item to every resultant list, and the output is again stored in the
    resultant array.
    """
    # Resultant array
    result = [[]]
    # For every item
    for item in array:
        # Going through each result list.
        for i in range(len(result)):
            # We append the item to the already existing result list one by one.
            curr = result[i] + [item]
            # And then again append the new list to the result array.
            result.append(curr)

    return result


print(powerset([1, 2, 3]))
