# Topics
- Hash Table
- String
- Counting
- Python3

# Intuition
- The problem asks for words that appear exactly once across two sentences.
- We can achieve this by combining the words from both sentences and then counting the occurrences of each word.
- Words that have a count of exactly one are uncommon and should be included in the result.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Word Count:**
  - Use a dictionary to store the frequency of each word from both sentences. The `defaultdict` from the `collections` module simplifies this by initializing default values automatically.
- **Split Sentences:**
  - First, split both sentences into individual words using the `split()` function.
- **Count Occurrences:**
  - Loop through the words from both sentences and increment their count in the dictionary.
- **Filter Uncommon Words:**
  - Finally, iterate over the dictionary and collect words that have a count of exactly 1, indicating they are uncommon between the two sentences.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)` where `n` is the total number of words in both sentences combined. This is because we are processing each word in the sentences once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` where `n` is the number of unique words in both sentences, as we store each word in the dictionary.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from collections import defaultdict

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        common_dict = defaultdict(int)
        for word in chain(s1.split(), s2.split()):
            common_dict[word] += 1

        return [key for key, value in common_dict.items() if value == 1]
```