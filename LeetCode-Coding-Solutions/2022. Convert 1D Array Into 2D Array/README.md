# Topics
- Array
- Matrix
- Simulation
- Python3

# Intuition
- The goal is to reshape a 1D array into a 2D array with dimensions `m x n`.
- My first thought is that this can be achieved by slicing the original list into sublists of size `n` and placing them in a list of lists (matrix).
- However, if the total number of elements in the `original` list does not match `m * n`, reshaping is impossible.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Check Validity:**
  - First, check if the length of the original list matches `m * n`.
  - If not, return an empty list since the reshaping is not possible.
- **Reshape the Array:**
  - Use list slicing to create sublists of size `n` from the original list.
  - This is done using a list comprehension that iterates over the range of `m` and slices the `original` list accordingly.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)` where `n` is the number of elements in the original list. This is because we iterate through the list once to create the sublists.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` since we create a new 2D list with the same number of elements as the original list.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        return [original[i * n:(i + 1) * n] for i in range(m)]

```