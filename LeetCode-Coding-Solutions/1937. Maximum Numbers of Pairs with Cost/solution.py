from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])

        # Iterate over each row starting from the second one
        for i in range(1, rows):
            # Left to right pass
            for j in range(1, cols):
                points[i - 1][j] = max(points[i - 1][j], points[i - 1][j - 1] - 1)

            # Right to left pass
            for j in range(cols - 2, -1, -1):
                points[i - 1][j] = max(points[i - 1][j], points[i - 1][j + 1] - 1)

            # Calculate new points for the current row
            for j in range(cols):
                points[i][j] += points[i - 1][j]

        # The answer is the maximum value in the last row
        return max(points[-1])
