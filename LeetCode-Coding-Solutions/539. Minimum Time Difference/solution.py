from datetime import datetime, timedelta
from typing import List


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
