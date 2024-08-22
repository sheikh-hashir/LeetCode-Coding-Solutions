# Topics
- Bit Manipulation
- Python3

# Intuition
- The complement of a number is formed by flipping all the bits in its binary representation (changing 1s to 0s and 0s to 1s).
- Therefore, to solve this problem, the first step is to convert the number to its binary form, then flip each bit, and finally convert the result back to an integer.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Convert the given number to its binary form (excluding the `'0b'` prefix).
- Flip all the bits using a translation method that replaces `'1'` with `'0'` and `'0'` with `'1'`.
- Convert the resulting binary string back to an integer and return it.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Converting a number to binary takes `O(logn)` time.
  - Flipping bits using `str.translate` is `O(logn)`.
  - Converting the binary string back to an integer also takes `O(logn)`.
  - Therefore, the overall time complexity is `O(logn)` .
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: The space complexity is `O(logn)` since we're storing the binary representation of the number.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        complement = binary.translate(str.maketrans("01", "10"))
        return int(complement, 2)

```