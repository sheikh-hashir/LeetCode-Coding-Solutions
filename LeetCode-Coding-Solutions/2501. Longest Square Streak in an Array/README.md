# Topics
- Array
- Hash Table
- Sorting
- Python3

# Intuition
- The goal is to find the longest streak of numbers in which each number is the square of the previous number.
- This can be achieved by iterating through each number, squaring it iteratively, and counting the length of the streak if each squared value exists in the set of numbers.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Sort and Convert to Set:**
  - First, we sort the numbers and convert the list to a set to enable quick lookups.
  - This set allows us to efficiently check if the next squared number exists in `nums`.

- **Iterate Through Each Number:**
  - For each number, start a streak, setting the `current` variable to this number and initializing streak_length to zero.
  - While `current` (or its square) exists in the set, square `current` and increment the `streak_length`.

- **Track the Maximum Streak Length:**
  - After each streak, update `count` with the maximum streak length found.
  - If the longest streak length is 1 (meaning no streak could be formed), return `-1`; otherwise, return the maximum count.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - Sorting the list takes `O(nlogn)`.
  - The loop goes through each element and then iterates for each streak. In the worst case, squaring the numbers could make the while loop log-based since each squared value grows quickly. Overall complexity is `O(nlogn)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: We use `O(n)` space for storing the set of numbers.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        count = 0
        nums.sort()
        nums = set(nums)

        for n in nums:
            current = n
            streak_length = 0
            while current in nums:
                current = current ** 2
                streak_length += 1
            count = max(count, streak_length)
        return count if count != 1 else -1

```