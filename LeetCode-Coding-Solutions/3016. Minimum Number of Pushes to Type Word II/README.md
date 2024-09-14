# Topics
- Hash Table
- String
- Greedy
- Sorting
- Counting
- Python3

# Approach
- Count the frequency of each character in the word.
- Sort the characters by their frequency in descending order.
- Distribute the characters to keys, starting with the most frequent characters assigned to the keys that require the fewest pushes.
- Calculate the total number of pushes by multiplying the frequency of each character by its corresponding multiplier (push count).
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(nlogn)` where `n` is the number of unique characters in the word (for sorting the frequencies).
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` for storing the frequency counts of the characters.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = sorted(Counter(word).items(), key=lambda x: x[1], reverse=True)
        multiplier = 1
        result = 0
        for index, (_, value) in enumerate(frequency):
            if index % 8 == 0 and index != 0:
                multiplier += 1
            result += value * multiplier
        return result

```