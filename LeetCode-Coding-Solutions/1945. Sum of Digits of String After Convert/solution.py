class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def calculate_digit_sum(num: int, _range: int):
            if _range == 0:
                return num

            new_num = 0
            while num:
                new_num += num % 10
                num //= 10

            return calculate_digit_sum(new_num, _range - 1)

        converted_number = int("".join(str(ord(_char) - ord("a") + 1) for _char in s))
        return calculate_digit_sum(converted_number, k)
