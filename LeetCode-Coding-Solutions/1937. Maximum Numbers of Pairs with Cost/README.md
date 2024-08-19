# Topics
- Dynamic Programming
- Array
- Python3

# Approach
- **Dynamic Programming:**
  - We can use dynamic programming to solve this problem by iterating over each row and computing the maximum possible points that can be achieved at each cell.
- **Two Passes:** For each row, we perform two passes:
  - **Left to Right:**
    - This pass ensures that moving rightwards in the row from the previous row's maximums doesn't incur a penalty greater than what has already been computed.
  - **Right to Left:**
    - This pass handles the potential penalty when moving leftwards.
- **Update Points:**
  - After adjusting for penalties using the two passes, we update the points for the current row by adding the maximum values computed in the previous row.
- **Final Answer:**
  - The maximum value in the last row of the grid will be the answer, representing the highest points achievable.

<!-- Describe your approach to solving the problem. -->
# Dry Run

- **Initial Input:**
```
points = [[5, 2, 1, 2],
          [2, 1, 5, 2],
          [5, 5, 5, 0]]
```
- **Step-by-Step Dry Run:**
  - **First Row (Initial):**
    - The first row remains unchanged as it serves as the base for calculating the next rows.
```
points = [[5, 2, 1, 2],
          [2, 1, 5, 2],
          [5, 5, 5, 0]]

```
- **Second Row (idx = 1):**
  - **Calculate `left_max` for the second row:**
    - Start from the first element in the second row:
      - `left_max[0] = points[0][0] = 5`
      - `left_max[1] = max(left_max[0] - 1, points[0][1]) = max(5 - 1, 2) = 4`
      - `left_max[2] = max(left_max[1] - 1, points[0][2]) = max(4 - 1, 1) = 3`
      - `left_max[3] = max(left_max[2] - 1, points[0][3]) = max(3 - 1, 2) = 2`

```
left_max = [5, 4, 3, 2]
```

  - **Calculate `right_max` for the second row:**
    - **Start from the last element in the second row:**
      - `right_max[3] = points[0][3] = 2`
      - `right_max[2] = max(right_max[3] - 1, points[0][2]) = max(2 - 1, 1) = 1`
      - `right_max[1] = max(right_max[2] - 1, points[0][1]) = max(1 - 1, 2) = 2`
      - `right_max[0] = max(right_max[1] - 1, points[0][0]) = max(2 - 1, 5) = 5`
```
right_max = [5, 2, 1, 2]
```

  - **Update the values for the second row:**
    - `points[1][0] += max(left_max[0], right_max[0]) = 2 + 5 = 7`
    - `points[1][1] += max(left_max[1], right_max[1]) = 1 + 4 = 5`
    - `points[1][2] += max(left_max[2], right_max[2]) = 5 + 3 = 8`
    - `points[1][3] += max(left_max[3], right_max[3]) = 2 + 2 = 4`


- Third Row (idx = 2):
  - Calculate `left_max` for the third row:
    - Start from the first element in the third row:
      - `left_max[0] = points[1][0] = 7`
      - `left_max[1] = max(left_max[0] - 1, points[1][1]) = max(7 - 1, 5) = 6`
      - `left_max[2] = max(left_max[1] - 1, points[1][2]) = max(6 - 1, 8) = 8`
      - `left_max[3] = max(left_max[2] - 1, points[1][3]) = max(8 - 1, 4) = 7`
```
left_max = [7, 6, 8, 7]
```

  - Calculate `right_max` for the third row:
    - Start from the last element in the third row:
      - `right_max[3] = points[1][3] = 4`
      - `right_max[2] = max(right_max[3] - 1, points[1][2]) = max(4 - 1, 8) = 8`
      - `right_max[1] = max(right_max[2] - 1, points[1][1]) = max(8 - 1, 5) = 7`
      - `right_max[0] = max(right_max[1] - 1, points[1][0]) = max(7 - 1, 7) = 7`
```
right_max = [7, 7, 8, 4]
```

  - Update the values for the third row:
    - `points[2][0] += max(left_max[0], right_max[0]) = 5 + 7 = 12`
    - `points[2][1] += max(left_max[1], right_max[1]) = 5 + 7 = 12`
    - `points[2][2] += max(left_max[2], right_max[2]) = 5 + 8 = 13`
    - `points[2][3] += max(left_max[3], right_max[3]) = 0 + 7 = 7`
```
points = [[5, 2, 1, 2],
          [7, 5, 8, 4],
          [12, 12, 13, 7]]
```

- **Final Result:**
  - The maximum value in the last row is `13`.

# Complexity
- Time complexity: `O(n×m)`, where `n` is the number of rows and `m` is the number of columns. We iterate over each cell in the matrix multiple times (specifically, twice per row).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)` since the solution modifies the input `points` matrix in place and doesn't require any extra space proportional to the input size.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows = len(points)
        cols = len(points[0])

        # Iterate over each row starting from the second one
        for i in range(1, rows):
            # Left to right pass
            for j in range(1, cols):
                points[i-1][j] = max(points[i-1][j], points[i-1][j-1] - 1)

            # Right to left pass
            for j in range(cols - 2, -1, -1):
                points[i-1][j] = max(points[i-1][j], points[i-1][j+1] - 1)

            # Calculate new points for the current row
            for j in range(cols):
                points[i][j] += points[i-1][j]

        # The answer is the maximum value in the last row
        return max(points[-1])

```