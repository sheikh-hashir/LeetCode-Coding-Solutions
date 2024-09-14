# Topics
- Counting
- Array
- Python3

# Intuition
- The problem is about checking if all characters in a word exist within a set of allowed characters.
- My first thought was to iterate over each word and check every character to see if it is in the allowed string.
- If all characters of the word are found in the allowed string, that word is considered "consistent."
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- For each word in the list of words, check if all characters in the word are present in the `allowed` string.
- Use Python's `all()` function to verify if all characters in a word meet this condition.
- `Sum` the number of words that satisfy the condition, i.e., where all characters are consistent with the allowed string.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n×m)`, where `n` is the number of words and `m` is the average length of each word. This is because we are iterating over each word and checking all of its characters.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`, since we are not using any extra space proportional to the input size beyond a few variables.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(_char in allowed for _char in word) for word in words)

```