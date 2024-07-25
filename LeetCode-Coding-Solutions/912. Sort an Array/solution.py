from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(array, left, mid, right):
            left_array = array[left : mid + 1]
            right_array = array[mid + 1 : right + 1]

            array_one_idx = 0  # Initial index of first sub-array
            array_two_idx = 0  # Initial index of second sub-array
            merged_array_idx = left  # Initial index of merged array

            left_array_length = len(left_array)
            right_array_length = len(right_array)
            # Merge the temp arrays back into array[left..right]
            while (
                array_one_idx < left_array_length and array_two_idx < right_array_length
            ):
                if left_array[array_one_idx] <= right_array[array_two_idx]:
                    array[merged_array_idx] = left_array[array_one_idx]
                    array_one_idx += 1
                else:
                    array[merged_array_idx] = right_array[array_two_idx]
                    array_two_idx += 1
                merged_array_idx += 1

            # Copy the remaining elements of left[], if any
            while array_one_idx < left_array_length:
                array[merged_array_idx] = left_array[array_one_idx]
                array_one_idx += 1
                merged_array_idx += 1

            # Copy the remaining elements of right[], if any
            while array_one_idx < right_array_length:
                array[merged_array_idx] = right_array[array_two_idx]
                array_two_idx += 1
                merged_array_idx += 1

        def mergeSort(nums: list, start: int, end: int):
            if start >= end:
                return

            mid = start + (end - start) // 2
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            merge(nums, start, mid, end)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
