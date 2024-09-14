from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            change[bill] += 1
            return_ = bill - 5

            for val in (20, 10, 5):
                while return_ >= val and change[val] > 0:
                    return_ -= val
                    change[val] -= 1

            if return_ != 0:
                return False
        return True
