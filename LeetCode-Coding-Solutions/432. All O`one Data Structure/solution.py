from collections import defaultdict


class AllOne:
    def __init__(self):
        self.dict = defaultdict(int)  # Stores the count of each key
        self.count_freq = defaultdict(set)  # Stores keys for each frequency
        self._max = None  # Current max key
        self._min = None  # Current min key

    def _update_min_max(self):
        # Update the _max key
        if self.dict:
            max_freq = max(self.count_freq.keys())
            self._max = next(iter(self.count_freq[max_freq]))  # Any key with max freq
        else:
            self._max = None

        # Update the _min key
        if self.dict:
            min_freq = min(self.count_freq.keys())
            self._min = next(iter(self.count_freq[min_freq]))  # Any key with min freq
        else:
            self._min = None

    def inc(self, key: str) -> None:
        if key in self.dict:
            old_count = self.dict[key]
            self.count_freq[old_count].remove(key)  # Remove key from old count
            if not self.count_freq[old_count]:
                del self.count_freq[old_count]
            new_count = old_count + 1
        else:
            new_count = 1

        # Increment the count of the key
        self.dict[key] = new_count
        self.count_freq[new_count].add(key)  # Add key to new count

        self._update_min_max()

    def dec(self, key: str) -> None:
        if key not in self.dict:
            return

        old_count = self.dict[key]
        self.count_freq[old_count].remove(key)  # Remove key from old count
        if not self.count_freq[old_count]:
            del self.count_freq[old_count]

        if old_count == 1:
            del self.dict[key]  # Remove key from dict if its count becomes 0
        else:
            new_count = old_count - 1
            self.dict[key] = new_count
            self.count_freq[new_count].add(key)  # Add key to new count

        self._update_min_max()

    def getMaxKey(self) -> str:
        return "" if self._max is None else self._max

    def getMinKey(self) -> str:
        return "" if self._min is None else self._min


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
