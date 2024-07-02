from typing import List, Tuple


class Box:
    def __init__(self, width: int, height: int, depth: int):
        self.width = width
        self.height = height
        self.depth = depth

    def can_be_above(self, other: 'Box') -> bool:
        return self.width < other.width and self.height < other.height and self.depth < other.depth


def max_stack_height(boxes: List[Tuple[int, int, int]]) -> int:
    """
    Compute the height of the tallest possible stack of boxes.

    Args:
    boxes (List[Tuple[int, int, int]]): List of (width, height, depth) for each box.

    Returns:
    int: The maximum possible height of the stack.
    """
    # Convert input tuples to Box objects
    box_objects = [Box(*box) for box in boxes]

    # Sort boxes based on base area in descending order
    box_objects.sort(key=lambda b: b.width * b.depth, reverse=True)

    n = len(box_objects)
    max_heights = [0] * n

    def stack_height(index: int) -> int:
        """
        Recursive helper function to compute max stack height starting from a given index.

        Args:
        index (int): The starting index in the sorted box list.

        Returns:
        int: The maximum height of the stack starting from the given index.
        """
        # If we've already computed this subproblem, return the memoized result
        if max_heights[index] != 0:
            return max_heights[index]

        # Initialize with the height of the current box
        max_height = box_objects[index].height

        # Try stacking the current box on top of each of the remaining boxes
        for i in range(index + 1, n):
            if box_objects[i].can_be_above(box_objects[index]):
                max_height = max(max_height, box_objects[index].height + stack_height(i))

        # Memoize the result before returning
        max_heights[index] = max_height
        return max_height

    # Compute the maximum height starting from each box
    return max(stack_height(i) for i in range(n))


# Example usage
boxes = [(50, 45, 20), (95, 37, 53), (45, 23, 12)]
print(f"Maximum possible stack height: {max_stack_height(boxes)}")

"""
Time Complexity Analysis:
The time complexity is O(n^2) in the worst case, where n is the number of boxes.
The sorting step takes O(n log n), and the dynamic programming approach with memoization
takes O(n^2) in the worst case.

Space Complexity Analysis:
The space complexity is O(n) for the memoization array, plus O(n) additional space
for the call stack in the worst case of the recursion.

Key improvements in this corrected version:
1. Properly handles cases where larger boxes can be stacked on smaller ones.
2. Sorts boxes based on base area (width * depth) instead of height, which is more
   appropriate for this problem.
3. Uses memoization to avoid redundant calculations.
4. Considers all possible starting boxes to ensure the optimal solution is found.
"""