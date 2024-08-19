# Topics
- Math
- Python3

# Intuition
- To find the minimum number of steps to get n characters on the screen starting with just one character `A`, we need to factorize `n` and use these factors as the steps.
- This is because, in each step, you either copy the entire current string or paste it, and the optimal way to do this is to divide `n` by its smallest possible factors.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- If `n` `is` `1`, then no steps are needed, so return `0`.
- If `n` is a prime number, the minimum number of steps required is `n` itself because you would have to keep copying and pasting the entire string.
- Otherwise, for each number from `4` upwards, check if it is a divisor of `n`. If it is, keep dividing n by that number and add the divisor to the result. This process continues until `n` is reduced to `1`.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: The time complexity of the solution is approximately `O(sqrt(n))` because the inner loop checks for factors starting from `4` upwards.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: The space complexity is `O(1)` since only a constant amount of space is used.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def minSteps(self, n: int) -> int:
        def is_prime(num: int):
            if num <= 3:
                return True
            for i in range(num//2):
                if i % 2 == 0:
                    return False
            return True

        if n == 1:
            return 0
        if is_prime(n):
            return n

        result = 0
        i = 2
        while n > 1:
            while n % i == 0:
                result += i
                n //= i
            i += 1
        return result
```