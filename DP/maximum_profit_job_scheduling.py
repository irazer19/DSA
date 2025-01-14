"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i]

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are
no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
"""


# Brute Force Solution - Using Recursion
# Time Complexity: O(2^n) where n is number of jobs
# Space Complexity: O(n) for recursion stack
def jobScheduling_bruteforce(startTime, endTime, profit):
    n = len(startTime)
    # Create jobs as tuples for easier handling
    jobs = sorted(zip(startTime, endTime, profit))

    def findMaxProfit(index):
        # Base case: if no more jobs to process
        if index >= n:
            return 0

        # Get current job details
        curr_start, curr_end, curr_profit = jobs[index]

        # Option 1: Skip current job
        skip = findMaxProfit(index + 1)

        # Option 2: Take current job and find next non-overlapping job
        next_index = index + 1
        while next_index < n and jobs[next_index][0] < curr_end:
            next_index += 1

        take = curr_profit + findMaxProfit(next_index)

        # Return maximum of taking or skipping current job
        return max(skip, take)

    return findMaxProfit(0)


# Optimized Solution - Using Dynamic Programming with Binary Search
# Time Complexity: O(nlogn) where n is number of jobs
# Space Complexity: O(n)
def jobScheduling_optimized(startTime, endTime, profit):
    """Optimized Approach (Using DP with Binary Search):

    Uses dynamic programming with binary search to optimize the solution
    Key optimizations:

    Sort jobs by start time to make it easier to find non-overlapping jobs
    Use binary search to quickly find the next non-overlapping job
    Use DP array to store maximum profit for subproblems

    The dp[i] represents the maximum profit we can get from jobs[i:] onwards
    For each job, we:

    Find the next non-overlapping job using binary search
    Calculate max profit by either taking or skipping current job

    Time complexity is reduced to O(nlogn) due to sorting and binary search"""
    n = len(startTime)
    jobs = sorted(zip(startTime, endTime, profit))
    dp = [0] * (n + 1)  # dp[i] represents max profit from jobs[i:]

    def binary_search(start_index, target_time):
        left, right = start_index, n - 1
        result = n  # Default if no valid job found

        while left <= right:
            mid = (left + right) // 2
            if jobs[mid][0] >= target_time:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    # Fill dp array from right to left
    for i in range(n - 1, -1, -1):
        curr_start, curr_end, curr_profit = jobs[i]

        # Find next non-overlapping job using binary search
        next_job = binary_search(i + 1, curr_end)

        # Maximum profit by either taking or skipping current job
        dp[i] = max(
            curr_profit + dp[next_job], dp[i + 1]  # Take current job
        )  # Skip current job

    return dp[0]
