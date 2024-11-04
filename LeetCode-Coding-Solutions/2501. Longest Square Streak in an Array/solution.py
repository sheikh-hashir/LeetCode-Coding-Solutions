from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        nums = set(nums)

        for n in nums:
            current = n
            streak_length = 0
            while current in nums:
                current = current ** 2
                streak_length += 1
            count = max(count, streak_length)
        return count if count != 1 else -1
