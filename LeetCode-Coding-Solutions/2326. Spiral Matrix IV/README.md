# Topics
- Array
- Linked List
- Matrix
- Simulation
- Python3

# Intuition
- The problem requires us to fill a matrix in a spiral order using values from a linked list.
- Since spiral traversal involves moving in four directions (right, down, left, and up), we need to carefully manage these transitions while filling the matrix.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Initialize a 2D matrix filled with `-1` to represent unfilled cells.
- Define directions for moving right, down, left, and up.
- Traverse the matrix, placing values from the linked list into the matrix in a spiral order:
  - Move in the current direction until you hit a boundary or a cell that has already been filled.
  - Change direction when necessary.
- Continue this process until the linked list is exhausted or the matrix is completely filled.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(m×n)`, where `m` is the number of rows and `n` is the number of columns, as we iterate through the entire matrix.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(m×n)` to store the matrix.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1 for _ in range(n)] for _ in range(m)]

        # Directions for right, down, left, and up respectively
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        row, column = 0, 0
        path = 0

        while head:
            result[row][column] = head.val
            head = head.next

            dr, dc = directions[path]
            next_row, next_column = row + dr, column + dc

            # Check if the next move is out of bounds or the cell has already been visited
            if not (0 <= next_row < m and 0 <= next_column < n and result[next_row][next_column] == -1):
                # Change direction
                path = (path + 1) % 4
                dr, dc = directions[path]
                next_row, next_column = row + dr, column + dc

            row, column = next_row, next_column

        return result

```
