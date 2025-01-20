"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0]
is a name, and the rest of the elements are emails representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common
email to both accounts. Note that even if two accounts have the same name, they may belong to different people as
people could have the same name. A person can have any number of accounts initially, but all of their accounts
definitely have the same name.
After merging the accounts, return the accounts in the following format: the first element of each account is the name,
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"]
,["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],
["John","johnnybravo@mail.com"]]

Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'],
['John', 'johnnybravo@mail.com'], ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
would still be accepted.
"""


def accountsMerge(accounts):
    # Time: O(n * k * nlogn), n is the number of accounts and k is the max number of emails
    # Space: O(nk)
    """
    Logic:
    We will create a graph where an email address will be linked to all its accounts email addresses.
    Then we will visit every email in the graph, and do DFS where we will store all the child email addresses in
    a stack and keep marking the emails as visited.
    After the dfs is returned, we will sort the value of the stack store in the result, then go to the next unvisited
    email address.
    """
    # Creating graph
    graph = {}
    # Used to store account name for each email address
    names = {}
    # For each account
    for item in accounts:
        # Getting account name
        name = item[0]
        # For each email which starts from index 1
        for i in range(1, len(item)):
            email = item[i]
            if email not in graph:
                graph[email] = set()
            if item[1] not in graph:
                graph[item[1]] = set()
            # Linking the current email to the 1st email of this account
            graph[email].add(item[1])
            # Linking the 1st email of the account to this email
            graph[item[1]].add(email)
            # Adding the account name for this email
            names[email] = name
    # Final result
    result = []
    # Marking visited emails
    visited = set()
    # For each email
    for email in graph.keys():
        # If unvisited
        if email not in visited:
            visited.add(email)
            # Storing this email in the stack
            stack = [email]
            # DFS
            dfs(graph, email, stack, visited)
            # Storing the result of DFS after sorting the emails
            result.append([names[email]] + list(sorted(stack)))

    return result


def dfs(graph, email, stack, visited):
    # For each child email
    for nextEmail in graph.get(email, []):
        # IF unvisited
        if nextEmail not in visited:
            visited.add(nextEmail)
            stack.append(nextEmail)
            # Start the function from this child email
            dfs(graph, nextEmail, stack, visited)


accountsMerge(
    [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
)
