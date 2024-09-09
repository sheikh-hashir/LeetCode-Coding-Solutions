from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
            if not (
                0 <= next_row < m
                and 0 <= next_column < n
                and result[next_row][next_column] == -1
            ):
                # Change direction
                path = (path + 1) % 4
                dr, dc = directions[path]
                next_row, next_column = row + dr, column + dc

            row, column = next_row, next_column

        return result
