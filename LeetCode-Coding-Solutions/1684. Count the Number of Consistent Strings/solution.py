from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(all(_char in allowed for _char in word) for word in words)
