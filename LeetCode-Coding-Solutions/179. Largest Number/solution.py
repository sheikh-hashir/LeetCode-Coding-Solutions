from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))

        def compare(x, y):
            return (1 if x + y < y + x else -1) if x + y != y + x else 0

        # Sort the numbers using the custom comparator
        str_nums.sort(key=cmp_to_key(compare))
        # Concatenate the numbers
        result = "".join(str_nums)

        # Edge case: if the result starts with '0', it means all numbers are '0'
        return "0" if result[0] == "0" else result
