# Topics
- Array
- Greedy
- String
- Sorting
- Python3

# Intuition
- To solve this problem, we need to arrange the numbers in such a way that their concatenation forms the largest possible number.
- The challenge is to determine the optimal order for concatenation.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Convert Numbers to Strings:**
  - Convert each integer in the array to a string. This allows us to perform string-based operations and comparisons.

- **Custom Sorting:**
  - Define a custom comparison function that determines the order of two numbers based on their concatenated results. Specifically, given two numbers `x` and `y`, compare `x + y` with `y + x`:
    - If `x + y` is greater than `y + x`, `x` should come before `y` in the final order.
    - Otherwise, `y` should come before `x`.
- **Sort the Strings:**
  - Use the custom comparator to sort the list of string numbers.
- **Concatenate and Handle Edge Cases:**
  - Join the sorted list into a single string. Handle the edge case where the result might start with '0' (which indicates that all numbers were '0') by returning "0".
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: Sorting the strings based on custom comparison takes `O(nlogn)` time, where `n` is the number of elements in the array.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: Space complexity `O(n)` is primarily due to storing the converted string representations of the numbers.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))

        def compare(x, y):
            return (1 if x + y < y + x else -1) if x + y != y + x else 0

        # Sort the numbers using the custom comparator
        str_nums.sort(key=cmp_to_key(compare))
        # Concatenate the numbers
        result = "".join(str_nums)

        # Edge case: if the result starts with '0', it means all numbers are '0'
        return "0" if result[0] == "0" else result

```