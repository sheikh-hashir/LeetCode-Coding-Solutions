class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        index = 0
        length = len(nums)
        result = []
        while index < length:
            nums[abs(nums[index]) - 1] = abs(nums[abs(nums[index]) - 1]) * -1
            index += 1
        return [idx + 1 for idx, num in enumerate(nums) if num > 0]
