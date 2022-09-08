"""
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you.
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of
this new language. Derive the order of letters in this language.

Input：["wrt","wrf","er","ett","rftt"]
Output："wertf"
Explanation：
from "wrt"and"wrf" ,we can get 't'<'f'
from "wrt"and"er" ,we can get 'w'<'e'
from "er"and"ett" ,we can get 'r'<'t'
from "ett"and"rftt" ,we can get 'e'<'r'
So return "wertf"
"""


def alien_dictionary(arr):
    # Time: O(v + e) and Space: O(v)
    """
    Logic: Since we have to order the letters according to the sorted list of words, this is topologicalSort
    problem where a letter is supposed to appear before another letter.
    So we first create a graph, which is a prerequisites graph,
    Ex: For 'abc', we know that the letter 'a' should be before 'b', 'c' so the prerequisites graph will be
    { 'a' : ['b', 'c'] }, which means, to complete 'a', we must first complete 'b' and 'c'.

    So first we create a graph, and then do topological sort and return the result.
    """

    # Creating a prerequisites graph of the words
    graph = generate_graph(arr)
    # Tracking all the visited letters/nodes
    visited = set()
    # Stores the final order of the letters
    result = []
    # For each node/letter
    for node in graph:
        # Only unvisited letters/nodes.
        if node not in visited:
            dfs(graph, visited, result, node)

    return result


def dfs(graph, visited, result, node):
    # Exploring all the children of the given node
    for child in graph[node]:
        if child not in visited:
            dfs(graph, visited, result, child)

    # Only after fully exploring the current node, we mark it as visited and append to the result.
    visited.add(node)
    result.append(node)


def generate_graph(arr):
    # We generate the prerequisites graph.
    # First we initialize the graph with all the nodes/letters
    graph = {letter: [] for word in arr for letter in word}
    # We compare current word and the next word, we only check the first letter, if its different then
    # we store the word1's letter as the prerequisite of word2's letter.
    # Else, if the letters dont match, then we use a while loop till the minimum length of the two words,
    # until we find a different letter, if we dont find a different letter then return empty array.
    for i in range(len(arr) - 1):
        word1, word2 = arr[i], arr[i + 1]
        # Getting the minimum length
        min_length = min(len(word1), len(word2))
        ptr = 0  # pointer to increase if the letters are same.
        while ptr < min_length:
            # Go to next letter if the current letters are same
            if word1[ptr] == word2[ptr]:
                ptr += 1
            else:  # Else break
                break

        # If after the while loop, the pointer has the same length as min_length then we did not find any
        # different letters in the two words, so we return empty array.
        if ptr == min_length:
            return []
        # Adding the prerequisite of word2
        graph[word2[ptr]].append(word1[ptr])

    return graph


print(alien_dictionary(["wrt", "wrf", "er", "ett", "rftt"]))
