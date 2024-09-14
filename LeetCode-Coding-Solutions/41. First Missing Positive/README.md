# Topics
- Array
- Python3

# Intuition
- To find the first missing positive integer efficiently, leverage the property that the integers we need to track (from 1 to n, where n is the length of the array) can be placed in their respective indices in the array.
- This approach avoids the need for extra space by modifying the array in place.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Rearrange the Array In-Place:**
  - Iterate over the array and place each integer `nums[i]` in its correct index if it falls within the range `[1, length]`.
  - Specifically, for each valid number `nums[i]`, swap it with the number at its target position `nums[nums[i] - 1]`.


- **Find the Missing Positive Integer:**
  - After rearranging, iterate through the array to check which index does not match its expected value (i.e., `nums[i] != i + 1`). The first such mismatch indicates the smallest missing positive integer.
  - If all indices contain the correct values, the smallest missing positive integer is `length + 1`.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)` The array is traversed a constant number of times, resulting in linear time complexity.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)` The algorithm operates in constant space since it rearranges the elements in place without requiring additional space for another array.

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return next((i + 1 for i in range(length) if nums[i] != i + 1), length + 1)

```
