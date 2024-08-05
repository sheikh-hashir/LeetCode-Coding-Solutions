from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        frequency = Counter(arr)
        distinct_items = [item for item in arr if frequency[item] == 1]
        return distinct_items[k - 1] if len(distinct_items) >= k else ""
