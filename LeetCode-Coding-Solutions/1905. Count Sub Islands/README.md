# Topics
- Array
- Depth-First Search
- Matrix
- Python3

# Intuition
- The problem requires us to determine if a portion of an island in `grid2` is a sub-island of `grid1`.
- My initial thought was to traverse all the islands in `grid2` and check whether every cell in that island exists as land in grid1.
- If the entire island in `grid2` exists in `grid1`, then it counts as a sub-island.

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Depth-First Search (DFS):**
  - I use `DFS` to traverse each island in `grid2`.
  - This allows us to collect all the coordinates that make up the island.
- **Coordinate Matching:**
  - After gathering the coordinates of the current island in grid2, we compare them with `grid1`.
  - If all coordinates match land (1) in `grid1`, we count this as a sub-island.
- **Marking Visited Cells:**
  - During the `DFS`, I mark the visited cells in `grid2` with `-1` to avoid counting them again.
- **Result Calculation:**
  - For each island in `grid2` that matches fully with `grid1`, we increment the result counter.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(m×n)`, where `m` and `n` are the dimensions of the grids. This is because we visit each cell at most once during the DFS traversal.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(m×n)` in the worst case, which corresponds to the space used by the recursion stack during the DFS.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        result = 0

        def match_coordinates(coordinates: list):
            return all(
                (
                    grid1[coordinate[0]][coordinate[1]] == 1
                    for coordinate in coordinates
                )
            )

        def dfs(i: int, j: int, coordinates: list):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[i]) or grid2[i][j] != 1:
                return

            grid2[i][j] = -1  # Mark the cell as visited
            coordinates.append((i, j))
            dfs(i+1, j, coordinates)
            dfs(i-1, j, coordinates)
            dfs(i, j+1, coordinates)
            dfs(i, j-1, coordinates)

        for i, row in enumerate(grid2):
            for j, cell in enumerate(row):
                if cell == 1:
                    coordinates = []
                    dfs(i, j, coordinates)
                    if match_coordinates(coordinates):
                        result += 1
        return result

```