"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears
in at most one part. Note that the partition is done so that after concatenating all the parts in order, the resultant
string should be s.
Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

https://leetcode.com/problems/partition-labels/description/

Brute Force:
Find all the min and max index for every letter, and then merge overlapping intervals.
Time: O(n) and Space: O(1) because we only store at most 26 characters

Optimized:
First, we create a dictionary that stores the last occurrence of each character in the string.

We maintain two pointers:
start: beginning of current partition
end: tracks the furthest extending character in current partition

As we iterate through the string:
For each character, we update end to be the maximum of current end and the last occurrence of current character
When our current index reaches end, we've found a valid partition
Time Complexity: O(n)
Space Complexity: O(1) since we only store at most 26 characters in the hash map

"""


def partitionLabels(s):
    # Get the last occurrence of each character
    last_occurrence = {char: i for i, char in enumerate(s)}

    partitions = []
    start = 0
    end = 0

    # Iterate through the string
    for i, char in enumerate(s):
        # Update the end to be the furthest last occurrence
        # of any character we've seen in current partition
        end = max(end, last_occurrence[char])

        # If we've reached the end of current partition
        if i == end:
            partitions.append(end - start + 1)
            start = i + 1

    return partitions
