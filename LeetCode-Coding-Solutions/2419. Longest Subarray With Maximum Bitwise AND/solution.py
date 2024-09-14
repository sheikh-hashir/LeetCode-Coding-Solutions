from itertools import groupby
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        _max = max(nums)
        return max(
            (len(list(group)) for key, group in groupby(nums) if key == _max), default=0
        )
