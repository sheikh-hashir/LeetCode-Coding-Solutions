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
