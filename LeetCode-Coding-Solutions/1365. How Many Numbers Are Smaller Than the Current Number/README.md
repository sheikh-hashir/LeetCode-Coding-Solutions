#  O(n log n) | Sorting & Mapping First-Occurrence Indices

# Intuition
If an array is sorted in ascending order, the index of any element naturally tells us how many elements come before it. For example, if the number `5` first appears at index `3` in a sorted array, it means there are exactly 3 numbers smaller than `5`. By leveraging this sorting property and, find the count of smaller numbers for each element without using a brute-force nested loop.

# Approach
1. **Sort a Copy:** Create a sorted copy of the input array called `new_nums`.
2. **Map the First Occurrence:** Iterate through `new_nums` using `enumerate()`. Store the index of each number in a hash map (`smaller_count_map`). If a number appears multiple times, only record its *first* occurrence to ensure duplicates don't skew the count.
3. **Construct the Result:** Map each number from the original unsorted `nums` array to its corresponding value in `smaller_count_map` using a list comprehension, preserving the original array order.

# Complexity
- Time complexity:
O(n log n)
*Sorting the array takes O(n log n) time. Building the hash map and constructing the final result list both take linear O(n) time, making sorting the dominant operation.*

- Space complexity:
O(n)
*Allocate extra memory for the sorted array copy `new_nums`, the hash map `smaller_count_map`, and the final output list, all of which scale linearly with the size of the input array.*

# Code
```python3 []
from collections import defaultdict

class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        new_nums = sorted(nums)

        smaller_count_map = {}
        for idx, num in enumerate(new_nums):
            if num not in smaller_count_map:
                smaller_count_map[num] = idx

        return [smaller_count_map[num] for num in nums]
```