from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)
        count = 0

        for j in range(1, length - 1):
            left_less = left_greater = 0
            right_less = right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                if rating[i] > rating[j]:
                    left_greater += 1

            for k in range(j + 1, length):
                if rating[k] < rating[j]:
                    right_less += 1
                if rating[k] > rating[j]:
                    right_greater += 1

            count += left_less * right_greater + left_greater * right_less

        return count
