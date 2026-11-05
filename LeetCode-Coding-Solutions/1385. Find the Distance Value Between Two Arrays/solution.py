class Solution:
    def get_closest_index(self, arr, target):
        low = 0
        high = len(arr) - 1

        min_diff = float("inf")
        closest_idx = -1

        while low <= high:
            mid = low + (high - low) // 2
            current_diff = abs(target - arr[mid])

            if current_diff < min_diff:
                min_diff = current_diff
                closest_idx = mid

            if arr[mid] == target:
                return mid

            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return closest_idx

    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()

        count = 0
        for num in arr1:
            closest_index = self.get_closest_index(arr2, num)
            if abs(num - arr2[closest_index]) > d:
                count += 1

        return count
