"""
Calculate the total number of connected components in the graph. A connected component is a set of vertices in a graph
that are linked to each other by paths.

input = [[0, 1], [1, 2], [3, 4]]
output = 2

"""


def numberOfConnectedComponents(edges, n):
    # Time: O(v + e) and Space: O(v)
    """
    Logic:
    First create a graph using the edges list, then do DFS on every unvisited node.
    At completion of every DFS, we know that we have finished a component, so we increase +1 to the result.
    :param edges: Edge list
    :param n: Number of nodes
    :return: Result, total number of connected components.
    """

    # Creating a graph using the edges list.
    graph = createGraph(edges, n)
    # Tracking the visiting nodes.
    visited = set()
    result = 0  # Storing the total number of connected components.
    # For every node
    for node in graph.keys():
        # only unvisited nodes
        if node not in visited:
            dfs(graph, visited, node)
            # After completion of DFS, increment the result.
            result += 1

    return result


def dfs(graph, visited, node):
    # BASIC DFS
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph, visited, child)

    return None


def createGraph(edges, n):
    # Creating a graph using the edges list, each item in the edge list = [source node, destination node]
    graph = {i: [] for i in range(n)}
    for src, dest in edges:
        graph[src].append(dest)

    return graph


input = [[0, 1], [1, 2], [3, 4]]
print(numberOfConnectedComponents(input, 5))
