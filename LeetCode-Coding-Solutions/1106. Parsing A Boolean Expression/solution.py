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
