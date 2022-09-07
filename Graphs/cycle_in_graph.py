"""
Given an adjacency graph, check whether it contains a cycle

"""


def checkCycle(arr):
    # Time: O(v + e) and Space: O(v), v = vertices and e = edges.

    # We keep track of the visited nodes
    visited = [False for _ in arr]
    # We also keep track of nodes through which we visit other nodes to find a cycle.
    # If a node is already present in the stack, that means we have found a cycle.
    stack = [False for _ in arr]
    # Doing DFS for each node
    for i in range(len(arr)):
        # Only if its not visited.
        if not visited[i]:
            if dfs(arr, visited, stack, i):
                return True
    return False


def dfs(arr, visited, stack, idx):
    # If the node is already in stack, we found a cycle and return True
    if stack[idx]:
        return True

    # Marking that the current node is being explored.
    stack[idx] = True
    # Exploring all the children of the current node
    for child in arr[idx]:
        # Only unvisited children.
        if not visited[child]:
            if dfs(arr, visited, stack, child):
                return True

    # At this point, we did not find a cycle with the current node, so we remove it from stack and
    # mark it as visited.
    stack[idx] = False
    visited[idx] = True
    return False


print(checkCycle([[1, 2], [2], [0], []]))
