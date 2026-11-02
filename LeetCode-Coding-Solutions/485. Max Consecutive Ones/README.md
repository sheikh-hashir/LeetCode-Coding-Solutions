
# Approach
Solve this in a single line using the following steps wrapped inside Python's built-in `max()` function:
1. `map(str, nums)` converts each integer in the array into its string representation (`0` or `1`).
2. `"".join(...)` merges these characters into a single cohesive binary string.
3. `.split("0")` breaks the string apart wherever a `0` occurs, creating a list of substrings containing only `1`s (or empty strings where `0`s were adjacent).
4. `len(s) for s in ...` is a generator expression that calculates the length of each remaining substring of `1`s.
5. `max(...)` evaluates these lengths and returns the highest count found.

# Complexity
- Time complexity:
`O(n)`
*Converting the array to string elements, joining them, splitting the string, and scanning the lengths all take linear time relative to the number of elements n.*

- Space complexity:
`O(n)`
*Creating the string representation and the resulting list of split substrings both require temporary allocations that scale linearly with the input size n.*

# Code
```python3 []
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        return max(len(s) for s in "".join(map(str, nums)).split("0"))
```
