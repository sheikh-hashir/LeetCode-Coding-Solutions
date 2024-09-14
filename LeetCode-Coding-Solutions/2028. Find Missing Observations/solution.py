from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        _sum = sum(rolls)
        result = ((len(rolls) + n) * mean) - _sum

        if result < n or result > 6 * n:
            return []

        start = result // n
        remainder = result % n

        answer = []
        for i in range(n):
            if i < remainder:
                answer.append(start + 1)  # Distribute the remainder
            else:
                answer.append(start)
        return answer
