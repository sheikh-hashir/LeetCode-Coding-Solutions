class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        result = "0"

        # Build the sequence up to nth iteration
        for _ in range(1, n + 1):
            inverted = "".join("1" if char == "0" else "0" for char in result)
            result = f"{result}1{inverted[::-1]}"

        # Return the k-th character (1-based index, so subtract 1)
        return result[k - 1]
