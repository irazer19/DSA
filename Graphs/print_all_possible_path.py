"""
Print all paths from a given source to a destination in a graph.

"""


def printAllPath(arr, start_node, end_node):
    # Time = Space = O(v^v), because for each vertex we can have at max v possibilities.

    # Stores the all the nodes in the path while traversing
    stack = []
    result = []  # Stores the list of path from src to dest

    # Do DFS starting from source
    dfs(arr, stack, end_node, result, start_node)

    return result


def dfs(arr, stack, dest, result, node):
    # If there is a cycle, just return
    if node in stack:
        return None

    # If the current node = destination node, append the stack array to the result.
    if node == dest:
        stack.append(node)
        result.append(stack[:])
        stack.pop()
        return None

    # Add this node to the path until we have explored this node fully.
    stack.append(node)
    for child in arr[node]:  # Exploring all the children.
        dfs(arr, stack, dest, result, child)
    # Remove this node from the path.
    stack.pop()


print(printAllPath([[1, 2, 3], [3], [0, 1], []], 2, 3))
