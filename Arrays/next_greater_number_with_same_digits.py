"""
Also called "NEXT PERMUTATION".
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1],
[3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical
order, then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order
(i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger
rearrangement.
Given an array of integers nums, find the next permutation of nums

Input: nums = [1,2,3]
Output: [1,3,2]

https://leetcode.com/problems/next-permutation/description/

Brute Foce:
1. Generate all possible permutations
2. Sort them lexicographically
3. Find the current permutation in the sorted list
4. Return the next one (or the first if we're at the end)
Time = Space = O(n!)

Optimized:
Step 1: First we find the digit which is smaller than the immediate next digit.
Step 2: Now we find the largest index digit which is immediate greater than the above found digit.
Step 3: We swap the above two digits.
Step 4: Now we reverse from everything from the swapped idx onwards.
Time: O(n) and Space: O(1)
"""


def findNext(nums):
    n = len(nums)
    k = -1

    # Step 1: Find the pivot
    for i in range(n - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            k = i - 1
            break

    # If the sequence is already the highest permutation, reverse it to get the lowest permutation
    if k == -1:
        nums.reverse()
        return nums

    # Step 2: Find the first element greater than the pivot
    l = n - 1
    while nums[l] <= nums[k]:
        l -= 1

    # Step 3: Swap the pivot and the element found in step 2
    nums[k], nums[l] = nums[l], nums[k]

    # Step 4: Reverse the subsequence from the pivot to the end
    # We reverse because after swapping, the values from pivot to end are in descending order, try it with an example
    nums[k + 1 :] = reversed(nums[k + 1 :])
    return nums


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


print(findNext([1, 2, 3]))
