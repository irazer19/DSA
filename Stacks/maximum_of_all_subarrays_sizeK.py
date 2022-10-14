"""
Given an array and an integer K, find the maximum for each and every contiguous subarray of size K.

Input: arr[] = {1, 2, 3, 1, 4, 5, 2, 3, 6}, K = 3
Output: 3 3 4 5 5 5 6
Explanation: Maximum of 1, 2, 3 is 3
                       Maximum of 2, 3, 1 is 3
                       Maximum of 3, 1, 4 is 4
                       Maximum of 1, 4, 5 is 5
                       Maximum of 4, 5, 2 is 5
                       Maximum of 5, 2, 3 is 5
                       Maximum of 2, 3, 6 is 6

"""


def maximumOfAllSubarraysSizeK(arr, k):
    # Time: O(n) and Space: O(k)
    """
    Logic:
    We maintain a dequeue for storing the k elements at any moment in time in descending order, meaning the
    0th index will have the max value.
    We will slide through the array with a window size of k using start and end pointers.
    At every slide, we will check whether the current 0th element in the deq is out of range for the current window
    size, and whether the last inserted deq element is smaller than the current new element.

    """
    # Doubly ended queue.
    deq = []
    # Handling the first k elements manually inside a function.
    traverseFirstk(arr, k, deq)
    # Storing the max element from the first k elements in the result.
    result = [arr[deq[0]]]
    # The second window starts from index 1 and ends at index k.
    start = 1
    end = k
    # While loop until the end index is out of range.
    while end < len(arr):
        # If the current starting window index has crossed the elements index at the 0th position of deq.
        # then we pop that element because its out of range for the current window.
        if start > deq[0]:
            deq.pop(0)
        # Now if the current element is greater than the last inserted element in the deq, then we dont need those
        # elements so we pop them.
        while deq and arr[end] > arr[deq[-1]]:
            deq.pop()
        # Finally, we know add the current element index to the deq.
        deq.append(end)
        # Now whatever is the at the 0th index is the having the largest value for the current window size.
        # so we add it to the result.
        result.append(arr[deq[0]])
        # Moving the window
        start += 1
        end += 1

    return result


def traverseFirstk(arr, k, deq):
    # Looping first k elements.
    for i in range(k):
        # If deq has elements, and the last inserted deq element is smaller than the current element,
        # then we simply pop it because we store the elements in descending order.
        while deq and arr[deq[-1]] < arr[i]:
            deq.pop()
        deq.append(i)


print(maximumOfAllSubarraysSizeK([11, 3, 9, 6], 3))
