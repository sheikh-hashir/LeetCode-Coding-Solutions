# Intuition
- The problem is about performing arithmetic operations on fractions.
- Instead of dealing with floating-point operations, which may lead to precision issues, fractions can be handled using the `Fraction` class, which supports exact arithmetic on rational numbers.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Parse the Input Expression**
  - The input expression is a string that represents a mathematical expression of fractions, including addition and subtraction operations (e.g., `"1/3-1/2+2/6"`). The goal is to parse this expression and perform the arithmetic operations step by step.
    - **Sign Handling:** First, check if the expression starts with a negative sign (`-`). If it does, set a `sign` variable to `-1` and remove the negative sign from the expression. Otherwise, set the `sign` to `1`.
    - **Splitting Components:** Use a regular expression to split the input expression into components. The regex `re.split(r"([+-])", expression)` splits the expression at each `+` or `-` sign, keeping the operators as separate components in the list. This allows us to handle each fraction and its corresponding operation individually.
<!-- Describe your approach to solving the problem. -->

- **Process Each Component**
  - Iterate over the components of the expression. The components consist of fractions (like `"1/3"`) and operators (`"+"`, `"-"`). For each component:
    - **Fraction Handling:** If the component contains a fraction (i.e., it has a `/`), split it into the numerator and denominator using `map(float, component.split("/"))`. Convert the fraction to a floating-point value for easier arithmetic.
    - **Operator Handling:** If the component is an operator (`"+"` or `"-"`), add it to the stack.


- **Calculate the Result**
  - After parsing all components into fractions and operators, start calculating the result:
    - **Handle Initial Sign:** If the expression started with a negative sign, multiply the first fraction by `-1` to account for this.
    - **Iterate through the Stack:** Perform arithmetic operations between consecutive fractions based on the operators in the stack:
      - Pop the first fraction (`val_1`), then pop the operator (`+` or `-`), then pop the second fraction (`val_2`).
      - If the operator is `+`, add the fractions. If the operator is `-`, subtract them.
      - Insert the result back at the beginning of the stack and continue until only one value (the final result) remains in the stack.

- **Convert Result to Fraction**
  - Once the calculation is done, the final value in the stack is the result of the expression. This value is a floating-point number, so it needs to be converted back to a fraction:
    - Use the `Fraction` class from the fractions module to convert the result to a fraction. The `limit_denominator()` method is used to ensure the fraction is in its simplest form.
    - **Formatting:** Convert the fraction to a string. If the fraction simplifies to an integer (e.g., `3/1`), format it as `3` by checking if the string consists of only digits or is a negative number (like `"-3"`).

# Complexity
- Time complexity: `O(n)`, where `n` is the number of characters in the input string. The parsing and arithmetic operations are linear in the size of the expression.


<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, as we store the components of the expression in the stack.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
import re
from fractions import Fraction


class Solution:
    def fractionAddition(self, expression: str) -> str:
        sign = -1 if expression[0] == "-" else 1
        expression = expression[1:] if expression[0] == "-" else expression

        components = re.split(r"([+-])", expression)
        stack = []

        operator = None
        for component in components:
            if "/" in component:
                val_1, val_2 = map(float, component.split("/"))
                stack.append(val_1 / val_2)
            elif component in ["+", "-"]:
                stack.append(component)

        first_num = True
        if len(stack) == 1:
            result = stack.pop()
            result = result * sign
            stack.append(result)
        while len(stack) != 1:
            val_1 = stack.pop(0)
            operator = stack.pop(0)
            val_2 = stack.pop(0)

            if first_num:
                val_1 *= sign
                first_num = False

            ans = val_1 + val_2 if operator == "+" else val_1 - val_2
            stack.insert(0, ans)

        fraction = str(Fraction(stack[0]).limit_denominator())
        return (
            f"{fraction}/1"
            if fraction.isdigit() or (fraction[0] == "-" and fraction[1:].isdigit())
            else fraction
        )

```