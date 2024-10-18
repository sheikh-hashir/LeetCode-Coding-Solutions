from functools import lru_cache
from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        length = len(s)
        cache = {}

        @lru_cache(None)
        def dfs(i: int):
            if i == length:
                return 0

            res = 1 + dfs(i + 1)
            for j in range(i, length):
                if s[i : j + 1] in dictionary:
                    res = min(dfs(j + 1), res)

            cache[i] = res
            return res

        return dfs(0)
