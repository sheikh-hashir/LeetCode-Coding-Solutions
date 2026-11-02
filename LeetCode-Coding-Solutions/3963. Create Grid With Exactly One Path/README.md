# Deterministic Grid Traversal with Boundary Safety

# Intuition
To ensure there is exactly one valid path from the top-left to the bottom-right corner, systematically construct a single, deterministic trail of free cells (`.`) while filling the rest of the grid with obstacles (`#`). By restricting the free cells to a single, continuous line with no branches, eliminate any possibility of alternative routes or deviations.

# Approach
1. Initialize an m × n grid filled entirely with obstacle characters (`#`).
2. Trace a path starting from the top-left corner `(0, 0)` using two pointers to keep track of the current position (`row`, `colume`).
3. Advance through the grid systematically, dynamically updating directions to navigate toward the bottom-right corner `(m - 1, n - 1)`.
4. Include boundary safety checks to ensure that once a pointer hits an edge (the last row or the last column), it stops alternating and routes directly to the final cell.
5. Convert the final 2D list of characters into a list of strings matching the required output format.

# Complexity
- Time complexity:
`O(m x n)`
Initializing the grid takes `O(m x n)` time. The path tracing loop iterates linearly bounded by the dimensions of the grid, and transforming the matrix rows into individual strings takes `O(m x n)` time.

- Space complexity:
`O(m x n)`
The solution creates and holds an `m × n` matrix of characters alongside the final list of constructed strings.

# Code
```python3 []
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        result = [["#"] * n for _ in range(m)]

        row, colume = 0, 0
        count = 0

        while row < m and colume < n:
            result[row][colume] = "."

            if row == m - 1:
                colume += 1
            elif colume == n - 1:
                row += 1
            elif count % 2 == 0:
                colume += 1
            else:
                row += 1

            count += 1

        return ["".join(r) for r in result]
```
