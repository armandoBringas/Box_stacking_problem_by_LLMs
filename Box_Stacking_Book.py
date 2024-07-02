from typing import List

class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def can_be_above(self, other):
        # A box can be stacked on top of another if it is strictly smaller in all dimensions
        return self.width < other.width and self.height < other.height and self.depth < other.depth

def create_stack(boxes: List[Box]) -> int:
    # Sort the boxes by their height in descending order
    boxes.sort(key=lambda box: box.height, reverse=True)
    # Initialize the stack_map to store the maximum heights
    stack_map = [0] * len(boxes)
    # Start the recursive process to calculate the maximum stack height
    return create_stack_recursive(boxes, None, 0, stack_map)

def create_stack_recursive(boxes: List[Box], bottom: Box, offset: int, stack_map: List[int]) -> int:
    # If we've processed all boxes, return 0
    if offset >= len(boxes):
        return 0

    # Current box being considered as the new bottom
    new_bottom = boxes[offset]
    height_with_bottom = 0

    # Check if the current box can be placed on top of the bottom box
    if bottom is None or new_bottom.can_be_above(bottom):
        # Use memoization to avoid recalculating the height
        if stack_map[offset] == 0:
            # Calculate the height of the stack with the current box as the bottom
            stack_map[offset] = create_stack_recursive(boxes, new_bottom, offset + 1, stack_map)
            # Include the height of the current box
            stack_map[offset] += new_bottom.height
        # Update the height if the current box is used as the bottom
        height_with_bottom = stack_map[offset]

    # Calculate the height of the stack without using the current box as the bottom
    height_without_bottom = create_stack_recursive(boxes, bottom, offset + 1, stack_map)

    # Return the maximum height of the two possibilities
    return max(height_with_bottom, height_without_bottom)

# Example usage with the given box dimensions
boxes = [
    Box(50, 45, 20),
    Box(95, 37, 53),
    Box(45, 23, 12)
]

print("The height of the tallest stack is:", create_stack(boxes))

# Explanation:
# 1. Box Class: Represents a box with width, height, and depth.
# 2. can_be_above Method: Determines if one box can be placed on top of another by comparing their dimensions.
# 3. create_stack Function:
#    - Sorts the boxes by their height in descending order to facilitate the stacking process.
#    - Initializes the stack_map to store the maximum heights.
#    - Calls the recursive helper function create_stack_recursive.
# 4. create_stack_recursive Function:
#    - Computes the maximum height for a stack starting with the given box using a top-down recursive approach with memoization.
#    - Checks if the current box can be the new bottom and calculates the height with and without the current box as the bottom.
#    - Returns the maximum of the two heights.

# Time Complexity:
# - Sorting: O(n log n) where n is the number of boxes.
# - Recursive Calls: Each box can potentially involve a recursive call to every other box, leading to a time complexity of O(n^2).
# - Overall: O(n^2) dominated by the nested recursive calls.

# Space Complexity:
# - The space complexity is O(n) for the stack_map array to store the maximum heights.
# - The call stack for recursion can go up to O(n) in the worst case.
# - Overall: O(n) for both the array and the recursive stack.
