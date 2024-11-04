from functools import lru_cache
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            # Initialize the maximum count from the current position
            max_count = 0

            # Explore the three possible directions: top-right, right, and bottom-right
            if (
                row - 1 >= 0
                and column + 1 < cols
                and grid[row][column] < grid[row - 1][column + 1]
            ):
                max_count = max(max_count, 1 + dfs(row - 1, column + 1))
            if column + 1 < cols and grid[row][column] < grid[row][column + 1]:
                max_count = max(max_count, 1 + dfs(row, column + 1))
            if (
                row + 1 < rows
                and column + 1 < cols
                and grid[row][column] < grid[row + 1][column + 1]
            ):
                max_count = max(max_count, 1 + dfs(row + 1, column + 1))

            return max_count

        # Start DFS from each cell in the first column
        max_moves = 0
        for row in range(rows):
            max_moves = max(max_moves, dfs(row, 0))

        return max_moves
