from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping_digits = [
            (int("".join(str(mapping[int(digit)]) for digit in str(num))), idx)
            for idx, num in enumerate(nums)
        ]
        sorted_data = sorted(mapping_digits, key=lambda x: (x[0], x[1]))
        return [nums[idx] for _, idx in sorted_data]
