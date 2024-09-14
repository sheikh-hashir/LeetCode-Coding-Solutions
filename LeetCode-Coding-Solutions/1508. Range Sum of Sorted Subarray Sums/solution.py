from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        """
        Calculate the sum of all possible sub-arrays of the given array within the specified range.

        Args:
            nums: A list of integers representing the input array.
            n: An integer representing the length of the input array.
            left: An integer representing the left boundary of the range.
            right: An integer representing the right boundary of the range.

        Returns:
            int: The range sum of sorted sub-array sums within the specified range.
        """

        result = []
        length = len(nums)
        for idx in range(length):
            previous_sum = 0
            for jdx in range(idx, length):
                previous_sum += nums[jdx]
                result.append(previous_sum)
        result.sort()
        return sum(result[left - 1 : right]) % ((10 ** 9) + 7)
