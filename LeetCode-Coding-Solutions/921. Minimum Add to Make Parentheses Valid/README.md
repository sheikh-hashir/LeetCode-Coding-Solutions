# Intuition
- When solving the problem of making a string of parentheses valid, the main challenge is to balance the number of opening and closing parentheses.
- We need to ensure that each opening parenthesis has a corresponding closing parenthesis and vice versa.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- The number of unmatched opening parentheses (`opening`).
- The number of unmatched closing parentheses (`result`) we need to add.
- For each opening parenthesis `(`, we increment the opening counter.
- For each closing parenthesis `)`, we check if there is an unmatched opening parenthesis available (`opening > 0`).
- If yes, we decrement the `opening` counter as we've found a valid pair.
- If no unmatched opening parenthesis exists, it means we have an excess closing parenthesis, so we increment `result` as this closing parenthesis needs to be "matched" by an opening parenthesis later.

At the end of the iteration, the total number of insertions required to make the string valid is the sum of unmatched opening and unmatched closing parentheses (`opening + result`).



<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the length of the string. We only traverse the string once, processing each character in constant time.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`, since we only use a constant amount of space for the two counters (`opening` and `result`).
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening, result = 0, 0
        for char in s:
            if char == "(":
                opening += 1
            elif char == ")":
                if opening > 0:
                    opening -= 1
                else:
                    result += 1
        return opening + result
```