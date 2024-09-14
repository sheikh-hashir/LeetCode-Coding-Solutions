# Topics
- Tree
- Stack
- Depth-First Search
- Binary Tree
- Python3


# Intuition
- The postorder traversal of a binary tree involves visiting the left subtree, then the right subtree, and finally the root node.
- This leads to a depth-first search approach, where you recursively traverse the tree, starting with the left child, then the right child, and then process the current node.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Recursive Traversal:**
  - We use a recursive helper function, `post_order`, to perform the traversal.
- **Base Case:**
  - If the node is None, we return from the function.
- **Recursive Calls:**
  - Traverse the left subtree by calling `post_order(node.left)`.
  - Traverse the right subtree by calling `post_order(node.right)`.
- **Process Node:**
  - Once both subtrees have been traversed, append the current node's value to the `nodes` list.
- **Return Result:**
  - After the traversal completes, return the list `nodes` containing the postorder traversal of the tree.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of nodes in the tree. Every node is visited once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, for storing the result and the recursion stack. In the worst case, the depth of the recursion stack is proportional to the height of the tree, which can be `O(n)` in the case of a skewed tree.
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def post_order(node):
            if not node:
                return
            post_order(node.left)
            post_order(node.right)
            nodes.append(node.val)

        post_order(root)
        return nodes

```