# Topics
- Array
- Math
- Sorting
- String
- Python3
- Datetime

# Intuition
- The key challenge of the problem is that time is circular, so we need to account for the difference between the last and first time in the sorted list.
- The goal is to minimize the time difference between any two time points, and sorting the list simplifies this process by making it easier to compare consecutive times.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Convert times to datetime objects:**
  - First, convert all the time strings to datetime objects so we can easily calculate the time differences.
- **Sort the times:**
  - Sorting helps us ensure that the time points are in order, making it easier to compute the difference between consecutive times.
- **Handle the circular time difference:**
  - To account for the circular nature of time (i.e., 23:59 and 00:00), we add an extra time point by adding 24 hours to the first time and appending it to the sorted list.
- **Compute differences:**
  - Iterate through the sorted list, calculating the difference between consecutive time points and keeping track of the minimum difference.
- **Return the minimum difference:**
  - After iterating through the list, return the smallest difference in minutes.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: Sorting the list of time points takes `O(nlogn)`, and calculating the time differences takes `O(n)`. Hence, the total time complexity is `O(nlogn)`, where `n` is the number of time points.


<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: We store the list of datetime objects, so the space complexity is `O(n)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from datetime import datetime

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        _min = float("inf")
        time_format = "%H:%M"
        times = sorted(datetime.strptime(time, time_format) for time in timePoints)

        times.append(times[0] + timedelta(days=1))

        for i in range(1, len(times)):
            difference = int((times[i] - times[i - 1]).total_seconds()) // 60
            _min = min(_min, difference)

        return _min


```