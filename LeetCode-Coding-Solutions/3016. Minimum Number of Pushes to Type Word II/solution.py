from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = sorted(Counter(word).items(), key=lambda x: x[1], reverse=True)
        multiplier = 1
        result = 0
        for index, (_, value) in enumerate(frequency):
            if index % 8 == 0 and index != 0:
                multiplier += 1
            result += value * multiplier
        return result
