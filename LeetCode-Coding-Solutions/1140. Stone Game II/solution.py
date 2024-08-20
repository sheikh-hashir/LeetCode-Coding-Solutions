from typing import List


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
                total += piles[i + X - 1]
                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))
            cache[(alice, i, M)] = res
            return res

        return dfs(True, 0, 1)
