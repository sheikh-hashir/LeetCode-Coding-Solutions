# Topics
- Array
- Math
- Simulation
- Python3

# Intuition
- To find the missing rolls, we need to calculate the total sum that the missing rolls should add up to, given the desired mean.
- The goal is to distribute this total sum across the missing rolls while ensuring that each roll value is between 1 and 6 (inclusive).
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- First, calculate the total sum of the missing rolls by subtracting the sum of the given rolls from the total required sum based on the desired mean.
- Check if it’s possible to distribute the total sum among the missing rolls (each roll should be between 1 and 6). If it’s not possible, return an empty list.
- Calculate the base value for each roll and distribute any remainder across the first few rolls to ensure the sum matches the required total.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of missing rolls. We iterate over n to construct the result list.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, since we are creating a list of size `n` to store the missing rolls.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        _sum = sum(rolls)
        result = ((len(rolls) + n) * mean) - _sum

        if result < n or result > 6 * n:
            return []

        start = result // n
        remainder = result % n

        answer = []
        for i in range(n):
            if i < remainder:
                answer.append(start + 1)  # Distribute the remainder
            else:
                answer.append(start)
        return answer
```