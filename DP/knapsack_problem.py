"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the
maximum total value in the knapsack.

"""


def knapsackProblem(items, capacity):
    # Time = Space = O(n x c), n items and c capacity.

    # Using DP, create a matrix of rows=items and columns=capacity.
    # Each cell represents: The max value using i items with c capacity.
    store = [[0 for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    # Filling the matrix starting from capacity 1
    for i in range(1, len(store)):
        for j in range(1, len(store[0])):
            # We can add the current item only if the items weight is <= current capacity.
            if j >= items[i - 1][1]:
                # We have two options, either to add the item or skip the item.
                # And we consider the max of both of them, since we want to maximize the value.
                store[i][j] = max(store[i - 1][j], items[i - 1][0] + store[i - 1][j - items[i - 1][1]])
            else:
                # Else, since we cannot add this item, the max value is whatever the previous top value.
                store[i][j] = store[i - 1][j]

    # We can build the full sequence along with the max value result.
    return [store[-1][-1], build_sequence(store, items)]


def build_sequence(store, items):
    # We start from the bottom right corner of the matrix.
    row = len(store) - 1
    col = len(store[0]) - 1
    seq = []  # Stores the sequence

    # If we reach the first row/col then we break because it represents 0 capacity/0 items.
    while row > 0 and col > 0:
        # If the current value in the store is same the value above it, then we know that we did not add
        # this item. So we move the row up.
        if store[row][col] == store[row - 1][col]:
            row -= 1
        else:
            # Else, we have added the item. And so we move to the top row.
            # And the column is the remainder of current capacity - current items weight.
            seq.append(row - 1)
            col = col - items[row - 1][1]  # current capacity - current items weight.
            row -= 1
    # Reverse the sequence because we started from bottom
    return list(reversed(seq))


print(knapsackProblem([
    [1, 2],
    [4, 3],
    [5, 6],
    [6, 7]
], 10))
