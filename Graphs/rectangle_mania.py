"""
Write a function that takes in a list of cartesian coordinates and returns the number of rectangles formed by these
coordinates.
We only care about rectangles with sides parallel to the x and y axes.

Ex: coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
Output: 6

"""


def rectangleMania(coords):
    # Time: O(n^2) and Space: O(n)
    """
    Logic: We assume every coordinate as a bottom-left corner of the rectangle, and then we again loop every
    coordinate and check whether it can be a top-right corner of the rectangle,
    If yes, then we try to find whether we have the top-left and bottom-right corner of the rectangle in the
    hash table of coordinates, if yes, then we increase the result counter +1, else ignore it.

    """

    # Creating a hash table of coordinates
    coordTable = getCoordTable(coords)
    result = 0  # Stores the result

    # Treating each coord as a bottom left corner of the rectangle.
    for x1, y1 in coords:
        # Finding the top-right corner of the rectangle.
        for x2, y2 in coords:
            # If x2, y2 are top-right corner of the rectangle
            if isUpperRight(x1, y1, x2, y2):
                # Now we make a rectangle, we check whether we have the top-left & bottom-right corner of the rectangle
                # in the hash table..
                topLeft = coordTable.get((x1, y2), False)
                bottomRight = coordTable.get((x2, y1), False)
                # Only if both are present then we add +1 to the result.
                if topLeft and bottomRight:
                    result += 1

    return result


def getCoordTable(coords):
    # Storing each coordinate in the hash table
    coordTable = {}
    for x, y in coords:
        coordTable[(x, y)] = True

    return coordTable


def isUpperRight(x1, y1, x2, y2):
    # Checking for Top right coordinate.
    return x2 > x1 and y2 > y1
