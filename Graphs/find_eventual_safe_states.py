"""
There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed
2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from
node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from
that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.

Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
"""


def brute_force(graph):
    """Time Complexity: O(n * 2^n) in worst case
    Space Complexity: O(n) for the recursion stack and visited set"""
    n = len(graph)

    def is_safe(node, visited):
        # If we've seen this node in current path, it's a cycle
        if node in visited:
            return False

        # If no outgoing edges, it's terminal and safe
        if not graph[node]:
            return True

        # Mark current node as visited for this path
        visited.add(node)

        # Check all paths from this node
        # If any path is unsafe, this node is unsafe
        for next_node in graph[node]:
            if not is_safe(next_node, visited.copy()):
                return False

        return True

    safe_nodes = []
    # Check each node
    for node in range(n):
        if is_safe(node, set()):
            safe_nodes.append(node)

    return safe_nodes


# Optimized Solution using DFS with memoization (Colors)
def eventualSafeNodes_optimized(graph):
    """Time Complexity: O(V + E) where V is number of vertices and E is number of edges
    Space Complexity: O(n) for the colors array and recursion stack
    Approach:

    Uses color marking (similar to cycle detection in graphs)
    WHITE (0): Node not processed
    GRAY (1): Node is being processed (in current path)
    BLACK (2): Node is completely processed and is safe
    We memoize results using the colors array
    If we encounter a GRAY node, we've found a cycle
    If we encounter a BLACK node, we can use its pre-computed result"""
    n = len(graph)
    # Colors: WHITE (0) = unvisited, GRAY (1) = in current path, BLACK (2) = processed
    colors = [0] * n

    def is_safe(node):
        # If already processed, check if it was marked safe
        if colors[node] > 0:
            return colors[node] == 2

        # Mark as being visited in current path
        colors[node] = 1

        # Check all neighboring nodes
        # If any neighbor forms a cycle or leads to unsafe node, this node is unsafe
        for next_node in graph[node]:
            if colors[next_node] == 1 or not is_safe(next_node):
                return False

        # Mark as safe and processed
        colors[node] = 2
        return True

    safe_nodes = []
    # Process all nodes
    for node in range(n):
        if is_safe(node):
            safe_nodes.append(node)

    return safe_nodes
