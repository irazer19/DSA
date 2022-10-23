"""
You're given an array of points plotted on a 2D graph (the xy-plane). Write a function that returns the maximum number
of points that a single line (or potentially multiple lines) on the graph passes through.
The input array will contain points represented by an array of two integers [x, y] . The input array will never contain
duplicate points and will always contain at least one point.

input = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]
expected = 4
"""


def lineThroughPoints(points):
    # Time: O(n^2) and Space: O(n)
    """
    Logic:
    For each point, we will compare it against other points. We will compute the slope between the two points,
    and add the slope value in the dictionary as key and the number of points having the same slope as value.
    We will extract the maximum number of points which share the common slope from a common point.
    Hashing the slope is the problem, we cannot hash it in float because for large decimals, it will auto-round
    the value and give erroneous result.
    Instead, we will store the slope in fraction format reduced to the smallest value possible by dividing the
    numerator and denominator using the GCD.

    """
    # Result
    maxNumberOfPointsOnLine = 1

    # For each point as p1
    for idx1, p1 in enumerate(points):
        # Storing all the slopes between points p1 and p2.
        slopes = {}
        # For each points p2, we will start the index after p1 to counter duplicate computation.
        for idx2 in range(idx1 + 1, len(points)):
            # Point p2
            p2 = points[idx2]
            # Getting the slope, rise = y1 - y2 and run = x1 - x2
            rise, run = getSlopeOfLineBetweenPoints(p1, p2)
            # Hashing the slope
            slopeKey = createHashableKey(rise, run)
            # Storing the slope in the dictionary, we initialize with 1 because the line passes through the current
            # point p1.
            if slopeKey not in slopes:
                slopes[slopeKey] = 1
            # Updating the points count having the same slope.
            slopes[slopeKey] += 1
        # Updating the result
        maxNumberOfPointsOnLine = max(maxNumberOfPointsOnLine, max(slopes.values(), default=0))

    return maxNumberOfPointsOnLine


def getSlopeOfLineBetweenPoints(p1, p2):
    # Extracting the coordinates
    p1x, p1y = p1
    p2x, p2y = p2
    # Slope of a vertical line
    slope = [1, 0]

    # If line is not vertical
    if p1x != p2x:
        # Slope denominator
        xDiff = p1x - p2x
        # Slope numerator
        yDiff = p1y - p2y
        # Finding the GCD for reducing the fraction in the smallest form.
        gcd = getGreatestCommonDivisor(abs(xDiff), abs(yDiff))
        xDiff = xDiff // gcd
        yDiff = yDiff // gcd
        # If the denominator is negative then we convert it to positive, and make the numerator negative instead.
        if xDiff < 0:
            xDiff *= -1
            yDiff *= -1
        # Slope
        slope = [yDiff, xDiff]
    return slope


def createHashableKey(numerator, denominator):
    # Hashing the slope
    return str(numerator) + ':' + str(denominator)


def getGreatestCommonDivisor(num1, num2):
    a = num1
    b = num2
    while True:
        if a == 0:
            return b
        if b == 0:
            return a
        a, b = b, a % b
