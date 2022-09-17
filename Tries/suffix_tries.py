"""
Write a SuffixTrie class for a Suffix-Trie-like data structure. The class should have a root property set to be the
root node of the trie and should support:
1. Creating the trie from a string: this will be done by calling the populateSuffixTrieFrom method upon class
instantiation, which should populate the root of the class.
2. Searching for strings in the trie.

Input "babc"
Output = {
    "c": {"*": True},
    "b": {
        "c": {"*": True},
        "a": {"b": {"c": {"*": True}}},
    },
    "a": {"b": {"c": {"*": True}}},
}
"""


# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Time = Space = O(n^2)
        """
        Logic:
        From every index we will loop till the length of the string, and add the letter to the dictionary if
        it's not already there, once the inner loop is finished, we will append * to mark that we have a word
        at this level of dictionary.
        """

        # From every index
        for i in range(len(string)):
            # We will always start at the root node
            node = self.root
            # Our word starts from j and goes till the end of the string.
            for j in range(i, len(string)):
                # If the dictionary/node does not contain the letter then we add that letter to the dictionary/node.
                if string[j] not in node:
                    node[string[j]] = {}
                # Once we have the letter, we will move forward in the dictionary/node to search for the next letter.
                node = node[string[j]]
            # At this point we have completed a word, and so we append * to mark the end of that word.
            node[self.endSymbol] = True

        print(self.root)

    def contains(self, string):
        # Check whether the given string is present in the trie data structure.
        # Initializing the trie at the root.
        node = self.root
        # For every letter in the string.
        for c in string:
            # If the letter is not in the current level of the dictionary/node, we return False.
            if c not in node:
                return False
            # Else, we keep moving forward in the dictionary/node.
            node = node[c]
        # Finally, since we have found all the letters, we will only return True if "*" is found after completing
        # all the letters of the string because that confirms that we have a word.
        return '*' in node
