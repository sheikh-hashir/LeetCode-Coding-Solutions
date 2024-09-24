# Topics
- Array
- Hash Table
- String
- Python3

# Intuition
- The goal of the problem is to find the longest common prefix between two arrays of integers. For each number, we can keep reducing it by removing the last digit and check if the resulting number exists in the other array.
- The largest such common number will be our answer.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Storing Prefixes:**
  - For each number in the first array, generate all possible prefixes by repeatedly removing the last digit. Store these prefixes in a set.
- **Checking for Common Prefix:**
  - For each number in the second array, generate all possible prefixes in the same way.
  - Check if the prefix exists in the set from the first array.
  - If it does, keep track of the longest such common prefix.
- **Returning the Length:**
  - The result is the length of the longest common prefix. If no common prefix is found, return 0.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - For each number in `arr1` and `arr2`, we calculate all prefixes, which could take up to the number of digits in each number.
  - Let `n` be the size of `arr1` and `m` the size of `arr2`, and assume each number has at most `d` digits.
  - The total time complexity would be `O((n+m)⋅d)`, where `d` is the average number of digits in the numbers
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - We store all prefixes from arr1 in a set, which would require `O(n⋅d)` space 
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
import math
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        _prefix = set()
        result = float("-inf")

        def calculate_all_prefix(num: int, validate_prefix: bool = False):
            nonlocal result
            while num >= 1:
                if validate_prefix:
                    if num in _prefix:
                        result = max(result, num)
                        break
                else:
                    _prefix.add(num)
                num //= 10

        for num in arr1:
            calculate_all_prefix(num)

        for num in arr2:
            calculate_all_prefix(num, True)

        return 0 if math.isinf(result) else len(str(int(result)))
```