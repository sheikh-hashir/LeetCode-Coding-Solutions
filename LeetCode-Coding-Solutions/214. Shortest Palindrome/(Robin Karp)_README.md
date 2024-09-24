# Topics
- String
- String Matching
- Hash Function
- Python3

# Intuition
- Initial thought is to find the shortest palindrome by adding characters in front of the given string.
- The idea is to identify the longest palindromic prefix and then determine which characters need to be added to the front to form a complete palindrome.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Understanding the Problem:**
  - The goal is to construct the shortest palindrome that can be formed by adding characters only to the front of the input string.
  - A palindrome reads the same forwards and backwards.

- **Identifying the Longest Palindromic Prefix:**
  - To solve the problem efficiently, we want to identify the longest palindromic prefix of the string.
  - The characters following this prefix will need to be added to the front in reverse order to form the complete palindrome.

- **Using Hashing for Efficient Comparison:**
  - To quickly determine if the prefix matches the reversed suffix, we can use a hashing technique similar to the Rabin-Karp algorithm.
  - This involves computing hash values for both the prefix and the suffix of the string.

- **Algorithm Steps:**
  - **Initialize two hash values:** one for the prefix (`prefix`) and one for the suffix (`suffix`).
  - Use a base value (e.g., 29) and a large prime modulus (e.g., `10^9 + 7`) to avoid hash collisions and keep the values manageable.
  - Loop through each character in the string:
    - Update the `prefix` hash value by incorporating the current character.
    - Update the `suffix` hash value to include the current character multiplied by a power of the base (to account for the position).
    - Update the `power` for the next iteration.
    - If the current `prefix` hash matches the `suffix` hash, it indicates that we have found a palindromic prefix, and we can update the last_index to this position.
  - After the loop, any characters following the `last_index` in the original string are not part of the palindrome. These characters need to be reversed and added to the front of the string.

- **Constructing the Result:**
  - Finally, take the substring of characters after the longest palindromic prefix, reverse it, and concatenate it with the original string to form the shortest palindrome.
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: `O(n)`, where `n` is the length of the string. The algorithm processes each character in linear time.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: `O(1)`. The algorithm uses a fixed amount of space for variables and does not utilize additional data structures proportional to the input size.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Robin Karp Algorithm
        prefix = 0
        suffix = 0
        base = 29
        last_index = 0
        power = 1
        mod = 10**9 + 7
        for idx, _char in enumerate(s):
            char = (ord(_char) - ord("a")) + 1

            prefix = ((prefix * base) + char) % mod
            suffix = (suffix + char * power) % mod
            power *= base % mod

            if prefix == suffix:
                last_index = idx

        suffix = s[last_index + 1:]
        return suffix[::-1] + s
```