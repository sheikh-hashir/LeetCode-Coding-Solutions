import heapq
import math
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        def heappush_max(heap, item):
            heap.append(item)
            heapq._siftdown_max(heap, 0, len(heap) - 1)

        # Initialize the max heap
        heapq._heapify_max(nums)
        result = 0

        for _ in range(k):
            # Pop the maximum element
            res = heapq._heappop_max(nums)
            result += res
            # Push the new element after applying the math operation
            heappush_max(nums, math.ceil(res / 3))

        return result
