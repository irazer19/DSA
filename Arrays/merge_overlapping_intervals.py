"""
Write a function that takes in a non-empty array of arbitrary intervals, merges any overlapping intervals, and returns
the new intervals in no particular order.

intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
expected = [[1, 2], [3, 8], [9, 10]]

"""


def mergeOverlappingIntervals(intervals):
    # Time: O(nlogn) and Space: O(n)
    """
    Logic:
    First we sort the intervals by start time. Then for each interval, we will compare it with the previous
    result interval, if its can be merged, then we merge and update the previous result interval, else
    add the current interval to the result.
    """
    # Sorting the intervals by start time.
    intervals = sorted(intervals, key=lambda x: x[0])
    # Storing the result, since we compare with the previous result interval, we add the first element to the result.
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        # Getting the current interval
        currInterval = intervals[i]
        # Getting the previous result interval
        prevInterval = result[-1]
        # Getting start and end time of each interval
        currStart, currEnd = currInterval
        prevStart, prevEnd = prevInterval
        # If the previous result interval's end time > current intervals start time, they are overlapping.
        if prevEnd >= currStart:
            # New merged interval
            newInterval = [prevStart, max(prevEnd, currEnd)]
            # Updating the previous result interval
            result[-1] = newInterval
        else:
            # If no overlapping, then we just add the current interval to the result
            result.append(currInterval)
    return result
