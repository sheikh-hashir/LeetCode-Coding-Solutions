# Intuition
- The problem can be broken down into smaller sub-problems where each player tries to maximize their stones while minimizing the opponent's gain.
- By storing results of sub-problems in a cache, we avoid redundant calculations, leading to a more efficient solution.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Use a recursive Depth-First Search (DFS) approach where the game alternates between Alice and her opponent.
- The `dfs` function calculates the maximum stones Alice can collect (if `alice` is `True`) or the minimum stones the opponent can collect (if `alice` is `False`) at each step.
- The `cache` dictionary stores results of subproblems to avoid recalculating the same states.
- At each step, the number of stones picked is controlled by the variable `X`, which can range from `1 to 2 * M`. The function recursively calculates the optimal result for the current player.
<!-- Describe your approach to solving the problem. -->

# Code
```python3 []
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        cache = {}
        def dfs(alice: bool, i: int, M: int):
            if i == len(piles):
                return 0
            if (alice, i, M) in cache:
                return cache[(alice, i, M)]

            res = 0 if alice else float("inf")
            total = 0
            for X in range(1, min(2 * M + 1, len(piles) - i + 1)):
                total += piles[i + X -1]
                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))
            cache[(alice, i, M)] = res
            return res
        return dfs(True, 0, 1)

```