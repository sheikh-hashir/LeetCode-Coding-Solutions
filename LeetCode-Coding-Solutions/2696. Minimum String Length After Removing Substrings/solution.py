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
