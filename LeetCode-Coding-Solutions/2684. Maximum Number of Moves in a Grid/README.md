# Topics
- Array
- Matrix
- Depth First Search
- Python3

# Intuition
- The problem requires finding the longest path of increasing values starting from any cell in the first column and moving only in specific directions.
- Using Depth-First Search (DFS) from each cell in the first column and caching intermediate results can help optimize the process by reusing previously computed paths.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Start from each cell in the first column.
- Use `DFS` to explore three possible moves: top-right, right, and bottom-right, each only if the move has a higher value than the current cell.
- Use caching (`lru_cache`) to store results from DFS calls, avoiding redundant calculations for each cell.
- Track the maximum number of moves across all possible starting cells.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: The DFS traversal has a time complexity of `O(m×n)` due to caching, where each cell is calculated only once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(m×n)`, needed for caching and recursion stack.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from typing import List
from functools import lru_cache

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            # Initialize the maximum count from the current position
            max_count = 0

            # Explore the three possible directions: top-right, right, and bottom-right
            if row - 1 >= 0 and column + 1 < cols and grid[row][column] < grid[row - 1][column + 1]:
                max_count = max(max_count, 1 + dfs(row - 1, column + 1))
            if column + 1 < cols and grid[row][column] < grid[row][column + 1]:
                max_count = max(max_count, 1 + dfs(row, column + 1))
            if row + 1 < rows and column + 1 < cols and grid[row][column] < grid[row + 1][column + 1]:
                max_count = max(max_count, 1 + dfs(row + 1, column + 1))

            return max_count

        # Start DFS from each cell in the first column
        max_moves = 0
        for row in range(rows):
            max_moves = max(max_moves, dfs(row, 0))

        return max_moves

```