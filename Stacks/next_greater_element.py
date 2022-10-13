"""
Write a function that takes in an array of integers and returns a new array containing, at each index, the next
element in the input array that's greater than the element at that index in the input array.

Input: [2, 5, -3, -4, 6, 7, 2]
Output: [5, 6, 6, 6, 7, -1, 5]

"""


def nextGreaterElement(array):
    # Time = Space = O(n)
    """
    Logic:
    As we iterate, we check whether the current element is greater than the top element in the stack, if yes
    then we keep popping the stack elements and replace its value with the current element.
    If no, then we simply add the current element to the stack.
    We Loop 2x length because for last element the next greater element could be on the starting of the array.
    """

    stack = []
    # Result initialized with -1, incase there is not greater element then its value will be -1
    result = [-1 for i in array]

    for i in range(2 * len(array)):
        # Getting the index in the correct range.
        idx = i % len(array)
        # If the stack is empty, then we add the index of the current element.
        if not stack:
            stack.append(idx)
        else:
            # Else, we check whether the top stack element is smaller than this current element.
            if array[stack[-1]] < array[idx]:
                # We keeping popping the stack elements until the above condition is true.
                while stack and array[stack[-1]] < array[idx]:
                    stackIdx = stack.pop()
                    # Update the next greater element for the stack elements
                    result[stackIdx] = array[idx]
            # Finally, add the current element index to the stack.
            stack.append(idx)
    return result
