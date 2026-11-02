# Topics
- Array
- Maths
- Sorting
- Python3

# Intuition
The problem asks for the minimum number of moves to make all array elements equal, where each move increments \(n - 1\) elements by \(1\). Incrementing \(n - 1\) elements by \(1\) is mathematically equivalent to **decrementing a single element by \(1\)** relative to the rest of the array. From this perspective, instead of trying to push all smaller elements up to match the maximum, try to reduce all larger elements down to match the absolute minimum element in the array.

# Approach
1. **Find the Target Minimum:** The absolute minimum element (`_min`) in the array can never be decremented relative to the others (or rather, it defines the baseline that all other elements must reach). Thus, it serves as our anchor target.
2. **Calculate Differences:** For every element `num` in the array, the number of operations required to bring it down to match the baseline is exactly `num - _min`.
3. **Sum the Operations:** Summing up these individual differences across all numbers gives the total number of operations required to equalize the array without having to simulate any step-by-step increments.

# Complexity
- Time complexity:
O(n)
*Iterate through the array once to find the minimum value using `min(nums)` and iterate through it a second time to calculate the sum of the differences. Both steps scale linearly with the size of the input.*

- Space complexity:
O(1)
*The algorithm uses only a few integer variables (`_min` and the generator expression sum) to track values, running in constant auxiliary space.*

# Code
```python3 []
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        _min = min(nums)
        return sum(num - _min for num in nums)
```