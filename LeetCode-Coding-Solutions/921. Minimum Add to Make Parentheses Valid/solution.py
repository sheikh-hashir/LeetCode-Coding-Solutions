class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening, result = 0, 0
        for char in s:
            if char == "(":
                opening += 1
            elif char == ")":
                if opening > 0:
                    opening -= 1
                else:
                    result += 1
        return opening + result
