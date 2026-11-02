from collections import defaultdict

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        new_nums = sorted(nums)

        smaller_count_map = {}
        for idx, num in enumerate(new_nums):
            if num not in smaller_count_map:
                smaller_count_map[num] = idx

        return [smaller_count_map[num] for num in nums]
