from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remaining_chalk = k % sum(chalk)

        for idx, chalk_needed in enumerate(chalk):
            if remaining_chalk < chalk_needed:
                return idx
            remaining_chalk -= chalk_needed
        return 0
