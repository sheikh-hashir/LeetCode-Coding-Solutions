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
