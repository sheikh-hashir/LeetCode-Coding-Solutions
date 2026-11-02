# Topics
- Array
- Stack
- Simulation
- Python3

# Approach
1. **Pointers & Iteration:** Track our current progress in the `target` array using `current_target_index`. Use a `while` loop to stream integers starting from `idx = 1`.
2. **Early Exit:** Instead of blindly running all the way to `n`, stop our stream as soon as `idx` surpasses the maximum value in the target array (`target[-1]`). Any stream numbers larger than this are completely irrelevant.
3. **Simulating Operations:**
   - Every incoming stream number is pushed onto our stack (`result.append("Push")`).
   - If the current stream number `idx` matches the expected number at `target[current_target_index]`, successfully "keep" it and advance our target array pointer (`current_target_index += 1`).
   - If it does not match, it means this number is skipped in the target array. Immediately remove it from the stack (`result.append("Pop")`).
   - Increment `idx` to process the next number in the stream.

# Complexity
- Time complexity:
`O(m)`
*Where \(m\) is the maximum value inside the `target` array (\(target[-1] \le n\)). Loop exactly \(m\) times, doing constant time \(O(1)\) operations on each step, ensuring an optimal linear execution runtime.*

- Space complexity:
`O(1)`
*Excluding the memory allocated for the returned stack operations array (`result`), the logic uses only a few primitive integer pointers, running in constant auxiliary space.*

# Code
```python3 []
class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        result = []
        current_target_index = 0
        length = len(target)
        idx = 1

        while target[-1] >= idx:
            result.append("Push")
            if idx == target[current_target_index]:
                current_target_index += 1
            else:
                result.append("Pop")
            idx += 1
        return result
```