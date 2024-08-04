# Topics
- Sorting
- Array
- Python3

# Approach
- **Generate All Subarray Sums:**
  - Iterate through the array and calculate the sums of all possible subarrays.
  - Store these sums in a list.
- **Sort the Subarray Sums:**
  - Sort the list of subarray sums.
- **Calculate the Range Sum:**
  - Extract the elements from the sorted list within the specified range and compute their sum.
- **Modulus Operation:**
  - Return the sum modulo `((10^9)+7)` to ensure the result is within the required bounds.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Generating all subarray sums takes `O(n^2)` time, where `n` is the length of the array.
  - Sorting the list of subarray sums takes `O(n^2logn^2)` time.
  - Summing up the elements within the specified range takes `O(n)` time.
  - Overall time complexity: `O(n^2logn)`.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - Storing all subarray sums takes `O(n^2)` space.
  - Overall space complexity: `O(n^2)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        result = []
        length = len(nums)
        for idx in range(length):
            previous_sum = 0
            for jdx in range(idx, length):
                previous_sum += nums[jdx]
                result.append(previous_sum)
        result.sort()
        return sum(result[left-1: right]) % ((10 ** 9) + 7)
```