# Simple Iterative Simulation with Index Tracking

# Approach
Initialize an empty list called `result` and a pointer `index` starting at 0. Since the array is split perfectly into two halves of size n, and run a `while` loop that iterates exactly n times (up to `length // 2`). In each iteration:
1. Append the current element from the first half: `nums[index]`.
2. Append the corresponding element from the second half using the offset n: `nums[index + n]`.
3. Increment `index` by 1 to move to the next pair.

Finally, return the fully interleaved `result` array.

# Complexity
- Time complexity:
O(n)
*Iterate through the first half of the array exactly once. Each loop iteration performs constant-time O(1) operations to index and append, making the overall time complexity linear relative to the number of elements.*

- Space complexity:
O(n)
*Construct a new list `result` to store the shuffled elements, which scales linearly with the size of the input array (requiring O(2n) space, which simplifies to O(n)).*

# Code
```python3 []
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        index = 0
        length = len(nums)
        while index < length // 2:
            result.append(nums[index])
            result.append(nums[index + n])

            index = index + 1

        return result
```
