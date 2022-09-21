"""

Input:
    cups = [[200, 210], [450, 465], [800, 850]]
    low = 2100
    high = 2300

Output:

    true
    // We use cup [450, 465] to measure four volumes:
    // First measurement: Low = 450, High = 465
    // Second measurement: Low = 450 + 450 = 900, High = 465 + 465 = 930
    // Third measurement: Low = 900 + 450 = 1350, High = 930 + 465 = 1395
    // Fourth measurement: Low = 1350 + 450 = 1800, High = 1395 + 465 = 1860
    // Then we use cup [200, 210] to measure two volumes:
    // Fifth measurement: Low = 1800 + 200 = 2000, High = 1860 + 210 = 2070
    // Sixth measurement: Low = 2000 + 200 = 2200, High = 2070 + 210 = 2280
    // We've measured a volume in the range [2200, 2280] -
    // This is within our target range, so we return "true".
    // Note: there are other ways to measure a volume in the target range.

"""


def ambiguousMeasurements(measuringCups, low, high):
    # Time: O(low * high * n) and Space: O(low * high), where n is the number of measuring cups.
    """
    Logic:
    The objective is to measure the low and high using cups, mainly we want to find a cup whose cupLow and cupHigh
    is same as or between the given low and high.

    Recursively, for every cup we try, we will subtract the cup's cupLow from low and cupHigh from high, that way
    we will reduce the problem by reducing the value of low and high. Now if the value of low and high is so low
    such that there is a cup which fits between the low and high, then we return True, else if the low and high
    has gone <= 0, then its invalid, and we return False as the base case.
    We use cache to store the result of low, high which reduces the time.

    """

    # Using cache.
    cache = {}
    return canMeasureInRange(measuringCups, low, high, cache)


def canMeasureInRange(measuringCups, low, high, cache):
    # Checking in cache before computing the result for the current low and high.
    if (low, high) in cache:
        return cache[(low, high)]

    # If the low and high values are invalid, we return False
    if low <= 0 and high <= 0:
        return False

    # Variable to store the result for the current low and high.
    canMeasure = False
    # We try with every cup
    for cupLow, cupHigh in measuringCups:
        # If the cup fits between the given low and high, we mark True and break
        if low <= cupLow and high >= cupHigh:
            canMeasure = True
            break
        # Else, we use this cup, and call again with the updated low and high values.
        # If we get True, we break
        canMeasure = canMeasureInRange(measuringCups, low - cupLow, high - cupHigh, cache)
        if canMeasure:
            break
    # Finally, we store the result for the current low and high, and return the result.
    cache[(low, high)] = canMeasure
    return canMeasure
