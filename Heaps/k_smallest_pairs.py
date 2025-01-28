"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
"""

import heapq


def kSmallestPairs(nums1, nums2, k: int):
    # Time: O(m*n*logn) and Space: O(k), where m=length of nums1 and n=length of nums2
    """
    Logic:
    We loop over every element of the nums1 and nums2 till we hit k items.
    We take the sum of the elements and store in the heap, we use max heap because we want only the top k smallest
    pairs in the result, so the max heap will eliminate the larger paris easily when the smaller pair comes.
    """
    # Max heap
    heap = []
    # For every nums1 element, we loop max till k
    for i in range(min(len(nums1), k)):
        # For every nums2 element
        for j in range(min(len(nums2), k)):
            # If the number of pairs are less then k, then we keep pushing to the heap.
            if len(heap) < k:
                # Since the inbuilt heap is min heap, so we use the -ve sum to convert it to the max heap, we also
                # store the index for the result.
                heapq.heappush(heap, (-(nums1[i] + nums2[j]), i, j))
            else:
                # If the heap is full, and we see that the current sum is less than the top element of the heap,
                # then we replace it.
                if nums1[i] + nums2[j] < -heap[0][0]:
                    # This operation will, pop the element and add the current element
                    heapq.heappushpop(heap, (-(nums1[i] + nums2[j]), i, j))
                else:
                    # Case if the current sum is greater than the top element of the max heap, we just break because
                    # the next all of the elements will anyways be greater as the nums are sorted in ascending order.
                    break
    # Parsing the result from the heap.
    return [[nums1[i], nums2[j]] for val, i, j in heap]
