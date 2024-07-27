# Topics

- Python3
- Array
- Hash Table
- Sorting

# Approach

- Use the `Counter` from the `collections` module to count the frequency of each number in the list.
- Sort the list using the `sorted` function with a custom key. The key should first sort by frequency in ascending order and then by value in descending order in case of a tie.
<!-- Describe your approach to solving the problem. -->

# Complexity

- Time complexity: `O(nlogn)` because sorting the list takes `O(nlogn)` time, where `n` is the number of elements in the list.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` due to the storage required for the frequency counter and the sorted list.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code

```
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        return sorted(nums, key=lambda x: (frequency[x], -x))

```
