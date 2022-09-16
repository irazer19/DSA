"""
Check whether the given graph is Bipartite.
A Bipartite graph is one in which we can color the nodes such that the adjacent nodes are of different color.

Input: [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: False

"""


def isBipartite(arr):
    # Time: O(v + e) and Space: O(v)
    """
    Logic: We will create an array colors to store the color type at every index/node.
    We have two color types: True and False.
    For starting index we will give the color True, and then do BFS and for each child node we will
    check whether it is visited, if not visited then we will assign the opposite color to that child and add it to the
    queue. And if already visited then we will check whether the current node color and this child color are the same,
    if it's same then we will return False as it breaks the property of Bipartite graph.

    We will check the above process from every unvisited index.
    """

    # Empty graph is bipartite Graph.
    if not arr:
        return True

    # This array will store the color (True/False) for every node index.
    colors = [None for _ in arr]

    # For every index/node we start the BFS if it is unvisited.
    for i in range(len(colors)):
        # Only unvisited nodes
        if colors[i] is None:
            # Start color is True
            colors[i] = True
            # BFS
            q = [i]
            while q:
                node = q.pop(0)
                for child in arr[node]:
                    # If the child is unvisited, then we assign the opposite color and add to the queue.
                    if colors[child] is None:
                        colors[child] = not colors[node]
                        q.append(child)
                    else:
                        # Else, if current node and child color is same then we return False as the answer.
                        if colors[child] == colors[node]:
                            return False
                        # We dont add to the queue because we have already visited this node.
    # If we could not find any two adjacent nodes with same color then we return True.
    return True


print(isBipartite([[4], [], [4], [4], [0, 2, 3]]))
