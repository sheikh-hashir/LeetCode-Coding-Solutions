# Approach
- The goal is to convert a given integer into its English words representation. To achieve this, we break down the number into manageable chunks and process each chunk using predefined mappings for numbers and words.

- **Handle Zero Case:**
  - If the input number is zero, immediately return the string "Zero".

- **Define Mappings:**
  - **Ones Map:** A dictionary to map numbers from 1 to 19 to their corresponding English words.
  - **Tens Map:** A dictionary to map the multiples of ten (20, 30, ..., 90) to their corresponding English words.
```
ones_map = {
    1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
    6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
    11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
    15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
}

tens_map = {
    2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
    6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
}
```

- **Helper Function get_string:**
  - This function converts numbers less than 1000 into words.
  - **Hundreds Place:** If the number is 100 or more, handle the hundreds place by dividing by 100.
  - **Tens and Ones Place:**
    - If the last two digits are 20 or more, handle the tens and ones separately.
    - If the last two digits are less than 20, directly use the ones map for conversion.
```
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
```

- **Process Larger Units:**
  - Use a list `prefix` to represent the thousand, million, and billion units.
  - Iterate through the number in chunks of 1000:
  - Use the `get_string` function to convert each chunk into words.
  - Append the corresponding unit (thousand, million, etc.) to each chunk.
```
prefix = ["", " Thousand", " Million", " Billion"]
i = 0
result = []
while num:
    digits = num % 1000
    if s := get_string(digits):
        result.append(f"{s}{prefix[i]}")
    i += 1
    num //= 1000
```

- **Combine Results:**
  - Reverse the result list to get the correct order.
  - Join the words to form the final string.
```
result.reverse()
return " ".join(result)
```
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)` where `n` is the number of digits in the number. Each digit is processed a constant number of times.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)` additional space, not considering the space used to store the mappings and result string.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones_map = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
            6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }

        tens_map = {
            2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
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

```