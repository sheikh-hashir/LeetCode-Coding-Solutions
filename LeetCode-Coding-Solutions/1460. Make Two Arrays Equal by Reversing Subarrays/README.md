# Topics
- Array
- Sorting
- Python3

# Approach
- **Sort Both Arrays:**
  - Sort both the target and arr arrays.
- **Compare Sorted Arrays:**
  - Check if the sorted versions of target and arr are identical.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(nlogn)`, where `n` is the length of the arrays. This is due to the sorting operation.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, which is the space required to store the sorted arrays.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
```