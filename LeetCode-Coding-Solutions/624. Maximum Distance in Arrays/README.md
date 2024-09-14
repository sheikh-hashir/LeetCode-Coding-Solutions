# Topics
- Array
- Python3
- Greedy

# Intuition
- The goal is to find the maximum distance between elements from different arrays. My first thought was to track the minimum and maximum values encountered so far and calculate the potential maximum distance using these values.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Start by initializing `global_min` and `global_max` with the first array's minimum and maximum values, respectively.
- **Iterate through each subsequent array:**
  - Calculate the distance between the current array's maximum and `global_min`.
  - Calculate the distance between `global_max` and the current array's minimum.
  - Update the `result` with the maximum of these distances.
  - Update `global_min` and `global_max` as you proceed through the arrays.
- Return the maximum distance found.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of arrays. Each array is processed once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`, as only a few extra variables are used regardless of input size.

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        result = 0
        for array in arrays[1:]:
            result = max(result, abs(array[-1] - global_min), abs(global_max - array[0]))
            global_min = min(global_min, array[0])
            global_max = max(global_max, array[-1])
        return result
```