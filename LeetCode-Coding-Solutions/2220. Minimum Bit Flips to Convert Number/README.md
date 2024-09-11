# Topics
- Bit Manipulation
- Python3

# Intuition
- The problem asks for the minimum number of bit flips required to convert `start` to `goal`.
- My first thought was that the positions where `start` and `goal` differ are the ones that need flipping.
- This can be solved using the XOR operation.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Use the XOR (`^`) operation between `start` and `goal`.
- The XOR result will have `1`s at the positions where the bits of `start` and `goal` differ.
- Count the number of `1`s in the XOR result. Each 1 corresponds to a bit that needs flipping.
- Convert the XOR result to a binary string and count the `1`s using Python's `bin()` function and `count()` method.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(logn)` where `n` is the maximum of start or goal.This is because the XOR operation and counting the bits are proportional to the number of bits in the binary representation.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- - Space complexity: `O(1)`, as we're using a constant amount of space.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(start ^ goal).count("1")

```