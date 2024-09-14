from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        result = 0

        def match_coordinates(coordinates: list):
            return all(
                (grid1[coordinate[0]][coordinate[1]] == 1 for coordinate in coordinates)
            )

        def dfs(i: int, j: int, coordinates: list):
            if (
                i < 0
                or i >= len(grid2)
                or j < 0
                or j >= len(grid2[i])
                or grid2[i][j] != 1
            ):
                return

            grid2[i][j] = -1  # Mark the cell as visited
            coordinates.append((i, j))
            dfs(i + 1, j, coordinates)
            dfs(i - 1, j, coordinates)
            dfs(i, j + 1, coordinates)
            dfs(i, j - 1, coordinates)

        for i, row in enumerate(grid2):
            for j, cell in enumerate(row):
                if cell == 1:
                    coordinates = []
                    dfs(i, j, coordinates)
                    if match_coordinates(coordinates):
                        result += 1
        return result
