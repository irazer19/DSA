"""
You're given three inputs, all of which are instances of an AncestralTree class that have an ancestor property pointing
to their youngest ancestor. The first input is the top ancestor in an ancestral tree, and the other two inputs are
descendants in the ancestral tree.
Write a function that returns the youngest common ancestor to the two descendants.

Note that a descendant is considered its own ancestor.

     A
    / \
   B   C
  /
 D

For the above, let's say, topAncestor = A, descendantOne = C and descendantTwo = D.
So the youngest common ancestor of C & D is A.
"""


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Time: O(d) and Space: O(1), where d = depth of the ancestral tree.
    """
    Logic: First we get the heights of both the descendants from the topAncestor, and then check which descendant is
    has more depth/height. Let's say descendantOne has greater depth/height, then we will bring the
    descendantOne upto the same depth/height as descendantTwo.
    Once both the descendantOne and descendantTwo are at the same depth/height, we will move up both the
    descendants at the same time until we find a common ancestor (descendantOne == descendantTwo) .
    """

    # Getting the heights of the descendants.
    heightOne = getHeight(topAncestor, descendantOne)
    heightTwo = getHeight(topAncestor, descendantTwo)

    # Compare the heights, and bring the descendant with greater height to the same level as the other one.
    if heightOne < heightTwo:
        # Bring up the descendant two
        descendantTwo = levelUp(descendantTwo, heightTwo - heightOne)
    elif heightOne > heightTwo:
        # Bring up the descendant one
        descendantOne = levelUp(descendantOne, heightOne - heightTwo)

    # Now keep moving up until we find a common ancestor.
    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor

    # Return any descendant as the common ancestor.
    return descendantOne


def levelUp(node, levelUpBy):
    # Function to bring the greater height descendant up.
    # levelUpBy = height difference between the two descendants. Keep moving up until the difference is 0.
    while levelUpBy > 0:
        node = node.ancestor
        levelUpBy -= 1
    return node


def getHeight(top, node):
    # Function to get the height of the descendants.
    # We start counting the height from the bottom and move all the way to the topAncestor.
    height = 0
    while node != top:
        node = node.ancestor
        height += 1

    return height
