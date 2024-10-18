# Topics
- Array
- String
- Counting
- Hash Table
- Python3

# Intuition
- The idea is to calculate the score of each word by summing the counts of all its prefixes across the entire list of words
- By storing prefix counts in a dictionary, we can efficiently compute the sum of prefix scores for each word.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Prefix Count:**
  - We first iterate through the list of words and for each word, we generate all its prefixes and store how many times each prefix has been encountered using a dictionary (`prefix_sum`).
- **Prefix Score Calculation:**
  - For each word, we sum the prefix counts by iterating through all its prefixes.
  - This sum gives the total score of that word.
- **Efficient Calculation:**
  - Using a dictionary to store prefix counts allows us to quickly look up and sum the counts for any word’s prefixes.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - For each word, we generate all its prefixes, and for each prefix, we update the count in the dictionary. If there are `n` words, and the average word length is `k`, the overall time complexity is:
  - `O(n⋅k^2)` (due to nested loops for generating and summing prefixes)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - We store counts for each possible prefix, so in the worst case, the space complexity is proportional to the number of prefixes:
  - `O(n⋅k)`.

<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from collections import defaultdict
from typing import List

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_sum = defaultdict(int)
        for word in words:
            for i in range(1, len(word) + 1):
                prefix_sum[word[:i]] += 1

        return [
            sum(prefix_sum[word[:i]] for i in range(1, len(word) + 1)) for word in words
        ]
```