# Topics
- Hash Table
- Depth-First Search
- Graph
- Python3

# Intuition
- The problem requires removing the maximum number of stones such that there is at least one stone in the same row or column as the removed one.
- This can be visualized as identifying connected components (groups of stones connected by rows or columns) and counting them.

<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Graph Representation:**
  - The problem can be seen as a graph problem where each stone is a node.
  - An edge exists between two stones if they share the same row or column.
  - Our task is to find the connected components in this graph. A connected component is a group of stones that are directly or indirectly connected through shared rows or columns.

- **Adjacency Lists:**
  - To efficiently find connected components, we need to represent the graph using adjacency lists:
    - Row adjacency list (`row_dict`): Maps each row to a list of stones (nodes) that are in that row.
    - Column adjacency list (`col_dict`): Maps each column to a list of stones (nodes) that are in that column.

- **Depth-First Search (DFS):**
  - We use DFS to traverse the graph and find all the stones in a connected component.
  - For each unvisited stone (node), we start a DFS that visits all stones connected to it (either in the same row or the same column).
  - During DFS, we mark the stones as visited to avoid revisiting them.

- **Counting Connected Components:**
  - The number of connected components corresponds to the number of groups of stones that are interconnected.
  - At least one stone from each connected component must remain, so the maximum number of stones that can be removed is equal to the total number of stones minus the number of connected components.

- **Final Calculation:**
  - The formula to calculate the number of stones that can be removed is:
    - `Max stones removed = Total stones − Number of connected components`
    - This is because, within each connected component, you can remove all stones except one.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of stones. We visit each stone once during DFS.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` for storing the adjacency lists and visited set.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
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

```
