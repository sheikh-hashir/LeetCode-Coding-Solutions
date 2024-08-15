from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        def is_valid(x: int, y: int) -> bool:
            return 0 <= x < rows and 0 <= y < cols

        result = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        x, y = rStart, cStart
        step = 1

        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    # Each step has two phases (right and down or left and up)
                    if is_valid(x, y):
                        result.append([x, y])
                    x += direction[0][0]
                    y += direction[0][1]
                direction.append(direction.pop(0))  # Rotate direction

            step += 1  # Increase the step size after completing a full cycle

        return result
