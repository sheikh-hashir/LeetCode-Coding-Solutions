# Topics
- Array
- Greedy
- Heap (Priority Queue)
- Python3

# Intuition
- The goal is to maximize the sum of `k` elements, with the caveat that after selecting the maximum element, we replace it with one-third of its value (rounded up).
- Since we need to repeatedly find the maximum element, a max heap is a good data structure to use, as it allows us to efficiently pop the largest element and adjust the heap accordingly.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- First, convert the input list `nums` into a max heap using Python's `heapq` library. Since `heapq` only supports min-heaps by default, we use the `_heapify_max()` function to transform `nums` into a max heap.
- Then, for `k` iterations:
  - Pop the largest element from the heap.
  - Add this element to the result.
  - Push back one-third of this value (rounded up) into the heap.
- Repeat the above process until we've selected `k` elements.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Constructing the max heap initially takes `O(n)` where `n` is the size of nums.
  - For each of the k operations, both popping the maximum element and pushing a new element take `O(logn)` time.
  - Thus, the total time complexity is `O(n+klogn)`.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - We are using a heap data structure that stores the elements of nums, so the space complexity is `O(n)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
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

```