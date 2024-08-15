# Topics

- Python3
- Array
- Sorting

# Approach

- **Transform the numbers:** For each number in the input list, convert each digit according to the given mapping and form the new number.
- **Pair the transformed number with its index:** Create a list of tuples where each tuple contains the transformed number and its original index.
- **Sort the list of tuples:** Sort the list based on the transformed number and use the original index to break ties.
- **Retrieve the original numbers:** After sorting, use the original indices to extract the original numbers in the desired order.

<!-- Describe your approach to solving the problem. -->

# Complexity

- Time complexity: `O(nlogn)`, where `n` is the number of elements in nums. This is because the most time-consuming operation is the sorting step, which takes `O(nlogn)`. Transforming the numbers takes `O(n⋅k)`, where `k` is the average number of digits in the numbers, but this is dominated by the sorting step.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` due to the additional space needed for the list of tuples storing the transformed numbers and their original indices.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code

```
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping_digits = [(int(''.join(str(mapping[int(digit)]) for digit in str(num))), idx) for idx, num in enumerate(nums)]
        sorted_data = sorted(mapping_digits, key=lambda x: (x[0], x[1]))
        return [nums[idx] for _, idx in sorted_data]
```
