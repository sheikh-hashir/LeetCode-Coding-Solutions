from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Create a set to track visited stones
        visited = set()

        # Create adjacency lists for rows and columns
        row_dict = {}
        col_dict = {}

        # Build the adjacency lists
        for r, c in stones:
            if r not in row_dict:
                row_dict[r] = []
            if c not in col_dict:
                col_dict[c] = []
            row_dict[r].append((r, c))
            col_dict[c].append((r, c))

        # Helper function to perform DFS
        def dfs(r, c):
            # If this stone has already been visited, return
            if (r, c) in visited:
                return
            # Mark this stone as visited
            visited.add((r, c))
            # Visit all stones in the same row
            for nr, nc in row_dict[r]:
                dfs(nr, nc)
            # Visit all stones in the same column
            for nr, nc in col_dict[c]:
                dfs(nr, nc)

        # Count the number of connected components
        num_components = 0
        for r, c in stones:
            if (r, c) not in visited:
                # Start a DFS from each unvisited stone
                dfs(r, c)
                num_components += 1

        # The maximum number of stones that can be removed is
        # total stones - number of connected components
        return len(stones) - num_components
