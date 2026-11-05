# O(N log M) Binary Search for Closest Element | Clean & Fast

# Intuition
The problem asks us to count how many elements in `arr1` do not have any element in `arr2` within a distance of `d`. Instead of checking every element in `arr1` against every element in `arr2` (which takes \(O(n \times m)\) time) and, sort `arr2`. Once `arr2` is sorted and, use binary search to instantly locate the closest neighbor to our target number. If even the closest neighbor's absolute difference is greater than `d`, so no other element in `arr2` can satisfy the condition.

# Approach
1. **Sort the Reference Array:** First sort `arr2` in ascending order. This sets up the structure required to perform binary searches.
2. **Binary Search for Closest Neighbor (`get_closest_index`):** For each number in `arr1` perform a binary search on `arr2`:
   - Track the `min_diff` and its corresponding `closest_idx`.
   - If an exact match (`arr[mid] == target`), the difference is `0`, then return immediately.
   - Otherwise, narrow our search range down to find the closest possible value.
3. **Distance Evaluation:** Check the absolute difference between the current number from `arr1` and its closest match found in `arr2`. If `abs(num - arr2[closest_index]) > d`, it means no element in `arr2` violates the distance constraint, then increment the `count`.

# Complexity
- Time complexity:
\[O(m \log m + n \log m)\]
*Where \(m\) is the length of `arr2` and \(n\) is the length of `arr1`. Sorting `arr2` takes \(O(m \log m)\) time. Then, for each of the \(n\) elements in `arr1`, perform a binary search over `arr2` which takes \(O(\log m)\) time.*

- Space complexity:
\[O(1)\]
(or \[O(m)\] depending on python's built-in sorting allocation)
*The binary search function runs in-place with a few pointers, using \(O(1)\) auxiliary space. Python's Timsort (`arr2.sort()`) can utilize up to \(O(m)\) space internally to perform the sort.*

# Code
```python3 []
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
```