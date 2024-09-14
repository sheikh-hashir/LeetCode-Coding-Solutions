# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
