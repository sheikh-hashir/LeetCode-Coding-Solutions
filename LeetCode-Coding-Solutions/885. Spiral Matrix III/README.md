# Topics
- Array
- Matrix
- Simulation
- Python3

# Intuition
- To solve the problem of generating a spiral matrix starting from a given position
- The main idea is to simulate the spiral traversal by expanding the matrix in four possible directions (right, down, left, and up) while keeping track of the boundaries and ensuring the position is valid.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Initialize Directions:**
  - We use a list of direction vectors to handle movement in the spiral pattern. These directions represent right, down, left, and up, respectively:
    - `(0, 1)` represents moving right.
    - `(1, 0)` represents moving down.
    - `(0, -1)` represents moving left.
    - `(-1, 0)` represents moving up.

```
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

```

- **Spiral Traversal:**
  - The outer while loop continues until we have visited all cells in the matrix, i.e., until `len(result)` is equal to `rows * cols`.
  - Inside the loop, we handle the traversal in phases of directions:
    - Each phase consists of two iterations, where the number of steps in each direction is managed by the `step` variable.
    - For each phase:
      - Move in the current direction for the number of steps specified by step.
      - After moving, rotate the direction to the next one in the sequence. This is done using:
      - ```direction.append(direction.pop(0))```
      - This operation rotates the direction vector list, effectively changing the direction of traversal.
    - After completing one full cycle of directions (right, down, left, up), increase the `step` size to expand the spiral. This ensures that the spiral grows outward as needed.

- **Boundary Check:**
  - The `is_valid` function ensures that we only append positions to the `result` list if they are within the matrix boundaries:
```
def is_valid(x: int, y: int) -> bool:
    return 0 <= x < rows and 0 <= y < cols
```

- **Termination:**
    - The process continues until we have visited all cells in the matrix (``len(result) < rows * cols``), ensuring we don't add duplicate or out-of-bound positions.


# Key Points
- **Direction Rotation:**
  - By rotating the direction vectors after each phase, we handle the change in movement direction systematically.
  - **Step Size Increment:** Increasing the `step` size after each full cycle of directions ensures that the spiral expands outward correctly.
  - **Boundary Handling:** The `is_valid` function prevents adding positions outside the matrix boundaries.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(m⋅n)`, where `m` is the number of rows and `n` is the number of columns. This is because we visit each cell in the matrix exactly once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(m⋅n)`, where `m` is the number of rows and `n` is the number of columns. This is due to the space needed to store the result matrix.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def is_valid(x: int, y: int) -> bool:
            return 0 <= x < rows and 0 <= y < cols

        result = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        x, y = rStart, cStart
        step = 1

        while len(result) < rows * cols:
            for _ in range(2):  # Each step has two phases (right and down or left and up)
                for _ in range(step):
                    if is_valid(x, y):
                        result.append([x, y])
                    x += direction[0][0]
                    y += direction[0][1]
                direction.append(direction.pop(0))  # Rotate direction

            step += 1  # Increase the step size after completing a full cycle

        return result

```