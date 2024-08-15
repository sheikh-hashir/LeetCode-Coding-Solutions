from collections import Counter
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                combo.append(candidates[i])
                backtrack(remaining - candidates[i], combo, i + 1)
                combo.pop()

        candidates.sort()
        result = []
        backtrack(target, [], 0)
        return result
