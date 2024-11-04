# Topics
- String
- String Matching
- Python3

# Intuition
- To determine if one string is a rotation of another, we can concatenate the first string with itself.
- If the second string is indeed a rotation of the first, it should appear as a substring within this concatenated version.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Length Check:**
  - First, check if the lengths of both strings are the same. If they are not, return `False` since one cannot be a rotation of the other.
- **Concatenate and Check:**
  - Concatenate the string `s` with itself. This creates a new string that contains all possible rotations of `s`. Then, check if `goal` is a substring of this concatenated string.
- **Return Result:**
  - Return `True` if `goal` is found in the concatenated string; otherwise, return `False`.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the length of the string s. Checking for a substring in a string of size `2n` takes linear time.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, as we are creating a new string that is twice the length of `s`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return False if len(s) != len(goal) else goal in s+s
```