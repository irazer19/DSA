"""
You're given a list of time intervals during which students at a school need a laptop. These time intervals are
represented by pairs of integers [start, end], where 0 <= start < end . However, start and end don't represent real
times: therefore, they may be greater than 24
No two students can use a laptop at the same time, but immediately after a student is done using a laptop, another
student can use that! same laptop. For example, if one student rents a laptop during the time interval [0, 2] ,
another student can rent the same laptop during any time interval starting with 2.
Write a function that returns the minimum number of laptops that the school needs to rent such that all students will
always have access! to a laptop when they need one.

times = [
          [0, 2],
          [1, 4],
          [4, 6],
          [0, 4],
          [7, 8],
          [9, 11],
          [3, 10]
        ]
Output: 3

https://leetcode.com/problems/meeting-rooms-ii/description/
"""


def laptopRentals(times):
    # Time: O(nlog(n)) and Space: O(n)
    """
    Logic:
    Split the start and end times into two arrays. Now iterate through the start and end times using pointers,
    If the start time >= end time, it means that one student has already finished using a laptop and another student
    needs it.
    Else if the start time < end time, it means that we need a new laptop.

    """

    # Splitting the start and end times into two arrays and sorting them,
    startTime = sorted([item[0] for item in times])
    endTime = sorted([item[1] for item in times])

    # Result
    usedLaptops = 0
    # Starting index for start and end times for iteration.
    startIdx = 0
    endIdx = 0
    # Iterate until we have a start time.
    while startIdx < len(times):
        # If the start time >= end time, we reduce the used laptop count because a student has finished using it.
        if startTime[startIdx] >= endTime[endIdx]:
            usedLaptops -= 1
            # We also increase the end time to get the next finish time.
            endIdx += 1
        # We always increment the used laptop count because we have a student who needs a laptop at the current
        # start time.
        usedLaptops += 1
        # Moving to the next start time.
        startIdx += 1

    return usedLaptops
