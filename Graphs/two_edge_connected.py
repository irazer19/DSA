"""
You're given a list of edges representing an unweighted and undirected graph. Write a function that returns
a boolean indicating whether the graph is two-edge connected.

A graph is two-edge connected if, for every one of its edges, the edges' removal from the graph doesn't cause the graph
to become disconnected. If the removal of any single edge disconnects the graph, then it is not two-edge connected.
If the given graph is already disconnected, then also it is not two-edge connected. An empty graph is considered
two-edge connected.

Ex: [[1, 2, 5], [0, 2], [0, 1, 3], [2, 4, 5], [3, 5], [0, 3, 4]]
Output: True

"""


def twoEdgeConnectedGraph(edges):
    # Time: O(v + e) and Space: O(v)
    """
    Logic: We will use DFS, now as we arrive at a new node, we will store its arrival time, this arrival time
    is useful to track whether there is only one way of reaching this node. In future after exploring other nodes
    from this node, if the arrival time of this node remains the same, then we know that we have only one way
    of reaching this node, therefore the given graph is not two-edge connected.

    The arrival time of a node should decrease as we update it by comparing with its other child's arrival time.
    """

    # An empty graph is a two-edge connected.
    if not edges:
        return True

    # Default arrival time for all nodes is -1, this will help to know whether all the nodes were ever visited.
    arrivalTimeList = [-1 for _ in edges]
    # From here, we do DFS, where starting node is 0, its parent is -1, arrival time is 0
    # If we found a bridge (only way of reaching a node) then we return -1 from the function calls, so we check
    # if the final DFS value is -1 then we return False
    if dfs(edges, 0, -1, 0, arrivalTimeList) == -1:
        return False

    # Else, we still check whether all the nodes were visited so that we dont miss the case where a node was fully
    # disconnected.
    return allVisited(arrivalTimeList)


def dfs(edges, node, parent, arrivalTime, arrivalTimeList):
    # currArrivalTime will be updated the minimum arrival time returned by its children.
    currArrivalTime = arrivalTime
    # Updating the arrival time for the current node
    arrivalTimeList[node] = arrivalTime

    # For every child
    for child in edges[node]:
        # If we have not visited the child.
        if arrivalTimeList[child] == -1:
            # We do DFS and then update the arrival time for the current node to whichever is minimum.
            currArrivalTime = min(currArrivalTime, dfs(edges, child, node, arrivalTime + 1, arrivalTimeList))
        elif child != parent:
            # Else, since we have already visited this child before, we update the minimum arrival time.
            # Note: we ignore if the child == parent because it makes no sense since we came from parent.
            currArrivalTime = min(currArrivalTime, arrivalTimeList[child])

    # Finally, after exploring all the children and updating the arrival time to minimum possible, if we
    # still see that there is no change in before and after arrival time then we have a bridge and so we return -1.
    if currArrivalTime == arrivalTime and parent != -1:
        return -1

    # Else, returning the minimum arrival time for the current node.
    return currArrivalTime


def allVisited(arrivalTimeList):
    # Just check whether all the nodes were visited.
    # Unvisited nodes will have arrival time = -1
    for node in arrivalTimeList:
        if node == -1:
            return False
    return True


print(twoEdgeConnectedGraph([[1, 2, 5], [0, 2], [0, 1, 3], [2, 4, 5], [3, 5], [0, 3, 4]]))
