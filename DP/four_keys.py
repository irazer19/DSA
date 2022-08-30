"""
    Imagine you have a special keyboard with the following keys:
Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it
                 after what has already been printed.

If you can only press the keyboard for N times (with the above four
keys), write a program to produce maximum numbers of A's. That is to
say, the input parameter is N (No. of keys that you can press), the
output is number of A's that you can produce

"""


def four_keys(n):
    # Time: O(n^2) and Space: O(n)
    # For all the inputs <= 6, the total prints is the number itself.
    if n <= 6:
        return 6
    # We use DP here. Store all the previous result for every number till N.
    # We want N that's why n + 1
    store = [0 for i in range(n + 1)]
    # Again base case if n <= 6, we fill n itself
    for i in range(0, 7):
        store[i] = i

    # For every number till n, we find the total prints
    for x in range(7, len(store)):
        max_for_x = 0
        # Since for every number n, we will have to use atleast once ctrl A, C, V, thats why
        # start print from x - 3 onwards.
        # Ex: Fosr N = 10, we can start print 7 times, then 6 times, then 5 times...
        for p in range(x - 3, 0, -1):
            # Total prints for current x number
            # Which is = Max possible prints for p * Number of times we can use ctrl A, C, V...
            total_prints = store[p] * (x - p - 1)
            # Storing the max result for x
            max_for_x = max(max_for_x, total_prints)
        # Updating the DP array for x
        store[x] = max_for_x
    return store[-1]


print(four_keys(14))
