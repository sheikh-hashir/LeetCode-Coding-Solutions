class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i = len(s)
        while i >= 0 and s[:i] != s[:i][::-1]:
            i -= 1

        return f"{s[i:][::-1]}{s}"
