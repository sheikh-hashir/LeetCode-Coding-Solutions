# Intuition
- The problem asks to implement a calendar that allows us to book intervals without any overlap.
- This suggests a straightforward approach where we maintain a list of all intervals and ensure no new interval conflicts with existing ones.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
We can maintain a list of intervals (`self.intervals`) representing the start and end times of booked intervals. To book a new interval, we iterate through all previously booked intervals and check for any overlap using the condition `end > interval[0] and start < interval[1]`. If no overlap is found, we add the new interval to the list; otherwise, we return `False`.
- Initialize an empty list to store booked intervals.
- For each booking request, check if it overlaps with any previously booked interval.
- If there's no overlap, append the new interval to the list and return `True`; otherwise, return `False`.


<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of previously booked intervals, as each new booking checks against all existing bookings.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)` because we store all intervals in a list.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class MyCalendar:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        for interval in self.intervals:
            if end > interval[0] and start < interval[1]:
                return False
        self.intervals.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```