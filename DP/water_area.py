"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.

"""


def waterArea(heights):
    # Time: O(n) and Space: O(1)
    # Edge case
    if not heights:
        return 0
    """Logic: We create two pointers, left and right. If the height of left < right say, then we know that
    we the water height can be max till left's height. So we focus on left.
    This is what we do at left: We can want calculate the water which is trapped to the right side of the left building.
    So we move towards the left + 1 building, ideally the current left should be greater than the next building for the
    water to accumulate in between but that may not happen all the time. So we maintain a variable called 
    "left_max" which stores the max height of (current, next) building. Now to calculate the water between the
    current and next building, we do left_max - next_building_height.
    
    Same logic is repeated for the right side pointer. At right, we want to store the water to the left of the building.
    Because towards the right, the water will spill down. Think about it again using a pen and paper.
    
    """
    left_max = heights[0]
    right_max = heights[-1]
    left_idx = 0
    right_idx = len(heights) - 1
    area = 0  # final result

    # Comparing two different buildings only.
    while left_idx < right_idx:
        # If the left building is smaller than right
        if heights[left_idx] < heights[right_idx]:
            # First move to the next building
            left_idx += 1
            # Now check which one has max height
            left_max = max(left_max, heights[left_idx])
            # Update the area, as we want the water to the right of the building.
            area += left_max - heights[left_idx]
        else:
            # First move to the previous building
            right_idx -= 1
            # Now check which one has max height
            right_max = max(right_max, heights[right_idx])
            # Update the area, as we want the water to the left of the building.
            area += right_max - heights[right_idx]

    return area


print(waterArea([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
