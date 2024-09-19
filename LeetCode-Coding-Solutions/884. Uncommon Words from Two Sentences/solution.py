from collections import defaultdict
from itertools import chain
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        common_dict = defaultdict(int)
        for word in chain(s1.split(), s2.split()):
            common_dict[word] += 1

        return [key for key, value in common_dict.items() if value == 1]
