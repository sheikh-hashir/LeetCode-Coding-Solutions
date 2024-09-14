from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        result = 0
        for array in arrays[1:]:
            result = max(
                result, abs(array[-1] - global_min), abs(global_max - array[0])
            )
            global_min = min(global_min, array[0])
            global_max = max(global_max, array[-1])
        return result
