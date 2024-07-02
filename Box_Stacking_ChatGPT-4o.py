class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth


def can_be_above(bottom, top):
    # A box can be stacked on top of another if it is strictly smaller in all dimensions
    return bottom.width > top.width and bottom.height > top.height and bottom.depth > top.depth


def max_stack_height(boxes):
    n = len(boxes)

    # Sort boxes by height in descending order
    boxes.sort(key=lambda box: box.height, reverse=True)

    # Array to store the maximum possible height of stack starting from each box
    max_heights = [0] * n

    def stack_height(index):
        # If the height has already been computed, return it
        if max_heights[index] != 0:
            return max_heights[index]

        max_height = 0
        # Try to place each box on top of the current box
        for i in range(index + 1, n):
            if can_be_above(boxes[index], boxes[i]):
                max_height = max(max_height, stack_height(i))

        # Include the current box's height in the total height
        max_heights[index] = max_height + boxes[index].height
        return max_heights[index]

    max_height = 0
    # Calculate the maximum stack height for each box as the base
    for i in range(n):
        max_height = max(max_height, stack_height(i))

    return max_height


# Example usage with the given box dimensions
boxes = [
    Box(50, 45, 20),
    Box(95, 37, 53),
    Box(45, 23, 12)
]

print("The height of the tallest stack is:", max_stack_height(boxes))

# Explanation:
# 1. Box Class: Represents a box with width, height, and depth.
# 2. can_be_above Function: Determines if one box can be placed on top of another by comparing their dimensions.
# 3. max_stack_height Function:
#    - Sorting: Boxes are sorted by their height in descending order to facilitate the stacking process.
#    - Dynamic Programming Array (max_heights): Stores the maximum possible stack height starting from each box.
#    - Recursive Helper Function (stack_height): Computes the maximum height for a stack starting with the given box using a top-down recursive approach with memoization.
#    - Main Loop: Iterates through all boxes, computing the maximum stack height starting with each one, and returns the maximum value found.

# Time Complexity:
# - Sorting: O(n log n) where n is the number of boxes.
# - Recursive Calls: Each box can potentially involve a recursive call to every other box, leading to a time complexity of O(n^2).
# - Overall: O(n^2) dominated by the nested recursive calls.

# Space Complexity:
# - The space complexity is O(n) for the max_heights array to store the maximum heights.
# - The call stack for recursion can go up to O(n) in the worst case.
# - Overall: O(n) for both the array and the recursive stack.
