"""
Given a two non-empty list of integers, write a function that determines whether the second array is a
subsequence of the first one.

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

Output: True

"""


def isValidSubsequence(array, sequence):
    # Time: O(n) and Space: O(1)
    """
    Logic:
    As we iterate through the array, we will check whether the current array element matches the current sequence
    element, if yes then we move the pointer to the next sequence element.
    We return true only if the sequence pointer has reached the end of the array, which means every element was
    matched.
    """
    # Sequence index
    seqIdx = 0
    # Foe each array element
    for n in array:
        # If we have finished all the sequence elements, we break
        if seqIdx == len(sequence):
            break
        # Else if the the current array element matches the sequence element, we move to the next sequence element.
        if sequence[seqIdx] == n:
            seqIdx += 1
    
    return seqIdx == len(sequence)
