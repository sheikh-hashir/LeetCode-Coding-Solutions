class Solution:
    def minMoves(self, nums: list[int]) -> int:
        _min = min(nums)
        return sum(num - _min for num in nums)
