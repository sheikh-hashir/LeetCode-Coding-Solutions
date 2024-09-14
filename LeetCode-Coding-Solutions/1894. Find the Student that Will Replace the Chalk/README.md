# Intuition
- The problem can be approached by realizing that after every cycle of chalk distribution, the total chalk used will reset.
- Therefore, we can first calculate the total chalk needed per cycle and use the modulo operation to determine the remaining chalk after several complete cycles.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Calculate Total Chalk:**
  - First, compute the total chalk required for one full cycle of distribution by summing the chalk array.
- **Modulo Operation:**
  - Use `k % total_chalk` to find the remaining chalk after complete cycles.
- **Find the Student:**
  - Iterate over the chalk array and deduct the chalk needed for each student from the remaining chalk.
  - The first student whose required chalk is more than the remaining chalk will be the answer.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Calculating the sum of chalk takes `O(n)`.
  - Iterating through the array to find the student takes `O(n)`.
  - Overall, the time complexity is `O(n)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - The algorithm uses constant space, so the space complexity is `O(1)`.

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remaining_chalk = k % sum(chalk)

        for idx, chalk_needed in enumerate(chalk):
            if remaining_chalk < chalk_needed:
                return idx
            remaining_chalk -= chalk_needed
        return 0

```
