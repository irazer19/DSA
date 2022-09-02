"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i]

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are
no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

"""


def jobScheduling(startTime, endTime, profit) -> int:
    # Time: O(n^2) and Space: O(n)
    # We will store all the startTime, endTime and profit in an array of tuples
    arr = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
    # Let's sort this array by endTime so that all the jobs endTime can be compared in sequence.
    # It's because we dont want overlapping jobs together.
    arr.sort(key=lambda x: x[1])
    # This result array will store the maximum profit at each index
    result = [obj[2] for obj in arr]  # Since index=2 contains the profit

    # For the first job, we cannot have any overlap because it finishes first, so the max profit will be the current
    # profit. So we start the loop from index 1.
    for i in range(1, len(arr)):
        # We compare the current job with all the previous jobs
        for j in range(0, i):
            # if the previous job is not overlapping with the current job.
            if arr[j][1] <= arr[i][0]:
                # Update the max profit for the current job, either the current max profit OR the combo of
                # previous jobs profit + current jobs individual profit.
                result[i] = max(result[i], result[j] + arr[i][2])
    return max(result)


print(jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]))
