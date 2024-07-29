# Topics
- Python3
- String
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Filter Non-Alphanumeric Characters:**
  - Use filter combined with str.isalnum to remove all non-alphanumeric characters from the string.
- **Convert to Lowercase:**
  - Convert the entire string to lowercase to handle case insensitivity.
- **Check Palindrome:**
  - Compare the processed string to its reverse to determine if it is a palindrome.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: O(n)
  - Filtering and converting to lowercase both take linear time relative to the length of the string.
  - Comparing the string to its reverse also takes linear time.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: O(n)
  - The space used to store the filtered and lowercased version of the string is proportional to its length.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        return s == s[::-1]

```