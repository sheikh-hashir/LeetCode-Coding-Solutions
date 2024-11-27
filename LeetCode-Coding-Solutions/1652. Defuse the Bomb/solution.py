from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        if k == 0:
            return [0] * length
        result = []
        code = code + code + code
        for i in range(length, length * 2):
            if k > 0:
                result.append(sum(code[i + 1 : i + 1 + k]))
            if k < 0:
                result.append(sum(code[i + k : i]))
        return result
