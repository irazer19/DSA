"""
Heap sort.

"""


def heapSort(array):
	# Time: O(nlogn) and Space: O(1)
	"""
	Logic:
	First we will build a max heap using the given array.
	We know that the first element of the heap will have the max value, so we swap that with the end index of the heap,
	and then siftDown the 0th element till the end index of the heap.
	The end index of the heap will change as we keep swapping elements and place them in their correct place.
	As we progress, the heap size will decrease and the sorted array will size will increase.
	"""
	# Building the max heap.
	heap = buildMaxHeap(array)
	# This is the index where we will place the sorted element, and this index also marks the end index of the heap.
	rightIdx = len(heap) - 1
	# We will not iterate till the first index because that is the only element which by default should be in the
	# correct position
	while rightIdx > 0:
		# Swapping the 0th element of the max heap with the end index of the heap.
		swap(0, rightIdx, heap)
		# Reducing the size of the heap, as the end index already has the correct element.
		rightIdx -= 1
		# Moving down the 0th element which was newly swapped to its correct heap position.
		siftDown(0, rightIdx, heap)
	return heap


def buildMaxHeap(array):
	firstParent = (len(array) - 2) // 2
	for currIdx in range(firstParent, -1, -1):
		siftDown(currIdx, len(array) - 1, array)
	return array


def siftDown(currIdx, endIdx, heap):
	childOneIdx = (currIdx * 2) + 1
	while childOneIdx <= endIdx:
		childTwoIdx = (currIdx * 2) + 2 if (currIdx * 2) + 2 <= endIdx else -1
		if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]:
			idxToSwap = childTwoIdx
		else:
			idxToSwap = childOneIdx
		if heap[idxToSwap] > heap[currIdx]:
			swap(idxToSwap, currIdx, heap)
			currIdx = idxToSwap
			childOneIdx = (currIdx * 2) + 1
		else:
			break


def swap(i, j, heap):
	heap[i], heap[j] = heap[j], heap[i]
