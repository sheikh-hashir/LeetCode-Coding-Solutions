# Topics
- Stack
- String
- Python3

# Intuition
- The problem involves parsing and evaluating a boolean expression using basic logical operators: AND (`&`), OR (`|`), and NOT (`!`).
- My first thought is to use a stack-based approach to process the expression because each logical operation depends on sub-expressions nested within parentheses.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Stack-based processing:**
  - We can iterate through the string character by character, pushing operators and operands onto a stack.
- **Handling closing parenthesis:**
  - When encountering a closing parenthesis `)`, it indicates the end of a sub-expression.
  - We then pop elements from the stack until we reach the corresponding opening parenthesis `(`.
- **Applying the operator:**
  - Once we have all the boolean values (represented by `t` for `True` and `f` for `False`), we apply the relevant operator (`&`, `|`, or `!`) to these values.
- **Pushing the result:**
  - After evaluating the operation, we push the result back onto the stack and continue processing the expression until the entire input string is evaluated.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the length of the expression. Each character is processed once, and stack operations (push and pop) take constant time.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, because we use a stack to store the operators and boolean values.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operations = []
        for exp in expression:
            if exp != ")":
                operations.append(exp)
            else:
                bools = []

                # Pop the values between "(" and ")"
                while operations[-1] != "(":
                    val = operations.pop()
                    if val == "t":
                        bools.append(True)
                    elif val == "f":
                        bools.append(False)

                operations.pop()  # Remove the "("
                operator = operations.pop()  # Get the operator (&, |, !)

                # Apply the operation based on the operator
                if operator == "&":
                    result = all(bools)
                elif operator == "|":
                    result = any(bools)
                elif operator == "!":
                    result = not bools[0]  # NOT only applies to one value

                # Push the result back to the operations stack
                operations.append("t" if result else "f")

        # The final result is in the operations stack
        return operations[-1] == "t"

```