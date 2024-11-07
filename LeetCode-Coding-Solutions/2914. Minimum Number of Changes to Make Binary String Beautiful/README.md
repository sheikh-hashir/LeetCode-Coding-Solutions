# Topics
- String
- Python3

# Intuition
- To minimize changes in a string, the problem likely requires us to alternate characters.
- The simplest approach is to check every second character against the previous one and change it if needed to maintain the desired alternation.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Count Alternating Characters:**
  - Traverse the string, examining pairs of characters. For every odd-indexed character that matches the previous character, count it as a necessary change.
- **Return Total Changes:**
    - Sum up the required changes.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)` because we check each pair of characters once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)` as we're only tracking the count of changes.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def minChanges(self, s: str) -> int:
        length = len(s)
        return sum(1 if s[i] != s[i+1] else 0 for i in range(0, length-1, 2))

```