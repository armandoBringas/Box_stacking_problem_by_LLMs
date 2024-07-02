def max_stack_height(boxes):
    # Sort boxes based on area (width * depth) in descending order
    boxes.sort(key=lambda x: x[0] * x[2], reverse=True)

    n = len(boxes)
    # Initialize heights with individual box heights
    heights = [box[1] for box in boxes]

    # Iterate through each box and calculate the maximum stack height
    for i in range(1, n):
        for j in range(i):
            # Check if the current box can be stacked on top of the previous box
            if (boxes[i][0] < boxes[j][0] and
                    boxes[i][1] < boxes[j][1] and
                    boxes[i][2] < boxes[j][2]):
                # Update the height of the current box
                heights[i] = max(heights[i], heights[j] + boxes[i][1])

    # Return the maximum height found
    return max(heights)


# Example usage with the given box dimensions
boxes = [
    (50, 45, 20),
    (95, 37, 53),
    (45, 23, 12)
]

print(f"Maximum possible stack height: {max_stack_height(boxes)}")

# Explanation:
# 1. Sorting: The boxes are sorted based on their base area (width * depth) in descending order.
# 2. Initialize Heights: Create an array to store the maximum height of the stack ending with each box.
# 3. Nested Loop: Iterate through each pair of boxes to check if one can be stacked on top of the other.
# 4. Update Heights: If a box can be stacked on another, update the height of the stack ending with the current box.
# 5. Return Maximum Height: The result is the maximum value in the heights array.

# Time Complexity:
# - Sorting: O(n log n) where n is the number of boxes.
# - Nested Loop: Each pair of boxes is compared, leading to O(n^2) comparisons.
# - Overall: O(n^2) dominated by the nested loop.

# Space Complexity:
# - The space complexity is O(n) for the heights array to store the maximum heights of the stacks.
# - Overall: O(n).
