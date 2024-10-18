# Topics
- Array
- Hash Table
- Python3

# Intuition
- The goal is to divide the players (represented by their skill levels) into pairs such that each pair has the same total skill level, and we want to maximize the sum of the products of the skill levels of the players in each pair.
- To do this, we need to first calculate the target sum for each pair and then check if it's possible to form such pairs.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Calculate the Target for Each Pair:**
  - The target sum for each pair is calculated by dividing the total sum of all skill levels by half the number of players (since each pair consists of two players).
- **Use a Hash Map for Counting:**
  - We use a hash map (or dictionary) to count the frequency of each skill level.
- **Form Pairs:**
  - For each skill level, find the complement skill level needed to reach the target sum. If the complement exists, form a pair and accumulate the product of the two skills. Adjust the count of both the current skill and its complement in the hash map.
- **Return the Result:**
  - If all pairs can be formed correctly, return the sum of the products. If any pair cannot be formed, return `-1` to indicate that it's impossible to divide the players as required.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of players. This is because we iterate through the list of skills twice: once to populate the hash map and once to form pairs.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(n)`, since we store the frequency of each skill level in the hash map.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
from collections import defaultdict
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Calculate the target sum for each pair
        total_sum = sum(skill)
        n = len(skill)

        # If the total sum isn't divisible by the number of pairs, return -1 (invalid case)
        if total_sum % (n // 2) != 0:
            return -1

        target = total_sum // (n // 2)

        # Create a hashmap to store the count of each skill value
        cache = defaultdict(int)

        # Populate the hashmap with the frequency of each skill value
        for s in skill:
            cache[s] += 1

        _sum = 0

        # Iterate through the skill array
        for s in skill:
            # If this skill value has already been used in a pair, skip it
            if cache[s] == 0:
                continue

            # Calculate the complement that should pair with this skill to form the target
            complement = target - s

            # Check if the complement exists in the hashmap and has a non-zero count
            if cache[complement] > 0:
                # If it's the same number, ensure there are at least 2 of them available
                if s == complement and cache[s] < 2:
                    return -1

                # Form the pair and add their product to the result
                _sum += s * complement

                # Decrease the count for both the current number and its complement
                cache[s] -= 1
                cache[complement] -= 1
            else:
                # If the complement doesn't exist, return -1
                return -1

        # Return the accumulated sum of the products of the pairs
        return _sum

```