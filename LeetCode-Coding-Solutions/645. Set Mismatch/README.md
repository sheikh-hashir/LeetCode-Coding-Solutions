# Approach
- The approach is to calculate the expected total sum (total_sum) using the formula for the sum of the first n natural numbers, which is n * (n + 1) / 2. 
- Then, calculate the actual sum (actual_sum) by summing the unique elements in the given list nums using a set. 
- The repeated element (duplicate) is found by subtracting the actual sum from the sum of all elements in nums. 
- The missing element is then calculated as the difference between the total sum and the actual sum.

# Complexity
- Time complexity:
`O(N)`
*Converting the array to a set takes O(N) time. Calculating the sum of the raw array and the set also takes linear O(N) time. The remaining arithmetic checks operate in O(1) constant time.*

- Space complexity:
`O(N)`
*Although the math arithmetic uses constant space, casting the input list into a `set(nums)` dynamically allocates a hash set containing up to N unique elements, requiring linear auxiliary memory space.*

# Code
```
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = n * (n + 1) // 2
        actual_sum = sum(set(nums))
        duplicate = sum(nums) - actual_sum
        return [duplicate, total_sum - actual_sum]

```