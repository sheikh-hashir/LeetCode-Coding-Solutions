# Topics
- Tree
- Depth First Search
- Sorting
- Binary Tree
- Python3

# Intuition
- The goal is to find the sum of all nodes at each level of a binary tree and then determine the k-th largest level sum.
- This suggests that we need to traverse the tree, calculate the sum for each level, and sort those sums to find the required k-th largest sum.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- We can perform a depth-first search (DFS) traversal of the tree. While doing this, we will keep track of the sum of node values at each level.
- Use a dictionary `level_sums` where the keys represent the levels and the values are the sums of node values at that level.
- Traverse the tree recursively and update the sum for each level.
- Once the traversal is complete, sort the sums of each level in descending order and return the k-th largest sum. If k is larger than the number of levels, return `-1`.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(nlogn)`, where n is the number of levels in the tree. This is because we traverse all the nodes once `(O(n))` and then sort the level sums `(O(n \log n))`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` because of the dictionary that stores sums for each level and the recursion stack for DFS.
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = {}

        def dfs(node, level):
            if not node:
                return

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            level_sums[level] = level_sums.get(level, 0) + node.val

        dfs(root, 0)
        return (
            list(sorted(level_sums.items(), key=lambda x: x[1], reverse=True))[k - 1][1]
            if k <= len(level_sums)
            else -1
        )

```