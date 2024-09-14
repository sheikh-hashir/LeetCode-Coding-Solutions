# Topics
- Array
- Greedy
- Python3

# Intuition
- The problem asks us to simulate the process of providing change for each customer who pays with a bill.
- The key challenge is ensuring that we can always give the correct change using the bills we have already collected.

# Approach
- We maintain a dictionary `change` to keep track of the number of 5, 10, and 20 dollar bills we have.
- For each bill in the `bills` list:
  - Increment the count of that bill in change.
  - Calculate the required change by subtracting 5 from the bill value.
  - Attempt to give change using the largest denominations first (20, 10, then 5) to minimize the number of bills used.
  - If we cannot give the exact change (i.e., `return_` is not zero), return `False`.
- If we successfully process all bills, return `True`.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the number of bills, as we iterate through the list and for each bill, we potentially iterate through the available denominations.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`, as we only use a fixed amount of extra space for the change dictionary
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            change[bill] += 1
            return_ = bill - 5

            for val in (20, 10, 5):
                while return_ >= val and change[val] > 0:
                    return_ -= val
                    change[val] -= 1

            if return_ != 0:
                return False
        return True
```