"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

"""


def find_closest_elements(arr, k, x):
    # Time: O(nlogn) and Space: O(n)
    """
    We have four cases:
    1. x is not present in the list and is smaller than the first element in arr
    2. x is not present in the list and is greater than the last element in arr
    3. x is not present in the list and lies between the first and the last element of the arr.
    4. x is present in the list.
    """

    # Case 1
    if x < arr[0]:
        return arr[:k]
    # Case 2
    if x > arr[-1]:
        return arr[-k:]

    # Case 3 and 4
    # We try to find the closest index to x in the arr if x lies between the arr elements, irrespective of whether
    # it is present or not.
    x_idx = -1
    if arr[0] <= x <= arr[-1]:
        curr_abs_val = float("inf")
        for i in range(len(arr)):
            # We check the absolute difference
            if abs(arr[i] - x) < curr_abs_val:
                x_idx = i
                curr_abs_val = abs(arr[i] - x)

    # We store the closest element found
    res = [arr[x_idx]]
    # Now we take two pointers, one to the left and other to the right of the closest element, and start comparing them
    left_idx = x_idx - 1
    right_idx = x_idx + 1

    while left_idx >= 0 or right_idx < len(arr):
        # Check of result condition
        if len(res) == k:
            break
        # Getting the left val
        left_val = arr[left_idx] if left_idx >= 0 else float("inf")
        # getting the right val
        right_val = arr[right_idx] if right_idx < len(arr) else float("inf")
        # Comparing the val and adding the smallest
        if abs(left_val - x) <= abs(right_val - x):
            res.append(left_val)
            left_idx -= 1
        else:
            res.append(right_val)
            right_idx += 1
    # returning the sorted result
    return sorted(res)
