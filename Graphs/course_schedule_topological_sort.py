"""
In topological sort, we print the node having 0 in-degree/prerequisites first.
Ex: For 5 ---> 4, here to complete 5, first we need to complete 4. So prerequisites of 5 is 4.

Basically, Topological Sort of = Reverse DFS (print the node after the for loop).

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of
them. If it is impossible to finish all courses, return an empty array.
"""


def topologicalSort(numCourses, prerequisites):
    # Time: O(v + e) and Space: O(v)

    # First we create the graph, since the given prerequisites is not an adjacency list.
    # Graph ex: { 5: [3, 4] }, means 5's prerequisites are [3, 4].
    graph = {i: [] for i in range(numCourses)}
    # Tracking all the visited nodes to reduce duplicate calls.
    visited = {i: False for i in range(numCourses)}
    # We maintain all the nodes which we come across in the graph while exploring a node.
    # This is will help us detect a cycle, and if there is a cycle then we return [] result.
    # Topological sort only works for Directed Acyclic Graph.
    stack = {i: False for i in range(numCourses)}
    result = []  # Stores the final order of the nodes.

    # Creating the graph, start=from vertex, end=to vertex.
    for start, end in prerequisites:
        graph[start].append(end)

    # Doing DFS for each node.
    for curr_node in range(numCourses):
        # Only unvisited nodes.
        if not visited[curr_node]:
            # If any DFS returns -1, means we found a cycle and thus return []
            if dfs(graph, visited, stack, curr_node, result) == -1:
                return []
    return result


def dfs(graph, visited, stack, curr_node, result):
    # Cycle check.
    if stack[curr_node]:
        return -1

    # Add the current node in the path
    stack[curr_node] = True

    # Loop through all the children node of the current node.
    for node in graph[curr_node]:
        # Only unvisited node.
        if not visited[node]:
            # IF DFS returns -1, then return -1 because we found a cycle.
            if dfs(graph, visited, stack, node, result) == -1:
                return -1

    # After exploring all the nodes from the current node, we mark it as visited.
    # And add this to result and also remove it from the path (stack).
    visited[curr_node] = True
    result.append(curr_node)
    stack[curr_node] = False


print(topologicalSort(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
