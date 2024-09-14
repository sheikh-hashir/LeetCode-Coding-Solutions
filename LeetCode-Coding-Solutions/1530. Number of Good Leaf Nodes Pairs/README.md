# Topics
- Tree
- Depth-First Search
- Binary Tree
- Python3

# Intuition
- The goal is to count the number of valid pairs of leaf nodes in a binary tree where the distance between them does not exceed a given value.
- The approach involves traversing the tree and collecting distances of leaf nodes from each subtree.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Depth-First Search (DFS):**
  - Implement a DFS to traverse the tree and collect distances of leaf nodes.
- **Collect Distances:**
  - For each node, compute the distances from its left and right subtrees' leaf nodes.
- **Count Valid Pairs:**
  - Check all pairs of distances from left and right subtrees to see if their sum is within the allowed distance.
- **Update Distances:**
  - Increment the distances from the current node and propagate them up to the parent nodes.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n^2)`, where `n` is the number of nodes. Each pair of distances is checked, leading to a quadratic complexity.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(h)`, where `h` is the height of the tree. This accounts for the space used by the recursion stack and temporary lists.

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0

        def dfs(node: TreeNode):
            if not node:
                return []

            # If the node is a leaf, return a list with distance 1 (from leaf to its parent)
            if not node.left and not node.right:
                return [1]

            # Collect distances from leaf nodes for left and right subtrees
            left_distances = dfs(node.left)
            right_distances = dfs(node.right)

            print(node.val, left_distances, right_distances)

            # Check all pairs of leaf nodes from left and right subtrees
            for l in left_distances:
                for r in right_distances:
                    if l + r <= distance:
                        self.count += 1

            # Increment distances by 1 (to account for the current node) and return
            return [d + 1 for d in left_distances + right_distances]

        dfs(root)
        return self.count
```