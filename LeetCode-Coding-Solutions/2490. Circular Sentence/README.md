# Topics
- String
- Python3

# Intuition
- The problem requires checking if a sentence forms a "circular" pattern, meaning the last character of each word should match the first character of the next word, and the last character of the final word should match the first character of the first word.
- This suggests a circular linkage among words, which can be easily verified by comparing adjacent word boundaries.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Split the Sentence:**
  - First, split the input sentence into a list of words.
- **Circular Check:**
  - Append the first word to the end of the list to facilitate circular comparison.
- **Character Matching:**
  - For each word (starting from the second word), check if its first character matches the last character of the previous word.
- **Return Result:**
  - If all checks pass, return `True`; otherwise, return `False`.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of words in the sentence. This is because we iterate over each word once to perform the comparisons.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, due to the space required to store the list of words created from splitting the sentence.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        words.append(words[0])
        length = len(words)
        return all(words[i][0] == words[i - 1][-1] for i in range(1, length))

```