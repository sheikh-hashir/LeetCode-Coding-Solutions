# Approach
- **Initialization:**
  - Create a min heap to keep track of the k largest elements.
  - Iterate over the initial list of numbers and add each number to the heap using the `add` method to ensure the heap maintains the k largest elements.

- **Adding New Elements:**
  - If the heap contains fewer than `k` elements, simply add the new number.
  - If the heap already contains `k` elements, compare the new number with the smallest number in the heap (the root). If the new number is larger, replace the root with the new number. This keeps the heap size at `k` and ensures the root is the k-th largest element.

- **Returning the k-th Largest Element:**
  - After each insertion, return the root of the heap, which represents the k-th largest element.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - **Initialization:** Building the heap from `n` elements (where `n` is the size of the initial list) takes `O(nlogk)` time.
  - **Add Method:** Each insertion operation is `O(logk)` because we maintain a heap of size k.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(k)` because we are storing only k elements in the heap.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        # Build the initial heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            if val > self.min_heap[0]:
                heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]

```