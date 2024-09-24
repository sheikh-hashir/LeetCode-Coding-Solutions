import math
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        _prefix = set()
        result = float("-inf")

        def calculate_all_prefix(num: int, validate_prefix: bool = False):
            nonlocal result
            while num >= 1:
                if validate_prefix:
                    if num in _prefix:
                        result = max(result, num)
                        break
                else:
                    _prefix.add(num)
                num //= 10

        for num in arr1:
            calculate_all_prefix(num)

        for num in arr2:
            calculate_all_prefix(num, True)

        return 0 if math.isinf(result) else len(str(int(result)))
