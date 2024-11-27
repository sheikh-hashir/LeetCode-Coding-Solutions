# Topics
- Array
- Python3

# Intuition
The problem requires us to replace each number in the list with the sum of a specific number of adjacent elements. The direction (left or right) and the number of elements to sum depend on the value of `k`. If `k=0`, all elements should be replaced with 0. When `k>0`, we sum elements to the right; when `k<0`, we sum elements to the left.
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
- **Handle the Special Case:** If `k=0`, return a list of zeros of the same length as the input.
- **Extend the Array:** To simplify handling circular references, extend the array to 3 times its original length. This ensures the indices for adjacent sums remain valid without worrying about wrapping around.
- **Iterate Through the Array:** For each position in the original array:
  - If `k>0`, sum the next `k` elements starting from the next position.
  - If `k<0`, sum the previous `∣k∣` elements before the current position
- Append the computed sum for each position into the result array.

<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: Calculating the sum for each index involves summing `∣k∣` elements. Since this happens for `n` elements in the list, the total complexity is `O(n⋅∣k∣)`.
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: The extended array takes `O(3n)`, and the result array takes `O(n)`. Therefore, the total space complexity is `O(n)`.
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        if k == 0:
            return [0] * length
        result = []
        code = code + code + code
        for i in range(length, length*2):
            if k > 0:
                result.append(sum(code[i+1: i+1+k]))
            if k < 0:
                result.append(sum(code[i+k: i]))
        return result
```