from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check_magic_square(matrix, i, j):
            sub_matrix = [row[j : j + 3] for row in matrix[i : i + 3]]
            seen_values = set()
            for row in sub_matrix:
                for value in row:
                    if value < 1 or value > 9 or value in seen_values:
                        return False
                    seen_values.add(value)

            # Calculate row sums, column sums, and diagonal sums
            row_sums = [sum(row) for row in sub_matrix]
            col_sums = [sum(sub_matrix[i][j] for i in range(3)) for j in range(3)]
            main_diagonal_sum = sum(sub_matrix[i][i] for i in range(3))
            secondary_diagonal_sum = sum(sub_matrix[i][2 - i] for i in range(3))

            # Combine all sums into one list and check if they are all equal
            all_sums = row_sums + col_sums + [main_diagonal_sum, secondary_diagonal_sum]
            return all(x == all_sums[0] for x in all_sums)

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        # Iterate over all possible 3x3 sub_matrices in the grid
        for i in range(rows - 2):  # -2 because we're considering 3x3 sub_matrices
            for j in range(cols - 2):
                if check_magic_square(grid, i, j):
                    count += 1
        return count
