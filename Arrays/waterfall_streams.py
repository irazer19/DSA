"""
You're given a two-dimensional array that represents the structure of an indoor waterfall and a positive integer that
represents the column that the waterfall's water source will start at. More specifically, the water source will start
directly above the structure and will flow downwards.

Each row in the array contains Cs and 1 s, where a represents a free space and a 1 represents a block that water can't
pass through. You can imagine that the last row of the array contains buckets that the water will eventually flow into;
thus, the last row of the array will always contain only @s. You can also imagine that there are walls on both sides
of the structure, meaning that water will never leave the structure; it will either be trapped against a wall or flow
into one of the buckets in the last row.

As water flows downwards, if it hits a block, it splits evenly to the left and right-hand side of that block. In other
words, 50% of the water flows left and 50% of it flows right. If a water stream is unable to flow to the left or to
the right (because of a block or a wall), the water stream in question becomes trapped and can no longer continue to
flow in that direction; it effectively gets stuck in the structure and can no longer flow downwards, meaning that
50% of the previous water stream is forever lost.

Lastly, the input array will always contain at least two rows and one column, and the space directly below the water
source (in the first row of the array) will always be empty, allowing the water to start flowing downwards.

Write a function that returns the percentage of water inside each of the bottom buckets after the water has flowed
through the entire structure.

array = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]
source = 3
expected = [0, 0, 0, 25, 25, 0, 0]

"""


def waterfallStreams(array, source):
    # Time: O(w^2 * h) and Space: O(w), h is the height and w is the width.
    """
    Logic:
    We will maintain two rows always:
    1. Current Row
    2. Row above, which is the row above the current row.

    We will iterate over the rowAbove and check for water or if there is a block in the current row.
    We will also split the water if the rowAbove contains water but the current row is a block.
    To split the water, we will move to the left of the current idx and right of the current idx, until
    the water can freely flow (no block in the current idx row).
    """
    # Making a copy of the row above.
    rowAbove = array[0][:]
    # Marking the source of the water at the given position.
    rowAbove[source] = -1

    # We will start iterating from index 1 because that is the current row as we are using the first row as rowAbove.
    for row in range(1, len(array)):
        # Copy of the current row
        currentRow = array[row][:]
        # Iterating over the column of the rowAbove. We will compare rowAbove and currentRow.
        for idx in range(len(rowAbove)):
            # Getting the value of the above row
            valueAbove = rowAbove[idx]
            # Whether the above row has water
            hasWaterAbove = valueAbove < 0
            # Whether the current idx has a blocker
            hasBlock = currentRow[idx] == 1

            # If the row above has not water, then we continue to next column.
            if not hasWaterAbove:
                continue
            # If the current idx does not have a blocker, then we simply move the water down to that idx.
            if not hasBlock:
                currentRow[idx] += valueAbove
                continue
            # At this point we have a blocker at the current row idx.
            # Splitting the water into two halves
            splitWater = valueAbove / 2
            # Move water to right
            # We will keep moving until the current row idx has no block
            rightIdx = idx + 1
            while rightIdx < len(rowAbove):
                # If the row above itself has a block, then the water is trapped and we lost it forever.
                if rowAbove[rightIdx] == 1:
                    break
                # If the current idx has no block, then we can move the split water down.
                if currentRow[rightIdx] != 1:
                    currentRow[rightIdx] += splitWater
                    break
                # Else we keep moving to the right
                rightIdx += 1
            # Move water to the left
            leftIdx = idx - 1
            while leftIdx >= 0:
                # If the left idx of the row above itself has a block, then we are stuck.
                if rowAbove[leftIdx] == 1:
                    break
                # If the current row's idx has no block here, then we can move the water down.
                if currentRow[leftIdx] != 1:
                    currentRow[leftIdx] += splitWater
                    break
                # Else keep moving to left.
                leftIdx -= 1
        # At this point, we will move to the next currentRow in the for loop, so before that we update the new
        # rowAbove which is the currentRow.
        rowAbove = currentRow
    # Final answer by converting the split water values to percentage values.
    finalPercentagOfWater = list(map(lambda num: num * -100, rowAbove))
    return finalPercentagOfWater
