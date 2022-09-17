"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: ["flower", "flow", "flight"]
Output: 2

"""


def longest_common_prefix(strs):
    # Time: O(n x m) and Space: O(n x m), where n = no. of words, m = length of the longest word.
    """
    Logic:
    First create a tries for the given words, and then until you have only one letter in the node, keep
    moving forward in the node and increase the result.
    Once you have more than one letter in the node, that means we have found two different words at this point, so
    we break.
    """

    # Creating the tries data structure
    root = create_tries(strs)
    # Reference variable for traversing.
    node = root
    # To store the longest common prefix.
    result = 0

    # Until we have only one letter in the current node level.
    while len(node) == 1:
        # Keeping moving forward.
        node = node[list(node.keys())[0]]
        result += 1

    return result


def create_tries(strs):
    # Basic, tries data structure creation for the given words.
    root = {}
    for word in strs:
        node = root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["*"] = True

    return root


print(longest_common_prefix(["flower", "flow", "flight"]))
