# Topics
- Array
- Matrix
- Python3

# Intuition
- The problem can be visualized as a grid where guards and walls block cells. Guards can "guard" cells in straight lines (up, down, left, right) until a wall or another guard blocks their view. 
- The goal is to determine the number of unguarded cells in the grid.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Grid Initialization:**
  - Create a grid to represent the matrix, initializing all cells as unguarded (`0`). Represent guards as `1` and walls as `-1`.

- **Marking Guarded Cells:**
  - For each guard, traverse in all four directions (up, down, left, right) until hitting a boundary, a wall, or another guard. Mark all reachable cells as guarded (`2`).

- **Direction Traversal:**
  - Use a helper function (`dfs`) to traverse in a specified direction. Continue marking cells until an obstacle is encountered.

- **Counting Unguarded Cells:**
  - After marking all guarded cells, iterate through the grid to count cells that remain unguarded (`0`).
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
    - Each guard performs DFS in four directions. In the worst case, they traverse all unguarded cells in their path.
    - Total complexity: `O(m⋅n)`, where m and n are the dimensions of the grid.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
    - The grid itself uses `O(m⋅n)` space.
    - No additional space is required for recursion since the traversal is iterative.
    - Total space complexity: `O(m⋅n)`. 
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        def dfs(i, j, di, dj):
            """Mark cells in the direction (di, dj) as guarded until hitting a wall or edge."""
            while (
                0 <= i < m and 0 <= j < n and matrix[i][j] != -1 and matrix[i][j] != 1
            ):
                if matrix[i][j] == 0:  # Only mark empty cells as guarded
                    matrix[i][j] = 2
                i += di
                j += dj

        # Initialize the grid
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        # Place guards and walls on the grid
        for position in guards:
            matrix[position[0]][position[1]] = 1

        for position in walls:
            matrix[position[0]][position[1]] = -1

        # Perform DFS for each guard in all four directions
        for x, y in guards:
            dfs(x - 1, y, -1, 0)  # Up
            dfs(x + 1, y, 1, 0)  # Down
            dfs(x, y - 1, 0, -1)  # Left
            dfs(x, y + 1, 0, 1)  # Right

        # Count unguarded cells
        unguarded_count = sum(cell == 0 for row in matrix for cell in row)
        return unguarded_count

```