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