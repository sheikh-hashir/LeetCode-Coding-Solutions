class Solution:
    def minChanges(self, s: str) -> int:
        length = len(s)
        return sum(1 if s[i] != s[i + 1] else 0 for i in range(0, length - 1, 2))
