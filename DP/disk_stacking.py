"""
You're given a non-empty array of arrays where each subarray holds three integers and represents a disk.
These integers denote each disk's width, depth, and height, respectively. Your goal is to stack up the disks and to
maximize the total height of the stack. A disk must have a strictly smaller width, depth, and height than any other
disk below it.

Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the
bottom disk.
"""


def diskStacking(disks):
    # Time: O(n^2) and Space: O(n)
    # First we sort the disks by height so that we know the previous disk will always be smaller than next one.
    disks = sorted(disks, key=lambda x: x[2])
    # Using DP, store all the heights in the array, we will compute the max height using every height as the base
    # and see which one has the maximum height.
    store = [disk[2] for disk in disks]
    # The sequence array stores the index of the disk which is kept upon the current disk.
    # This is used only to build the full sequence of resultant disks.
    seq = [None for _ in disks]
    # To store the max height as the final answer
    max_height = disks[0][2]
    # The disks index which forms the max height as the base.
    max_height_idx = 0

    # Since the first disk is the smallest, the max height for it is itself, so we start from index 1.
    for curr in range(1, len(disks)):
        # curr = current disk index
        for prev in range(0, curr):
            # prev =  prev disk index.
            # We use the current disk as the base and try to add previous disks upon it by checking the
            # dimensions and whether the new stack increases the height of the existing disks height.
            if isValid(disks, curr, prev) and store[curr] < disks[curr][2] + store[prev]:
                # If yes, then we store the prev disk in the seq, meaning from the current disk, the next disk
                # stacked upon it is the prev disk.
                seq[curr] = prev
                # Update the max height for the current disk.
                store[curr] = disks[curr][2] + store[prev]
        # This part we calculate the overall max height. If the current disk height is greater than the
        # max height.
        if store[curr] > max_height:
            max_height = store[curr]
            max_height_idx = curr

    # Building the entire stack sequence.
    return build_sequence(disks, seq, max_height_idx)


def build_sequence(disks, seq, max_height_idx):
    # Stores the sequence
    result = []
    # We keep checking until the idx becomes None
    while max_height_idx is not None:
        # Append the disk
        result.append(disks[max_height_idx])
        # Update the idx to the next disk
        max_height_idx = seq[max_height_idx]

    return list(reversed(result))


def isValid(disks, curr, prev):
    """ Checking whether the previous disks dimensions are smaller than the current disk. """
    return disks[curr][0] > disks[prev][0] and disks[curr][1] > disks[prev][1] and disks[curr][2] > disks[prev][2]


print(diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]))
