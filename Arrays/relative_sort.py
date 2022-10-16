"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do
not appear in arr2 should be placed at the end of arr1 in ascending order.

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""


def relativeSortArray(arr1, arr2):
    # Time: O(n + m) = Space: O(n + m), where n, m is the length of the arr1 and arr2.
    """
    Logic:
    Count the frequency of the arr1 characters. Now we will loop through all the arr2 characters, and then
    add that character * its frequency to the result array, we will also pop out the char after it's added to the
    result array.
    Now the chars which were not in arr2 but were present in arr1 will be left inside the frequency hashmap,
    So we will loop through all the items in the frequency hashmap, and then add the remaining characters to the
    result array in sorted order according to the question's requirement.

    """
    # Stores all the char frequency of arr1
    freqTable = {}
    for n in arr1:
        if not freqTable.get(n, None):
            freqTable[n] = 0
        freqTable[n] += 1

    # Final result array
    result = []
    # Stores all the chars which were present in arr1 but not in arr2.
    doNotAppear = []
    # For each char in arr2
    for i in range(len(arr2)):
        n = arr2[i]
        # We will append the char * freq in the result.
        if freqTable.get(n, None):
            result += [n] * freqTable[n]
            # Pop out the already printed char.
            freqTable.pop(n)
    # Now the left over chars were present in arr1 only, so we add them in another array which will be sorted later.
    for n, freq in freqTable.items():
        doNotAppear += [n] * freq
    # Finally appending the sorted array to the result.
    result += sorted(doNotAppear)
    return result
