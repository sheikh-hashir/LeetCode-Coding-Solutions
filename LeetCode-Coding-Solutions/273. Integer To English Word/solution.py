class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens_map = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }

        def get_string(n):
            result = []
            if hundreds := n // 100:
                result.append(f"{ones_map[hundreds]} Hundred")
            last_2 = n % 100
            if last_2 >= 20:
                tens, ones = last_2 // 10, last_2 % 10
                result.append(tens_map[tens])
                if ones:
                    result.append(ones_map[ones])
            elif last_2:
                result.append(ones_map[last_2])

            return " ".join(result)

        prefix = ["", " Thousand", " Million", " Billion"]
        i = 0
        result = []
        while num:
            digits = num % 1000

            if s := get_string(digits):
                result.append(f"{s}{prefix[i]}")
            i += 1
            num //= 1000
        result.reverse()
        return " ".join(result)
