"""
Kosaraju's Algorithm.
Find and print all the strongly connected components in the given graph.
A strongly connected component is one in which you can reach a node starting from any node.
Every individual node is a strongly connected component by default.

Input: [[1], [2, 3], [0], [4], []]
Output: [[0, 2, 1], [3], [4]]

"""


def strongly_connected_components(arr):
    # Time: O(v + e) and Space: O(v)
    """
    Logic: There are 3 major steps:
    1. Sort the nodes in the order of their finishing time.
    2. Reverse the edges.
    3. Do DFS on every unvisited node of the sorted nodes, store the visiting nodes in the stack, once out of DFS,
       append this stack to the result.
    """

    # Stack to store the nodes by their finishing time.
    finishing_order_stack = []
    # Track the visited nodes
    visited = set()
    # First step: Sorting by finishing time.
    sort_by_finishing_order(arr, finishing_order_stack, visited, 0)

    # Second step: Reverse the edges of the graph.
    reversed_edges = reverse_edges(arr)

    # Third step: Doing DFS on the nodes sorted by finishing time.
    visited = set()
    result = []  # Final result
    while finishing_order_stack:
        # Getting the node with most finishing time, that's why we pop from the end of the stack
        node = finishing_order_stack.pop()
        # Unvisited nodes only
        if node not in visited:
            # Doing DFS, component_stack will store all the strongly connected components starting from the
            # current node.
            component_stack = []
            dfs(reversed_edges, component_stack, visited, node)
            # Storing the strongly connected components to the result
            result.append(component_stack)

    return result


def sort_by_finishing_order(arr, stack, visited, node):
    # Sorting by finishing time
    # This is not a topological sort as we mark visited at the start.
    # But the node is appended to the result after exploring all the child which is same as topological sort.
    visited.add(node)
    for curr_node in arr[node]:
        if curr_node not in visited:
            sort_by_finishing_order(arr, stack, visited, curr_node)
    stack.append(node)


def reverse_edges(arr):
    # We reverse the edges of the graph.
    # We create a new graph where the edges are reversed.
    reversed_edges = [[] for _ in arr]
    # Starting from node 0 ..to.. len(arr)
    for i in range(len(arr)):
        # We will make every child point to this current node
        for child in arr[i]:
            reversed_edges[child].append(i)  # This means, from node(child) --> node(i)
    return reversed_edges


def dfs(reversed_edges, stack, visited, node):
    # Basic DFS, where we append the node as we visit it.
    visited.add(node)
    stack.append(node)
    for child in reversed_edges[node]:
        if child not in visited:
            dfs(reversed_edges, stack, visited, child)

    return None


print(strongly_connected_components([[1], [2, 3], [0], [4], []]))
