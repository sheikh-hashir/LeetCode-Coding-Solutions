# Approach
1. **Initialize a Stack:** Maintain a list `stack` to keep track of the integers waiting to be processed.
2. **Process Tokens Linearly:** Loop through each string `token` in the input list:
   - If the token is a number, Convert it to an integer using `int(token)` and push it onto the stack.
   - If the token is an operator (`+`, `-`, `*`, `/`), pop the top two numbers from the stack. Notice that the *first* number popped is actually the second operand (`number_2`), and the *second* number popped is the first operand (`number_1`).
3. **Execute Operation Safely:** Pass these operands to a helper function `calculate` which maps the operator string to its respective mathematical function using a dictionary of lambdas.
   - *Note on Division:* Python's standard `//` truncates toward negative infinity (e.g., `-1 // 2 = -1`), but the problem requires truncation toward zero. Using `int(number_1 / number_2)` correctly drops the decimal part and truncates toward zero as required (e.g., `int(-0.5) = 0`).
4. **Return Final Result:** After iterating through all tokens, exactly one value remains in the stack, which is the final evaluated result.

# Complexity
- Time complexity:
\[O(n)\]
*Process each token exactly once. Pushing, popping, and dictionary lookups all take O(1) constant time, making the overall runtime linear with respect to the number of tokens.*

- Space complexity:
\[O(n)\]
*In the worst-case scenario (such as an expression consisting of all numbers followed by all operators), the stack will store up to n/2 + 1 elements, which scales linearly with the input size.*

# Code
```python3 []
class Solution:
    def calculate(self, number_1, number_2, operator):
        operations = {
            "+": lambda: number_1 + number_2,
            "-": lambda: number_1 - number_2,
            "*": lambda: number_1 * number_2,
            "/": lambda: int(number_1 / number_2),
        }
        return operations[operator]()

    def evalRPN(self, tokens: list[str]) -> int:
        operators = ("+", "-", "*", "/")
        stack = []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                number_2 = stack.pop()
                number_1 = stack.pop()
                stack.append(self.calculate(number_1, number_2, token))

        return stack[0]
```