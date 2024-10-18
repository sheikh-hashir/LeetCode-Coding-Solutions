from collections import defaultdict
from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_sum = defaultdict(int)
        for word in words:
            for i in range(1, len(word) + 1):
                prefix_sum[word[:i]] += 1

        return [
            sum(prefix_sum[word[:i]] for i in range(1, len(word) + 1)) for word in words
        ]
