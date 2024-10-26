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
