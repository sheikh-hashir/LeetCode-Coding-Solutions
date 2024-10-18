from functools import reduce
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Compute the maximum bitwise OR for the whole array
        max_bitwise = reduce(lambda x, y: x | y, nums)
        count = 0

        # Helper function to generate subsets and count the ones that match the max OR value
        def generate_subsets(arr, start, current):
            nonlocal count
            if current and reduce(lambda x, y: x | y, current) == max_bitwise:
                count += 1

            # Recursively generate subsets
            for i in range(start, len(arr)):
                generate_subsets(arr, i + 1, current + [arr[i]])

        # Start generating subsets
        generate_subsets(nums, 0, [])
        return count
