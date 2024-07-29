# Topics
- Python3
- Array

# Approach
- **Iterate through the list to select the middle soldier (`j`) of the triplet:**
  - This middle soldier (`rating[j]`) is considered as the middle element of the potential triplet.

- **Count elements less than and greater than `rating[j]` on both sides:**
  - Count how many elements to the left of `j` are less than `rating[j]` (`left_less`) and how many are greater (`left_greater`).
  - Similarly, count how many elements to the right of j are less than `rating[j]` (`right_less`) and how many are greater (`right_greater`).

- **Calculate the number of valid teams:**
  - For an increasing triplet, multiply the count of elements less than `rating[j]` on the left by the count of elements greater than `rating[j]` on the right (`left_less * right_greater`).
  - For a decreasing triplet, multiply the count of elements greater than `rating[j]` on the left by the count of elements less than `rating[j]` on the right (`left_greater * right_less`).

- **Sum up the counts of valid teams.**
<!-- Describe your approach to solving the problem. -->

# **Dry Run:**
- Initialize `count` to 0.
- Loop through each middle element `j` from 1 to `length - 2`.

- **Iteration for j = 1 (rating[1] = 5):**
  - Left Side Calculation (i from 0 to 0):
    - `rating[0] = 2`
      - `left_less` increases to 1 (since 2 < 5)
      - `left_greater` remains 0 (since 2 is not greater than 5)

  - **Right Side Calculation (k from 2 to 4):**
    - `rating[2] = 3`
      - `right_less` increases to 1 (since 3 < 5)
      - `right_greater` remains 0 (since 3 is not greater than 5)

    - `rating[3] = 4`
      - `right_less` increases to 2 (since 4 < 5)
      - `right_greater` remains 0 (since 4 is not greater than 5)

    - `rating[4] = 1`
      - `right_less` increases to 3 (since 1 < 5)
      - `right_greater` remains 0 (since 1 is not greater than 5)

  - **Team Calculation:**
    - `left_less` * `right_greater` = 1 * 0 = 0 (no increasing triplet)
    - `left_greater` * `right_less` = 0 * 3 = 0 (no decreasing triplet)

  - `count` remains 0 after this iteration.

- **Iteration for j = 2 (rating[2] = 3):**
  - Left Side Calculation (i from 0 to 1):
    - `rating[0] = 2`
      - `left_less` increases to 1 (since 2 < 3)
      - `left_greater` remains 0 (since 2 is not greater than 3)

    - `rating[1] = 5`
      - `left_greater` increases to 1 (since 5 > 3)
      - `left_less` remains 1 (since 5 is not less than 3)

  - Right Side Calculation (k from 3 to 4):
    - `rating[3] = 4`
      - `right_less` remains 0 (since 4 is not less than 3)
      - `right_greater` increases to 1 (since 4 > 3)

    - `rating[4] = 1`
      - `right_less` increases to 1 (since 1 < 3)
      - `right_greater` remains 1 (since 1 is not greater than 3)

  - **Team Calculation:**
    - `left_less` * right_greater = 1 * 1 = 1 (one increasing triplet: [2, 3, 4])
    - `left_greater` * right_less = 1 * 1 = 1 (one decreasing triplet: [5, 3, 1])
  - `count` increases to 2 after this iteration.

- **Iteration for j = 3 (rating[3] = 4):**
  - Left Side Calculation (i from 0 to 2):
    - `rating[0] = 2`
      - `left_less` increases to 1 (since 2 < 4)
      - `left_greater` remains 0 (since 2 is not greater than 4)

    - `rating[1] = 5`
      - `left_greater` increases to 1 (since 5 > 4)
      - `left_less` remains 1 (since 5 is not less than 4)

    - `rating[2] = 3`
    - `left_less` increases to 2 (since 3 < 4)
    - `left_greater` remains 1 (since 3 is not greater than 4)

  - Right Side Calculation (k from 4 to 4):
    - `rating[4] = 1`
      - `right_less` increases to 1 (since 1 < 4)
      - `right_greater` remains 0 (since 1 is not greater than 4)
  - Team Calculation:
    - `left_less` * `right_greater` = 2 * 0 = 0 (no increasing triplet)
    - `left_greater` * `right_less` = 1 * 1 = 1 (one decreasing triplet: [5, 4, 1])

    - `count` increases to 3 after this iteration.

- **Final Count:**
  - The total count of valid teams is `3`.


# Complexity
- Time complexity: `O(N^2)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)
        count = 0

        for j in range(1, length-1):
            left_less = left_greater = 0
            right_less = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                if rating[i] > rating[j]:
                    left_greater += 1

            for k in range(j+1, length):
                if rating[k] < rating[j]:
                    right_less += 1
                if rating[k] > rating[j]:
                    right_greater += 1

            count += left_less * right_greater + left_greater * right_less

        return count

```