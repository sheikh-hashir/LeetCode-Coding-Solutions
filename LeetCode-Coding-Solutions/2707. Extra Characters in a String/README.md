# Topics
- Hash Table
- String
- Array
- Dynamic Programming
- Python3

# Intuition
- The problem asks us to find the minimum number of extra characters in a string that are not part of any valid word from the given dictionary.
- The key idea is to explore every substring starting at every index and check if it exists in the dictionary.
- We can recursively explore this problem, making decisions at each step: either count the current character as an extra one or check if a valid word can be formed from the dictionary starting at the current position.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Dynamic Programming with Recursion:**
  - We can approach the problem using dynamic programming by breaking it down into subproblems.
  - Starting from each index `i`, we either skip the current character (counting it as extra) or try to form a valid word by checking substrings starting at `i`.

- **Memoization:**
  - Since the problem can have overlapping subproblems (checking the same index multiple times), we use memoization to store the results of subproblems and avoid recalculating them.

- **Recursive DFS with Memoization:**
  - We use a recursive function dfs(i) that returns the minimum number of extra characters required for the substring starting at index `i`.
  - For each index `i`, we have two options:
    - Count the current character as extra and move to the next index `(i + 1)`.
    - Try to form a valid word by checking substrings `s[i:j+1]`.
    - If the substring exists in the dictionary, we calculate the number of extra characters for the rest of the string (from `j + 1` onward).

- **Caching Results:**
  - We use Python's `lru_cache` to store the results of already computed subproblems, making the solution efficient.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n^2)`, where `n` is the length of the string `s`. For each index `i`, we check substrings up to the length of the string, resulting in a quadratic number of operations. The memoization ensures we don't recompute results.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` for the recursive call stack and the cache that stores the result for each index.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from typing import List
from functools import lru_cache

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        length = len(s)
        cache = {}

        @lru_cache(None)
        def dfs(i: int):
            if i == length:
                return 0


            res = 1 + dfs(i + 1)
            for j in range(i, length):
                if s[i: j+1] in dictionary:
                    res = min(dfs(j+1), res)

            cache[i] = res
            return res

        return dfs(0)

```