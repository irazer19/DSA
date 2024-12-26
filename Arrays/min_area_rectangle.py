"""
You're given an array of points plotted on a 2D graph (the xy-plane). Write a function that returns the minimum area
of any rectangle that can be formed using any 4 of these points such that the rectangle's sides are parallel to the x
and y axes (i.e., only rectangles with horizontal and vertical sides should be considered--no rectangles with diagonal
sides). If no rectangle can be formed your function! should return o.
The input array will contain points represented by arrays of two integers (x, y] .
The input array will never contain duplicate points.

input = [[1, 5], [5, 1], [4, 2], [2, 4], [2, 2], [1, 2], [4, 5], [2, 5], [-1, -2]]
expected = 3

https://leetcode.com/problems/minimum-area-rectangle/description/

"""


def minimumAreaRectangle(points):
    # Time: O(n^2) and Space: O(n)
    """
    Logic:
    We treat every coordinate as the bottom left coordinate of a rectangle, then again iterate over the points to
    and find the coordinates which can become the top right coordinate of the rectangle, if such a coordinate exists
    then we can derive the top left and bottom right coordinates, and check whether they are present in the
    input coordinates. If yes, then we calculate the X, Y and update the area of the rectangle.
    """
    # Storing the coordinates in a hastable
    getCoord = {tuple(c): True for c in points}
    # Result
    minArea = float("inf")
    # For every coordinate, this is the bottom left coordinate of the rectangle
    for bottomLeftPoint in points:
        # For ever top right coordinate
        for topRightPoint in points:
            # If the top right coordinate is valid
            if (
                topRightPoint[0] > bottomLeftPoint[0]
                and topRightPoint[1] > bottomLeftPoint[1]
            ):
                # Deriving the top left and bottom right coordinates
                topLeftPoint = [bottomLeftPoint[0], topRightPoint[1]]
                bottomRightPoint = [topRightPoint[0], bottomLeftPoint[1]]
                # If both the derived coordinates are present in the hastable
                if (
                    tuple(topLeftPoint) in getCoord
                    and tuple(bottomRightPoint) in getCoord
                ):
                    # Computing the X, Y of the rectangle
                    x = bottomRightPoint[0] - bottomLeftPoint[0]
                    y = topLeftPoint[1] - bottomLeftPoint[1]
                    # Updating the min area result.
                    minArea = min(minArea, x * y)
    return minArea if minArea != float("inf") else 0
