# Topics
- Sliding Window
- Array
- Python3

# Approach
- **Count Ones:**
  - First, count the number of 1s in the array.
- **Extend Array:**
  - Extend the array to handle the circular nature by appending a portion of the array to itself.
- **Sliding Window:**
  - Use a sliding window of size equal to the count of 1s to track the number of 0s within the window.
- **Track Minimum Swaps:**
  - As the window slides through the array, update the count of 0s and keep track of the minimum count of 0s encountered, which represents the minimum number of swaps required.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the length of the array. This is due to the single pass to count the 1s and the subsequent sliding window pass.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, due to the extended array which doubles the space requirement.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones_count = nums.count(1)
        nums.extend(nums[:ones_count+1])
        end = len(nums) - ones_count + 1
        current_min = nums[:ones_count].count(0)
        min_swap = current_min
        for i in range(1, end):
            if nums[i-1] == 0:
                current_min-=1
            if nums[i+ones_count-1] == 0:
                current_min+=1
            min_swap = min(min_swap, current_min)
        return min_swap

```