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
