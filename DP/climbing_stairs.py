"""
You are climbing a staircase of height. It takes n steps to reach the top.
Each time you can climb upto maxSteps steps. In how many distinct ways can you climb to the top?

"""


def staircaseTraversal(height, maxSteps):
    # Time = Space = O(n)
    # We will use sliding window technique, the number of elements in the window = maxSteps given to use in the
    # question. So the current height = sum of all the previous elements in the window.
    # Running sum will help us get the total window sum
    running_sum = 0
    # For each height, we will calculate the total ways and store here.
    store = [0 for _ in range(height + 1)]
    # For height=0, there is just 1 way as we are already there.
    store[0] = 1

    # For each height starting from 1
    for current_height in range(1, len(store)):
        # Start of the window, we add -1 to get the element which has to be subtracted in case.
        start_window = current_height - maxSteps - 1
        # End of the window is just the previous element
        end_window = current_height - 1

        # This is where we slide the window by subtracting the older element
        if start_window >= 0:
            running_sum -= store[start_window]

        # Whether we subtract or not, we will add the end window element to keep moving.
        running_sum += store[end_window]
        # Finally storing the total ways for the current height.
        store[current_height] = running_sum

    return store[-1]


print(staircaseTraversal(4, 3))
