"""
Write a function that takes in a non-empty string representing a valid unix-shell path and returns a shortened
version of that path.

Input: "/foo/../test/../test/../foo//bar/./baz"
Output: "/foo/bar/baz"

"""


def shortenPath(path):
    # Time = Space = O(n)
    """
    Logic:
    When you split the array using '/', there are few characters that we need to handle.
    If the char is "" or ".", just ignore it because it represents the current path.
    If the char is a word, then add it to the stack.
    If the char is "..", then we have multiple cases to handle which we will see in the code.
    """

    # We will store the chars in the stack and take the decision whether we should pop or add new one.
    stack = []
    # Checking whether the path starts with a root.
    # If no, then we will have to maintain the same relative path.
    startsWithRoot = path[0] == '/'
    path = path.split('/')

    # For each item
    for item in path:
        # If the item if one of the below chars, then just skip it.
        if item in ['', '.']:
            continue
        # If the item is the below char, it means, we have to go the parent directory
        # Ex: /foo/bar/../ is equal to /foo
        if item == '..':
            # If the stack is empty
            if not stack:
                # If the path does not starts with slash, then we add this item to maintain the relative path.
                if not startsWithRoot:
                    stack.append(item)
            else:
                # Else if the path starts with a slash or the top stack element is a word then just pop it,
                if startsWithRoot or stack[-1] != '..':
                    stack.pop()
                elif stack[-1] == '..':
                    # Else if the top stack element is also a .., then we maintain the relative path and
                    # therefor append this item also.
                    stack.append(item)
        else:
            # The item is a word, just add it.
            stack.append(item)

    # Now if the path starts with a slash, then we add the slash, else we keep the relative order of the path.
    result = '/' + '/'.join(stack) if startsWithRoot else '/'.join(stack)
    return result
