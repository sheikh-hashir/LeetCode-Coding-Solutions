# Topics
- Hash Table
- Array
- Math
- Matrix
- Python3

# Approach
- **Iterate Through Possible Sub-matrices:**
  - We scan the grid and consider every possible 3x3 sub_matrix by sliding a window over the grid.
- **Check for Magic Square:**
  - For each 3x3 sub_matrix, we:
    - Ensure all values are between 1 and 9 and are distinct.
    - Compute the sums of all rows, columns, and diagonals.
    - Verify if all these sums are equal.
- **Count Valid Magic Squares:**
  - We count how many such valid 3x3 magic squares exist in the grid.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - `O((m−2)×(n−2)×9)` where `m` and `n` are the number of rows and columns of the grid, respectively. The sliding window requires checking each possible 3x3 sub_matrix, and for each sub_matrix, we perform a fixed amount of work (checking 9 elements and calculating sums).
  - This simplifies to approximately `O(m×n)` since the sliding window is applied across the entire grid.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - `O(1)`. We use a fixed amount of additional space regardless of the grid size, as we only track sums and a set of seen values.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def check_magic_square(matrix, i, j):
            sub_matrix = [row[j:j+3] for row in matrix[i:i+3]]
            seen_values = set()
            for row in sub_matrix:
                    for value in row:
                        if value < 1 or value > 9 or value in seen_values:
                            return False
                        seen_values.add(value)
            row_sums = [sum(row) for row in sub_matrix]
            col_sums = [sum(sub_matrix[i][j] for i in range(3)) for j in range(3)]
            main_diagonal_sum = sum(sub_matrix[i][i] for i in range(3))
            secondary_diagonal_sum = sum(sub_matrix[i][2-i] for i in range(3))
            all_sums = row_sums + col_sums + [main_diagonal_sum, secondary_diagonal_sum]
            return all((x == all_sums[0] for x in all_sums))

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows-2):
            for j in range(cols-2):
                if check_magic_square(grid, i, j):
                    count+=1
        return count

```