# Intuition
- We are asked to find the length of the longest subarray where all elements are equal to the maximum element in the array.
- We can approach this by identifying the maximum value and then finding consecutive occurrences of that value.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach

- **Find the Maximum Value:**
  - The first step is to determine the maximum value in the array.
  - This is because we only care about consecutive subarrays where all the elements are equal to this maximum value.
  - This can be achieved using Python’s built-in `max()` function**
  - ```python3
    _max = max(nums)
  - This step takes `O(n)` time, where `𝑛` is the number of elements in the list.

- **Group Consecutive Elements:**
  - After finding the maximum value, we need to identify sequences of consecutive elements in the array that are equal to this maximum value.
  - This is where `itertools.groupby()` is helpful. It groups consecutive elements that have the same value. For example:
  - ```python3
     groupby([1, 2, 2, 1, 3, 3, 3, 1])
  - produces groups like:
    - (1, [1])
    - (2, [2, 2])
    - (1, [1])
    - (3, [3, 3, 3])
    - (1, [1])

- **Filter Groups that Match the Maximum Value:**
  - We only care about the groups where the key (the value being grouped) is equal to `_max`.
  - Using a generator expression, we filter the groups where the key is `_max`, and for each matching group, we calculate the length of the group:
  - ```python3
    (len(list(group)) for key, group in groupby(nums) if key == _max)
  - This expression iterates over the groups, and whenever the key is equal to `_max`, it computes the length of that group.

- **Find the Maximum Length of the Groups:**
  - To find the longest subarray of maximum elements, we use Python’s `max()` function on the lengths of the filtered groups.
  - We use `default=0` to handle cases where the list might not contain the maximum value (though in practice, since we derive the maximum value from the list, this edge case shouldn't happen).

# **Example Walkthrough:**

- **Consider the input:**
  - nums = [1, 3, 3, 2, 3, 3, 3, 1]

- **Find the maximum value:**
  - _max = 3

- **Group the consecutive elements:**
  - The groups would be: `(1, [1]), (3, [3, 3]), (2, [2]), (3, [3, 3, 3]), (1, [1])`

- **Filter the groups that match _max:**
  - We get two groups: `[3, 3]` and `[3, 3, 3]`

- **Compute the lengths:**
  - Length of `[3, 3]` = `2`
  - Length of `[3, 3, 3]` = `3`

- The maximum length is `3`, which is returned as the result.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Finding the maximum takes `O(n)`, where `𝑛` is the number of elements.
  - Iterating over the groups and filtering them also takes `O(n)`.
  - Overall time complexity is `O(n)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)` (not counting the input), as we are only storing a few variables and not creating large auxiliary data structures.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        _max = max(nums)
        return max((len(list(group)) for key, group in groupby(nums) if key == _max), default=0)

```