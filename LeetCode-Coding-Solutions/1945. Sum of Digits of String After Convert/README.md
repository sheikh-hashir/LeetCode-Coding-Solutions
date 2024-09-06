# Topics
- String
- Simulation
- Python3

# Intuition
- The problem asks for transforming a string into a number by replacing each character with its position in the alphabet and then repeatedly summing the digits of the resulting number k times.
- My first thought is to break down the problem into two main steps:
  - (1) convert the string into a number and
  - (2) repeatedly sum the digits `k` times.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Convert the string s into a number by replacing each character with its corresponding position in the alphabet (`a = 1, b = 2, ..., z = 26`).
- Sum the digits of the resulting number and repeat this operation `k` times.
- Use a recursive helper function `calculate_digit_sum` to repeatedly sum the digits for `k` iterations.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Converting the string to a number takes `O(n)` time.

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - The space complexity is `O(n)` due to the storage required for the converted number string.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def calculate_digit_sum(num: int, _range: int):
            if _range == 0:
                return num

            new_num = 0
            while num:
                new_num += num % 10
                num//=10

            return calculate_digit_sum(new_num, _range-1)

        converted_number = int(''.join(str(ord(_char) - ord("a") + 1) for _char in s))
        return calculate_digit_sum(converted_number, k)

```
