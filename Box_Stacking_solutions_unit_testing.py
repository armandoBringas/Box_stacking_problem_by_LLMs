import unittest


# Solution 1 (Claude 3.5 Sonnet)
def max_stack_height_s1(boxes):
    boxes.sort(key=lambda x: x[0] * x[2], reverse=True)
    n = len(boxes)
    heights = [box[1] for box in boxes]
    for i in range(1, n):
        for j in range(i):
            if (boxes[i][0] < boxes[j][0] and
                    boxes[i][1] < boxes[j][1] and
                    boxes[i][2] < boxes[j][2]):
                heights[i] = max(heights[i], heights[j] + boxes[i][1])
    return max(heights)


# Solution 2 (ChatGPT-4o)
class BoxS2:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth


def can_be_above_s2(bottom, top):
    return bottom.width > top.width and bottom.height > top.height and bottom.depth > top.depth


def max_stack_height_s2(boxes):
    n = len(boxes)
    boxes.sort(key=lambda box: box.height, reverse=True)
    max_heights = [0] * n

    def stack_height(index):
        if max_heights[index] != 0:
            return max_heights[index]
        max_height = 0
        for i in range(index + 1, n):
            if can_be_above_s2(boxes[index], boxes[i]):
                max_height = max(max_height, stack_height(i))
        max_heights[index] = max_height + boxes[index].height
        return max_heights[index]

    max_height = 0
    for i in range(n):
        max_height = max(max_height, stack_height(i))
    return max_height


# Solution 3 (Book)
class BoxS3:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def can_be_above(self, other):
        return self.width < other.width and self.height < other.height and self.depth < other.depth


def create_stack_s3(boxes):
    boxes.sort(key=lambda box: box.height, reverse=True)
    stack_map = [0] * len(boxes)
    return create_stack_recursive_s3(boxes, None, 0, stack_map)


def create_stack_recursive_s3(boxes, bottom, offset, stack_map):
    if offset >= len(boxes):
        return 0
    new_bottom = boxes[offset]
    height_with_bottom = 0
    if bottom is None or new_bottom.can_be_above(bottom):
        if stack_map[offset] == 0:
            stack_map[offset] = create_stack_recursive_s3(boxes, new_bottom, offset + 1, stack_map)
            stack_map[offset] += new_bottom.height
        height_with_bottom = stack_map[offset]
    height_without_bottom = create_stack_recursive_s3(boxes, bottom, offset + 1, stack_map)
    return max(height_with_bottom, height_without_bottom)


# Copilot Solution
class BoxCopilot:
    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth


def can_be_above_copilot(bottom, top):
    return bottom.width > top.width and bottom.height > top.height and bottom.depth > top.depth


def max_stack_height_copilot(boxes):
    boxes.sort(key=lambda box: box.width * box.depth, reverse=True)
    n = len(boxes)
    max_heights = [0] * n

    def stack_height(index):
        if max_heights[index] != 0:
            return max_heights[index]
        max_height = 0
        for i in range(index + 1, n):
            if can_be_above_copilot(boxes[index], boxes[i]):
                max_height = max(max_height, stack_height(i))
        max_heights[index] = max_height + boxes[index].height
        return max_heights[index]

    return max(stack_height(i) for i in range(n))


class TestBoxStacking(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([(50, 45, 20), (95, 37, 53), (45, 23, 12)], 68),
            ([(4, 6, 7), (1, 2, 3), (4, 5, 6), (10, 12, 32)], 20),
            ([(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)], 14),
        ]

    def test_solution_1(self):
        for boxes, expected in self.test_cases:
            with self.subTest(boxes=boxes, expected=expected):
                self.assertEqual(max_stack_height_s1(boxes), expected)

    def test_solution_2(self):
        for boxes, expected in self.test_cases:
            with self.subTest(boxes=boxes, expected=expected):
                boxes_s2 = [BoxS2(*box) for box in boxes]
                self.assertEqual(max_stack_height_s2(boxes_s2), expected)

    def test_solution_3(self):
        for boxes, expected in self.test_cases:
            with self.subTest(boxes=boxes, expected=expected):
                boxes_s3 = [BoxS3(*box) for box in boxes]
                self.assertEqual(create_stack_s3(boxes_s3), expected)

    def test_solution_copilot(self):
        for boxes, expected in self.test_cases:
            with self.subTest(boxes=boxes, expected=expected):
                boxes_copilot = [BoxCopilot(*box) for box in boxes]
                self.assertEqual(max_stack_height_copilot(boxes_copilot), expected)


if __name__ == '__main__':
    unittest.main()
