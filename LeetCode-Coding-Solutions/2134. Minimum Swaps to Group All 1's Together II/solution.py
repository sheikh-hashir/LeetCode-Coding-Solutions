from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones_count = nums.count(1)
        nums.extend(nums[: ones_count + 1])
        end = len(nums) - ones_count + 1
        current_min = nums[:ones_count].count(0)
        min_swap = current_min
        for i in range(1, end):
            if nums[i - 1] == 0:
                current_min -= 1
            if nums[i + ones_count - 1] == 0:
                current_min += 1
            min_swap = min(min_swap, current_min)
        return min_swap
