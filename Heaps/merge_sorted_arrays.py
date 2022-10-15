"""
Write a function that takes in a non-empty list of non-empty sorted arrays of integers and returns a merged list of
all of those arrays.
The integers in the merged list should be in sorted order.

Input:
arrays = [
            [1, 5, 9, 21],
            [-1, 0],
            [-124, 81, 121],
            [3, 6, 12, 20, 150],
        ]

Output: [-124, -1, 0, 1, 3, 5, 6, 9, 12, 20, 21, 81, 121, 150]
"""


def mergeSortedArrays(arrays):
    # Time: O(nlog(k) + k) and Space: O(n + k), where k is the number of subarrays and n is the total number of items.
    """
    Logic:
    We will first store the first element of all the sub arrays in a min heap.
    Now we will use a while-loop where we will pop the minimum element from the min heap, add it to the result, and
    then again insert the next element of that subarray into the min heap.
    If there is no next element for a given subarray, we will simply skip and continue the loop.
    """
    # Stores the result in sorted order
    sortedList = []
    # Stores all the first smallest elements of all subarrays.
    smallestItems = []
    # For each row, we will store the subarray's index, element index and the element value.
    for row in range(len(arrays)):
        smallestItems.append({"arrayIdx": row, "elementIdx": 0, "num": arrays[row][0]})

    # We will construct a min heap using the above dictionary, where we will use the "num" key as the min heap value.
    minHeap = MinHeap(smallestItems)
    # Until there is element in the min heap.
    while not minHeap.isEmpty():
        # Pop the top element from the min heap
        smallestItem = minHeap.remove()
        # Read all its dictionary properties
        arrayIdx, elementIdx, num = smallestItem['arrayIdx'], smallestItem['elementIdx'], smallestItem['num']
        # Add the value to the result.
        sortedList.append(num)

        # Now if the current element is the last element of the subarray, we will skip it.
        if elementIdx == len(arrays[arrayIdx]) - 1:
            continue
        # Else, we will add the next element of the subarray to the min heap.
        minHeap.insert({"arrayIdx": arrayIdx, "elementIdx": elementIdx + 1, "num": arrays[arrayIdx][elementIdx + 1]})

    return sortedList


class MinHeap:
    def __init__(self, arr):
        pass

    def insert(self, val):
        pass

    def remove(self):
        pass

    def isEmpty(self):
        pass
