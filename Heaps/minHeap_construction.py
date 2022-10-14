# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Time: O(n) and Space: O(1)
        """
        Logic:
        We get the first parent from the end of the array, and the call siftDown method on that it, and
        repeat this for all the parents.
        """
        firstParentIdx = (len(array) - 2) // 2
        for currIdx in range(firstParentIdx, -1, -1):
            self.siftDown(currIdx, len(array) - 1, array)

        return array

    def siftDown(self, currIdx, end_idx, heap):
        # Time: O(logn) and Space: O(1)
        """
        Logic:
        We want to move the current idx element to the right position in the min heap.
        We first get the first child, and then the second child, now the second child may not exist if its index
        is out of bounds. For this min heap, we will swap the current element with the child having the smaller value.
        We will keep repeating the above process until the current element's children are greater than it or
        there are no more children for the current element.
        """
        childOneIdx = (2 * currIdx) + 1
        while childOneIdx < len(heap):
            childTwoIdx = (2 * currIdx) + 2
            # Checking whether childTwoIdx exists.
            childTwoIdx = childTwoIdx if childTwoIdx < len(heap) else -1
            # Condition to swap the current element with the child two.
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                # Else we swap with child one
                idxToSwap = childOneIdx
            # We do the swap only if the current element if greater than the child to swap.
            if heap[idxToSwap] < heap[currIdx]:
                self.swap(idxToSwap, currIdx, heap)
                # Moving the current index
                currIdx = idxToSwap
                # Getting the child one
                childOneIdx = (2 * currIdx) + 1
            else:
                # At this point the current element is already at the correct position, so we break
                return

    def siftUp(self, currIdx, heap):
        # Time: O(logn) and Space: O(1)
        """
        Logic:
        We want to move the element up till we find its correct position.
        We will get the parent of the element, and then compare the value, in case of min heap, if the parent
        is greater than the current element, then we swap, else break
        """
        parentIdx = (currIdx - 1) // 2
        # Condition to repeat the process of swapping and moving up for min heap.
        while currIdx > 0 and heap[parentIdx] > heap[currIdx]:
            self.swap(currIdx, parentIdx, self.heap)
            # Updating the current idx
            currIdx = parentIdx
            # Getting its parent again.
            parentIdx = (currIdx - 1) // 2

    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Time: O(logn) and Space: O(1)
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        # Time: O(logn) and Space: O(1)
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
