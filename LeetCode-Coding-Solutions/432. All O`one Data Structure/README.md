# Topics
- Hash Table
- Python3

# Intuition
- The problem asks us to maintain a data structure that supports incrementing, decrementing, and retrieving the keys with the maximum and minimum counts.
- A dictionary can store the frequency of each key, and another dictionary can group keys by their frequencies.
- This will allow us to efficiently find the maximum and minimum frequencies.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Dictionary for Key Count:**
  - Use a dictionary (`self.dict`) to store the count (frequency) of each key. This helps in incrementing and decrementing the key counts.

- **Frequency Grouping:**
  - Another dictionary (`self.count_freq`) will map frequencies to the set of keys that share the same frequency. This allows us to track which keys belong to which frequency.

- **Increment (`inc`):**
  - When incrementing a key, update its count in the `self.dict`. If it already exists, remove the key from the set corresponding to its old frequency, increment the count, and add the key to the set corresponding to the new frequency.
  - Call `_update_min_max()` to update the minimum and maximum keys based on the new counts.

- **Decrement (`dec`):**
  - For decrement, the key's frequency is reduced by one. If the frequency becomes zero, remove the key completely. If the frequency is just reduced, move it to the appropriate frequency set.
  - Again, call `_update_min_max()` to adjust the min and max keys.

- **_update_min_max:**
  - After every increment or decrement, this function updates the keys with the highest and lowest frequencies by examining the `count_freq` dictionary.

- **Edge Cases:**
  - If no keys exist, `getMinKey` and `getMaxKey` return an empty string.




<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity:
  - `inc` and `dec` operations involve inserting and deleting elements from sets, which are on average `O(1)`. The max and min frequency updates are also `O(1)` due to the efficient frequency grouping.
  - Hence, the overall time complexity for each operation (`inc`, `dec`, `getMaxKey`, `getMinKey`) is `O(1)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
  - We use two dictionaries (`self.dict` and `self.count_freq`), both of which store data proportional to the number of unique keys. Therefore, the space complexity is `O(n)`, where `n` is the number of unique keys.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
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
        return "" if not self._max else self._max

    def getMinKey(self) -> str:
        return "" if not self._min else self._min


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

```