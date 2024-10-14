from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_array = sorted(set(arr))
        rank_dict = {val: idx + 1 for idx, val in enumerate(sorted_array)}
        return [rank_dict[num] for num in arr]
