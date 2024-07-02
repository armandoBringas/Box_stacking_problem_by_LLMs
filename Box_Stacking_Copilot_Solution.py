class Box:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

def can_be_above(bottom, top):
    return bottom.width > top.width and bottom.height > top.height and bottom.depth > top.depth

def max_stack_height(boxes):
    boxes.sort(key=lambda box: box.width * box.depth, reverse=True)
    n = len(boxes)
    max_heights = [0] * n

    def stack_height(index):
        if max_heights[index] != 0:
            return max_heights[index]
        max_height = 0
        for i in range(index + 1, n):
            if can_be_above(boxes[index], boxes[i]):
                max_height = max(max_height, stack_height(i))
        max_heights[index] = max_height + boxes[index].height
        return max_heights[index]

    return max(stack_height(i) for i in range(n))

# Example usage with the given box dimensions
boxes = [
    Box(50, 45, 20),
    Box(95, 37, 53),
    Box(45, 23, 12)
]

print("The height of the tallest stack is:", max_stack_height(boxes))