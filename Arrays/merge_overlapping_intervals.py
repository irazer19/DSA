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
    First we sort the intervals by start time. Then for each interval, we will compare it with i+1 intervals until
    they can be merged. Once the current and next intervals cannot be merged, we will store the current interval
    to the result and move to the next interval.
    """
    # Sorting the intervals by start time.
    intervals = sorted(intervals, key=lambda x: x[0])
    # Storing the result
    result = []
    # Starting index
    currIdx = 0
    # Until we have finished all the intervals
    # We skip the last interval because it does not have any interval next to it for comparison.
    while currIdx < len(intervals) - 1:
        # Storing the current interval in this variable
        currInterval = [intervals[currIdx][0], intervals[currIdx][1]]
        # We start comparing the current interval with the next interval
        currIdx = currIdx + 1
        # Until the next interval is valid, and the end time of current interval is greater or equal to the
        # start time of the next interval
        while currIdx < len(intervals) and currInterval[1] >= intervals[currIdx][0]:
            # Since we have sorted it by start time, the start time will remain the same
            currInterval[0] = currInterval[0]
            # The end time will be updated which is the max of either the current interval or the next interval's
            # end time.
            currInterval[1] = max(currInterval[1], intervals[currIdx][1])
            # Moving to the next interval.
            currIdx += 1
        # Storing the current interval to the result
        result.append(currInterval)
    # Finally, once we are out of the loop, if the idx is still pointing to the next interval, we append it
    # to the result.
    if currIdx == len(intervals) - 1:
        result.append(intervals[currIdx])
    return result
