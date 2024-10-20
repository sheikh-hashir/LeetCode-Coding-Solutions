# Topics
- String
- Simulation
- Python3

# Intuition
- The problem is about constructing a string based on recursive patterns and identifying a particular bit at a given position.
- My first thought is to generate the string iteratively by repeatedly following the given rules and then retrieving the desired bit from the final string.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Start with the base string `"0"`.
- For each iteration, invert the current string, reverse it, and concatenate it with the original string and a `'1'` in the middle.
- Continue this process for `n` iterations to build the string.
- Once the string is built, return the `k-th` character, keeping in mind that the index in Python is 0-based.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - The string roughly doubles in size with each iteration. So, after n iterations, the length of the string becomes approximately `2^n−1`.
  - Constructing the string at each iteration involves inverting and reversing the string, which takes `O(2^n)` operations in total. Therefore, the time complexity is `O(2^n)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - The space complexity is also `O(2^n)`, since we are storing the final string of length `2^n−1`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        result = "0"

        # Build the sequence up to nth iteration
        for _ in range(1, n + 1):
            inverted = "".join("1" if char == "0" else "0" for char in result)
            result = f"{result}1{inverted[::-1]}"

        # Return the k-th character (1-based index, so subtract 1)
        return result[k - 1]

```