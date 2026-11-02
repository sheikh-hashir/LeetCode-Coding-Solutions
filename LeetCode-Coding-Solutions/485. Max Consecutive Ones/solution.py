class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        return max(len(s) for s in "".join(map(str, nums)).split("0"))
