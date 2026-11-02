# O(n) Time & O(1) Space | In-Place Sign Flips via Index Mapping

# Approach
1. **In-Place Marking:** Iterate through the array from left to right using a `while` loop. For each element, find its absolute value to get the original number, subtract 1 to translate it to a 0-indexed position (`abs(nums[index]) - 1`), and flip the value at that target index to negative.
2. **Handle Re-visitation:** Apply `abs()` to the target value before multiplying by `-1` to ensure that if a number appears multiple times, its index stays negative instead of flipping back to positive.
3. **Filter Positives:** After marking all present numbers and, perform a second pass using a list comprehension. Any index `idx` that still holds a positive number means the value `idx + 1` was never present in the input array.

# Complexity
- Time complexity:
O(n)
*Iterate through the array of length n exactly once to mark the visited indices, and iterate a second time via list comprehension to collect the missing numbers. Both loops run in linear time.*

- Space complexity:
O(1)
*The tracking and marking happen completely in-place by reusing the input array's sign states. Excluding the returned list, no extra data structures are allocated.*

# Code
```python3 []
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        index = 0
        length = len(nums)
        result = []
        while index < length:
            nums[abs(nums[index]) - 1] = abs(nums[abs(nums[index]) - 1]) * -1
            index += 1
        return [idx + 1 for idx, num in enumerate(nums) if num > 0]
```