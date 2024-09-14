# Topics
- Array
- Backtracking
- Python3

# Approach
- **Sort the Candidates:**
  - Begin by sorting the `candidates` list. Sorting facilitates the identification and skipping of duplicate elements, ensuring that each combination is unique.

- **Define the Backtracking Function:**
  - **Function Signature:** Define a recursive helper function named `backtrack` that takes three parameters:
    - **remaining:** The remaining value needed to reach the target sum.
    - **combo:** The current combination of numbers being considered.
    - **start:** The index in the `candidates` list from which to consider elements for the current recursive call.

- **Base Cases:**
  - **Successful Combination:**
    - If `remaining` is exactly `0`, it means the current `combo` sums up to the target. In this case, append a copy of `combo` to the result list.
  - **Exceeded Target:**
    - If `remaining` is less than `0`, the current `combo` exceeds the target sum, and no further exploration is needed along this path.

- **Recursive Exploration:**
  - Iterate over the `candidates` list starting from the start index.
  - **Skip Duplicates:**
    - To avoid considering the same element multiple times at the same recursive level (which would lead to duplicate combinations), check if the current candidate is the same as the one before it. If so, skip it.
    - **Condition:** `if i > start and candidates[i] == candidates[i - 1]: continue`
  - **Include Current Candidate:**
    - Append the current candidate (`candidates[i]`) to the `combo` list.
  - **Recurse:**
    - Make a recursive call to `backtrack` with:
      - Updated `remaining` value decreased by `candidates[i]`.
      - The updated `combo` list.
      - The next index (`i + 1`) as the new `start` to prevent reusing the same element.
    - **Backtrack:**
      - After returning from the recursive call, remove the last added candidate from `combo` to explore other potential combinations.

- **Initialize and Execute Backtracking:**
  - **Result Storage:**
    - Initialize an empty list `result` to store all valid combinations found.
    - **Start Backtracking:**
      - Invoke the `backtrack` function with:
        - The initial `target` as the remaining value.
        - An empty list `[]` as the starting combo.
        - `0` as the starting index.
    - **Return Results:**
      - After exploring all possible combinations, return the `result` list containing all unique combinations that sum up to the target.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(2^n)` in the worst case, where `n` is the number of candidates. This is because each candidate can either be included or excluded from the combination.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(k)` where `k` is the number of elements in a valid combination. This space is used by the call stack during the backtracking process and by the list that stores the current combination.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
from collections import Counter
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, combo, start):
            if remaining == 0:
                result.append(list(combo))
                return
            elif remaining < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                combo.append(candidates[i])
                backtrack(remaining - candidates[i], combo, i + 1)
                combo.pop()

        candidates.sort()
        result = []
        backtrack(target, [], 0)
        return result


```