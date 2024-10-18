# Topics
- Array
- Bit Manipulation
- Enumeration
- Python3

# Intuition
- The task requires counting the subsets of an array whose bitwise OR results in the maximum possible bitwise OR for the entire array.
- First, we compute the maximum OR achievable using all elements of the array, then count the number of subsets that match this OR.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Compute the Maximum Bitwise OR:**
  - Use Python’s `reduce()` function to get the maximum bitwise OR for the entire array.

- **Generate All Subsets:**
  - Use a recursive function to generate all subsets of the array. For each subset, calculate the bitwise OR and check if it matches the maximum bitwise OR.

- **Count Matching Subsets:**
  - If the OR of a subset matches the precomputed maximum OR, increment the count.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - `O(n⋅2^n)` where `n` is the number of elements in the array.
  - The number of subsets for an array of length `n` is `2^n`. For each subset, computing the OR takes `O(n)`, so the overall time complexity is `O(n⋅2^n)`.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - `O(n)`. The recursion depth is `n`, and the space required for generating subsets is proportional to the length of the array.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
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

```