"""
Find the shortest path between "start" node and all the other nodes.
You are given adjacency list which contains [node, weight], where the distance between the current index node and the
node is the weight.

"""


def dijkstrasAlgorithm(start, edges):
    # Time: O(v^2 + e) and Space: O(v)

    # Logic: We find the node having the minimum distance from start, and loop through all the children
    # and update the distance of the children nodes. If we have visited all the children OR the minimum distance
    # is infinity then we stop.

    # We store all the min distance here for every node.
    result = [float('inf') for _ in edges]
    # The distance of the start node with itself is 0
    result[start] = 0
    # Tracking the visited nodes
    visited = [False for _ in edges]

    # Until we visit all the nodes.
    while not all(visited):
        # We get the node with the minimum distance from start.
        vertex, min_dist = get_min(result, visited)
        # If the vertex is None, that means we cannot reach this node at all so we break.
        if vertex is None:
            break
        # Marking the node as visited.
        visited[vertex] = True
        # Exploring all the children and updating their distance.
        for to_vertex, wgt in edges[vertex]:
            # The distance of current child from start =
            # min(existing distance, distance of parent from start + distance of the child from parent)
            result[to_vertex] = min(result[to_vertex], min_dist + wgt)

    # -1 if the node could not be visited.
    return [-1 if i == float('inf') else i for i in result]


def get_min(result, visited):
    # Gets the node with the minimum distance.
    vertex = None
    curr_dist = float('inf')
    for i in range(len(result)):
        # Only unvisited nodes.
        if not visited[i]:
            if result[i] < curr_dist:
                curr_dist = result[i]
                vertex = i
    return vertex, curr_dist


print(dijkstrasAlgorithm(0, [[[1, 7]], [[2, 6], [3, 20], [4, 3]], [[3, 14]], [[4, 2]], [], []]))
