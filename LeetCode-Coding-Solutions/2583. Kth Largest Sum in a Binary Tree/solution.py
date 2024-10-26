from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
