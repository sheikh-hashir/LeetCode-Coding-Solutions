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
