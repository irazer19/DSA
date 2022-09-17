"""
You're given a two-dimensional matrix of potentially unequal height and width containing letters; this matrix
represents a Boggle board. You're also given a list of words.

Write a function that returns an array of all the words contained in the Boggle board.

A word is constructed in the boggle board by connecting adjacent (horizontally, vertically, diagonally) letters,
without using any single letter at a given position more than once; while a word can have repeated letters, those
repeated letters must come from different positions in the Boggled board in order for the word to be contained in the
board. Note that two or more words are allowed to overlap and use the same letters in the Boggle board.

Input:
    board = [
        ["t", "h", "i", "s", "i", "s", "a"],
        ["s", "i", "m", "p", "l", "e", "x"],
        ["b", "x", "x", "x", "x", "e", "b"],
        ["x", "o", "g", "g", "l", "x", "o"],
        ["x", "x", "x", "D", "T", "r", "a"],
        ["R", "E", "P", "E", "A", "d", "x"],
        ["x", "x", "x", "x", "x", "x", "x"],
        ["N", "O", "T", "R", "E", "-", "P"],
        ["x", "x", "D", "E", "T", "A", "E"],
    ]
    words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]

Output:
["this", "is", "a", "simple", "boggle", "board", "NOTRE-PEATED"]

"""


def boggleBoard(board, words):
    # Time: O(nm * 8^m) and Space: O(nm + ws)
    # where n = width, m = height and w = no. of words, s = length of the longest word.
    """
    Logic:
    First we construct a Tries' data structure using the given words.
    We treat every letter in the board as a node, and for every letter we check whether it's present in the
    tries or not. If present then we start exploring from that node.
    Explore (DFS):
    If the current letter is not present in the tries then stop and return,
    Mark it as visited, and if * is present in the tries then add the word to the result.
    Now do DFS on all the neighbors, once out of the DFS then unvisited this node and return.

    Once we have explored all the nodes, we return the result

    """

    # Creating Tries data structure
    root = create_tries(words)
    # Tracking the visited nodes.
    visited = [[False for _ in row] for row in board]
    result = set()  # Stores the words, we use a set to remove the duplicate words.

    # For every letter in the board
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Initializing the tries to the root.
            node = root
            # If unvisited and the letter is present the tries.
            if not visited[i][j] and board[i][j] in node:
                # Explore from the given letter
                explore(board, words, visited, result, node, i, j)

    return result


def explore(board, words, visited, result, node, row, col):
    # This is a DFS function.
    # If the letter is not in the current tries level, then return because we dont have any matching word.
    if board[row][col] not in node:
        return
    # Mark the current letter as visited
    visited[row][col] = True
    # Moving forward in the tries.
    node = node[board[row][col]]

    # Checking for * and storing the word in the result.
    if "*" in node:
        result.add(node["*"])

    # Exploring the neighbors using DFS.
    # Top
    if row > 0 and not visited[row - 1][col]:
        explore(board, words, visited, result, node, row - 1, col)
    # left
    if col > 0 and not visited[row][col - 1]:
        explore(board, words, visited, result, node, row, col - 1)
    # bottom
    if row < len(board) - 1 and not visited[row + 1][col]:
        explore(board, words, visited, result, node, row + 1, col)
    # right
    if col < len(board[0]) - 1 and not visited[row][col + 1]:
        explore(board, words, visited, result, node, row, col + 1)
    # top left
    if row > 0 and col > 0 and not visited[row - 1][col - 1]:
        explore(board, words, visited, result, node, row - 1, col - 1)
    # top right
    if row > 0 and col < len(board[0]) - 1 and not visited[row - 1][col + 1]:
        explore(board, words, visited, result, node, row - 1, col + 1)
    # bottom left
    if row < len(board) - 1 and col > 0 and not visited[row + 1][col - 1]:
        explore(board, words, visited, result, node, row + 1, col - 1)
    # bottom right
    if row < len(board) - 1 and col < len(board[0]) - 1 and not visited[row + 1][col + 1]:
        explore(board, words, visited, result, node, row + 1, col + 1)

    # After finishing the DFS for the current node, we remove it from visited because it is possible that
    # another word can be formed using this node while exploring from another nodes.
    visited[row][col] = False


def create_tries(words):
    # Basic, tries data structure creation for the given words.
    root = {}
    for word in words:
        node = root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node["*"] = word

    return root


input_board = [
    ["t", "h", "i", "s", "i", "s", "a"],
    ["s", "i", "m", "p", "l", "e", "x"],
    ["b", "x", "x", "x", "x", "e", "b"],
    ["x", "o", "g", "g", "l", "x", "o"],
    ["x", "x", "x", "D", "T", "r", "a"],
    ["R", "E", "P", "E", "A", "d", "x"],
    ["x", "x", "x", "x", "x", "x", "x"],
    ["N", "O", "T", "R", "E", "-", "P"],
    ["x", "x", "D", "E", "T", "A", "E"],
]

input_words = ["this", "is", "not", "a", "simple", "boggle", "board", "test", "REPEATED", "NOTRE-PEATED"]

print(boggleBoard(input_board, input_words))
