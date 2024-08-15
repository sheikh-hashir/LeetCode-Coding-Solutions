from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        """
        Check if two arrays can be made equal by reversing sub-arrays.

        Args:
            target: A list of integers representing the target array.
            arr: A list of integers representing the input array.

        Returns:
            bool: True if the arrays can be made equal by reversing sub-arrays, False otherwise.
        """

        return sorted(target) == sorted(arr)