# Clean In-Place Brute Force | O(1) Auxiliary Space

# Intuition
The problem asks us to find the first element to the right of each item that is less than or equal to it and subtract that value as a discount. Instead of maintaining a separate results list and writing custom conditional blocks to catch edge cases (like the last item or items with no discount), and optimize the brute-force lookahead approach by modifying the input array **in-place**.

# Approach
1. **Iterate Through Items:** Use an outer loop with pointer `idx` to track each item from the beginning to the end of the array.
2. **Scan Future Items:** An inner loop starting at `idx + 1` scans forward through all upcoming items using a secondary pointer `jdx`.
3. **Apply and Break:** The moment a future item is encountered where `prices[idx] >= prices[jdx]`, update the current price directly (`prices[idx] -= prices[jdx]`) and immediately `break` out of the inner loop. Breaking ensures that it only applies to the *first* eligible discount.
4. **Natural Boundary Handling:** If no discount is found, the inner loop finishes naturally without making any modifications. Similarly, for the final item in the array, the inner loop range `range(length, length)` is empty, so it safely remains untouched without needing manual edge-case code.

# Complexity
- Time complexity:
`O(N^2)`
*In the worst-case scenario (such as prices sorted in strictly ascending order), no discounts are ever found. The inner loop will scan all the way to the end of the array for every single element, resulting in a quadratic runtime.*

- Space complexity:
`O(1)`
*By modifying the `prices` array directly in-place, the algorithm avoids allocating any new collections or auxiliary arrays, consuming true constant extra space.*

# Code
```python3 []
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        length = len(prices)

        for idx in range(length):
            for jdx in range(idx + 1, length):
                if prices[idx] >= prices[jdx]:
                    prices[idx] -= prices[jdx]
                    break
        return prices
```