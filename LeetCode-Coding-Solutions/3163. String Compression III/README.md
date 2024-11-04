# Topics
- String
- Python3

# Intuition
- The goal is to compress a string by counting consecutive occurrences of each character.
- This can be achieved by iterating through the string and keeping track of character counts, adding them to the result whenever the character changes.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Initialize Variables:**
  - Start by setting up an empty list `result` to store compressed segments, `previous_char` to track the last character seen, and `count` to count consecutive occurrences.
- **Iterate through Characters:**
  - Loop through each character in the string. If the character differs from `previous_char`, append the count and character to `result`, reset the count to 1, and update `previous_char`. If the character matches `previous_char`, increment the count.
- **Handle Count Limit:**
  - If the count exceeds 9, append `9` `previous_char` to limit each segment to a single digit, reset the count to 1, and continue counting.
- **Final Append:**
  - After the loop, append the last counted segment to  .
- **Join and Return:**
  - Join all segments in `result` to form the compressed string.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the length of word, as we iterate through each character once.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, due to storing compressed segments in the `result` list.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""

        result = []
        previous_char = word[0]
        count = 1

        for index in range(1, len(word)):
            if word[index] != previous_char:
                result.append(f"{count}{previous_char}")
                previous_char = word[index]
                count = 1
            else:
                count += 1
                if count > 9:
                    result.append(f"{count - 1}{previous_char}")
                    count = 1

        result.append(f"{count}{previous_char}")

        return "".join(result)

```