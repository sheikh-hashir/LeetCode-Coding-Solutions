class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        index = 0
        length = len(nums)
        while index < length // 2:
            result.append(nums[index])
            result.append(nums[index + n])

            index = index + 1

        return result
