"""
Given n, the number of nodes, find the total number of binary tree topologies which can be formed.
Note: For n=0, output is 1, because we can have "None" node.

Input: 3
Output: 5

"""


def numberOfBinaryTreeTopologies(n):
    # Time: O(n^2) and Space: O(n)
    """
    Logic:
    Using Bottom up approach.
    We calculate the number of topologies for n = 0, 1, 2, ... n (inclusive), and store the result in cache as
    we progress.
    The idea is that given n=3 say, we start the left subtree with 0 nodes, and right subtree with 2 nodes (since
    the root node consumes 1 node), the find the total number of topologies possible from left and right in this
    configuration and total becomes (result from left node * result from right node).
    Then repeat the above process by increasing the node in left subtree till we use all the nodes available.
    And we keep adding the result from each configuration to the numberOfTopologies.
    Finally, we add the result to the cache for the current n.

    """
    # For n=0, we have total topologies = 1.
    cache = {0: 1}

    # Using bottom up approach, we start from 1 because we already have the result for 0 in the cache.
    for m in range(1, n + 1):
        # The total number of topologies possible from the current m, where m= number of nodes available.
        numberOfTopologies = 0
        # We start forming the trees starting from 0 nodes in the left subtree and incrementing by one...
        for leftNodes in range(0, m):
            # We calculate the total nodes in the right subtree.
            # We subtract 1 because of the root node.
            rightNodes = m - 1 - leftNodes
            # The total number of topologies possible from the given configuration of leftNodes and rightNodes,
            # is equal to the product of the result of them.
            # We use product because, for example, for 4 different left subtrees and 3 different right subtrees,
            # we can have 4 * 3 = 12 different combinations.
            numberOfTopologies += cache[leftNodes] * cache[rightNodes]
        # Finally, we store the result for m in the cache.
        cache[m] = numberOfTopologies

    return cache[n]
