class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(set(nums))
        duplicate = sum(nums) - actual_sum
        return [duplicate, total_sum - actual_sum]
