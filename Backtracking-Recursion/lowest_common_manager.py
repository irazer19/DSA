"""
You're given three inputs, all of which are instances of an OrgChart class that have a directReports property pointing
to their direct reports. The first input is the top manager in an organizational chart (i.e., the only instance that
isn't anybody else's direct report), and the other two inputs are reports in the organizational chart. The two reports
are guaranteed to be distinct.

Write a function that returns the lowest common manager to the two reports.

Input:
topManager: A
reportOne: E
reportTwo: I

         A
       /   \
      B     C
     / \   / \
    D   E  F  G
   / \
  H   I

Output: Node B
"""


def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Time: O(n) and Space: O(d), where n is the number of nodes, and d is the depth of the graph.
    """
    Logic:
    We explore the nodes using DFS starting from the topManager. For every node we explore, we initialize a
    variable called found_from_here which stores the total found nodes from the current node manager.
    After exploring all the children, we check whether the current node is one of reportOne or reportTwo, if yes
    then we update the found_from_here variable += 1.
    The return of the function is an object which has the following properties:
    found = How many reports were found with this node as the manager.
    node = The node which is the manager if total found is 2. (Because we are looking for reportOne and reportTwo nodes)
    """

    # The final result object will contain the resultant node.
    result = solve(topManager, reportOne, reportTwo)

    return result.node


def solve(node, reportOne, reportTwo):
    # Initializing found_from_here to store total found reports from the current node.
    found_from_here = 0
    # Exploring every child/report node
    for child in node.directReports:
        # The function call returns the Result class object
        result = solve(child, reportOne, reportTwo)
        # If the result object has node attribute filled, then we have found the answer, so we return.
        if result.node:
            return result
        # Else, whatever was the found from this child, we add it to the current node's "found_from_here".
        found_from_here += result.found

    # After the for loop is over, we check whether the current node itself is one of reportOne or reportTwo.
    # If yes, then we update the found_from_here.
    if node == reportOne or node == reportTwo:
        found_from_here += 1

    # Finally, we create and return the Result object:
    # If found_from_here is already 2, then we fill the node attribute else we store None.
    return (
        Result(found_from_here, node)
        if found_from_here == 2
        else Result(found_from_here, None)
    )


class Result:
    def __init__(self, found, node):
        self.found = found
        self.node = node


# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
