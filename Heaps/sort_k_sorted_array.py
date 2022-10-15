"""
Write a function that takes in a non-negative integer k and a k-sorted array of integers and returns the sorted
version of the array. Your function can either sort the array in place or create entirely new array.
A k-sorted array is a partially sorted array in which all elements are at most k positions away from their sorted
position.
input = [3, 2, 1, 5, 4, 7, 6, 5]
k = 3

Output: [1, 2, 3, 4, 5, 5, 6, 7]
"""


def sortKSortedArray(array, k):
    # Time: O(nlog(k)) and Space: O(k)
    """
    Logic:
    Since every element is at most k positions away from its sorted position, we will maintain a min heap which will
    store k elements at any given time, and so the next smallest element will be the top value of the min heap.
    As we visit a new element, we will first pop the current min heap element and add it to the result, then add
    this new element to the min heap, this will always ensure we are having only k elements in the min heap.
    """
    # Creating a min heap with the first k elements.
    minHeap = MinHeap(array[: min(k + 1, len(array))])
    # The index to insert the correct element.
    idxToInsert = 0
    # For each element
    for i in range(k + 1, len(array)):
        # Popping the top heap element
        minElement = minHeap.remove()
        # Adding it the index
        array[idxToInsert] = minElement
        # Moving the index.
        idxToInsert += 1

        # Getting the current element
        currElement = array[i]
        # Inserting the element into the min heap.
        minHeap.insert(currElement)

    # If the min heap is not empty, we will keep popping and adding the element to the array.
    while not minHeap.isEmpty():
        minElement = minHeap.remove()
        array[idxToInsert] = minElement
        idxToInsert += 1

    return array


class MinHeap:
    def __init__(self, arr):
        pass

    def insert(self, val):
        pass

    def remove(self):
        pass

    def isEmpty(self):
        pass
