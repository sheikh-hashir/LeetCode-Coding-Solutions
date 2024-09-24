# Topics
- String
- String Matching
- Python3

# Intuition
- The problem is about finding the shortest palindrome that can be formed by adding characters in front of the given string.
- The first thought is to look for the longest prefix of the string that is already a palindrome. Once this prefix is found, the rest of the string (which is not a palindrome) can be reversed and added to the front to form the shortest palindrome.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- Start by iterating over the string and find the longest prefix that is a palindrome.
- This is done by checking substrings of the form `s[:i]` and comparing it with its reverse (`s[:i][::-1]`).
- Once the longest palindromic prefix is found, the remaining part of the string (which is not part of the palindrome) is reversed and added to the front of the original string.
- This ensures that the new string is the shortest possible palindrome.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n^2)`, where `n` is the length of the string. In the worst case, the loop checks each prefix of the string, and for each check, it reverses part of the string, leading to quadratic time complexity.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` because reversing part of the string and constructing the new string requires extra space proportional to the length of the input string.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = len(s)
        while i >= 0 and s[:i] != s[:i][::-1]:
            i-=1

        return f"{s[i:][::-1]}{s}"
```