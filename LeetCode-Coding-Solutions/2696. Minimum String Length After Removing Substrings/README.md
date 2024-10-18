# Topics
- String
- Stack
- Simulation
- Python3

# Intuition
- The goal is to reduce the string by repeatedly removing specific pairs of characters (`"AB"` and `"CD"`).
- A stack is ideal for this problem because we can push characters onto it, and when we encounter a pair, we can simply pop the top element.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- We use a stack to process the characters in the string.
- For each character in the string:
  - If the top of the stack forms a valid pair (`"AB"` or `"CD"`) with the current character, we pop the stack (i.e., remove the pair).
  - Otherwise, we push the current character onto the stack.
- At the end of the traversal, the stack contains the remaining characters after all possible pairs have been removed. The length of the stack is the answer.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the length of the string. We process each character once, pushing and popping elements from the stack.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` in the worst case, if no pairs are found and all characters are added to the stack.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def minLength(self, s: str) -> int:
        # Initialize a stack
        stack = []
        # Set of valid pairs to remove
        pairs = {"AB", "CD"}

        # Traverse through the string
        for char in s:
            # If the stack is not empty and the last character in the stack
            # forms a valid pair with the current character, pop the stack
            if stack and stack[-1] + char in pairs:
                stack.pop()
            else:
                stack.append(char)

        # The remaining characters in the stack represent the final string
        return len(stack)

```